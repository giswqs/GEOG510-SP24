print("Hello World!")

# %pip install -U leafmap
# %pip install -U rasterstats geopandas
dsm = 'https://open.gishub.org/data/elevation/dsm.tif'
hag = 'https://open.gishub.org/data/elevation/hag.tif'
buildings = 'https://open.gishub.org/data/elevation/buildings.geojson'
m = leafmap.Map()
m.add_cog_layer(dsm, name='DSM', palette='terrain')
m.add_cog_layer(hag, name='Height Above Ground', palette='magma')
m.add_geojson(buildings, layer_name='Buildings')
m
