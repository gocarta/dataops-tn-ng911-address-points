# dataops-tn-ng911-address-points
> Unofficial Mirror of Tennessee Next Generation 911 (NG911) Address Points within Hamilton County

<img width="443" height="415" alt="addresses" src="https://github.com/user-attachments/assets/0e10ade0-c3cf-493d-912b-a2f69d786529" />

## background
We need a way to securely and quickly geocode within a web app.

## source
[TN Next Generation 911 (NG911) Address Points](https://geodata.tn.gov/datasets/tnmap::tennessee-ng911-address-points/about)

## columns
| column | example | description |
| :--- | :--- | :--- |
| **AddNum_Pre** | `""` | Prefix for address name if applicable |
| **Add_Number** | `"1617"` | The address number |
| **AddNum_Suf** | `""` | Suffix for address name if applicable |
| **StNam_Full** | `"WILCOX BLVD"` | Full street name |
| **State** | `"TN"` | The state of the address, which is always "TN" for this dataset. |
| **Zip_Code** | `"37406"` | The postal code for the address. |
| **Longitude** | `-85.26937812` | The longitude location of the address. |
| **Latitude** | `35.05605029` | The latitude location of the address. |


## download links
- [metadata](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/meta.json)
- [csv](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.csv)
- [geojson](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.points.geojson)
- [geoparquet](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.parquet)
- [json](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.json)
- [json lines](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.jsonl)
- [shapefile](https://gocarta.s3.us-east-2.amazonaws.com/public/data/tn_ng911_address_points/v1/data.points.shp.zip)

## preview links
- You can query the data with SQL using [duckdb](https://shell.duckdb.org/#queries=v0,CREATE-TABLE-dataset-AS-SELECT-*-FROM-'s3%3A%2F%2Fgocarta%2Fpublic%2Fdata%2Ftn_ng911_address_points%2Fv1%2Fdata.parquet'~,Describe-dataset~,SELECT-State%2C-COUNT(*)-FROM-dataset-GROUP-BY-State~,SELECT-*-FROM-Dataset-WHERE-Add_Number-%3D-'1617'-AND-StNam_Full-%3D-'WILCOX-BLVD'-LIMIT-1~).
- Here's a proof-of-concept demo of client-side geocoding with this dataset: https://gocarta.github.io/dataops-tn-ng911-address-points/

## support
Post an issue [here](https://github.com/gocarta/dataops-tn-ng911-address-points/issues) or email the package author at DanielDufour@gocarta.org.
