# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datablob",
#     "requests",
#     "simple-env",
# ]
# ///

import datablob
import requests
import simple_env as se
import time

AWS_BUCKET_NAME = se.get("AWS_BUCKET_NAME")

AWS_BUCKET_PATH = se.get("AWS_BUCKET_PATH")

REQUEST_EXCEPTIONS_THRESHOLD = 10
BASE_URL = "https://services1.arcgis.com/YuVBSS7Y1of2Qud1/arcgis/rest/services/Tennessee_NG911_Address_Points/FeatureServer/0/query"

OUT_FIELDS = [
    "AddNum_Pre",
    "Add_Number",
    "AddNum_Suf",
    "StNam_Full",
    "State",
    "Zip_Code",
    "Longitude",
    "Latitude",
]

PAGE_SIZE = 2000

request_exceptions = 0
rows = []

for county in ["HAMILTON"]:
    offset = 0

    while True:
        try:
            params = {
                "where": f"County = '{county}'",
                "outFields": ",".join(OUT_FIELDS),
                "f": "json",
                "resultOffset": offset,
                "resultRecordCount": PAGE_SIZE,
            }
            resp = requests.get(BASE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(e)
            request_exceptions += 1
            print("request_exceptions:", request_exceptions)
            time.sleep(60)
            if request_exceptions > REQUEST_EXCEPTIONS_THRESHOLD:
                raise e

        features = data.get("features", [])
        if not features:
            break

        print(f"[dataops-tn-ng911-address-points] fetched {len(features)} features (offset={offset})")

        for feat in features:
            attrs = feat.get("attributes", {})
            row = {field: attrs.get(field) for field in OUT_FIELDS}
            rows.append(row)

        offset += len(features)
        print(f"[dataops-tn-ng911-address-points] num rows so far:", len(rows))

client = datablob.DataBlobClient(
    bucket_name=AWS_BUCKET_NAME, bucket_path=AWS_BUCKET_PATH
)

client.update_dataset(
    name="tn_ng911_address_points",
    description="Unofficial Mirror of Tennessee Next Generation 911 (NG911) Address Points",
    version="1",
    data=rows,
    column_names=OUT_FIELDS,
    json=True,
    jsonl=True,
    latitude_key="Latitude",
    longitude_key="Longitude",
    parquet=True,
    xlsx=False,
)

print(f"[dataops-tn-ng911-address-points] updated {len(rows)} rows")
