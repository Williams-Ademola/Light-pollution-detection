import geopandas as gpd
from blackmarble import BlackMarble, Product
import pandas as pd
import datetime as dt  # you used 'dt' but didn't use it — fixing that too

# Load Winnipeg region from geojson file
gdf = gpd.read_file("winnipeg.geojson")

# Auth is handled via env var: BLACKMARBLE_TOKEN
bm = BlackMarble()

# Use pd.to_datetime to create a DateTimeIndex, which BlackMarble expects
date_range = pd.to_datetime(["2024-06-01", "2024-06-02", "2024-06-03"])

# Download VNP46A1 product for June 1–3, 2024
ds = bm.raster(gdf=gdf, product_id=Product.VNP46A1, date_range=date_range)

# Inspect result
print(ds)
