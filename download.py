import json
# from esridump.dumper import EsriDumper
#
# d = EsriDumper('https://services1.arcgis.com/UWYHeuuJISiGmgXx/ArcGIS/rest/services/Part1_Crime_Beta/FeatureServer/0')
#
# # Iterate over each feature
# for feature in d:
#     print(json.dumps(feature))
#
# d = EsriDumper('https://services1.arcgis.com/UWYHeuuJISiGmgXx/ArcGIS/rest/services/Part1_Crime_Beta/FeatureServer/0')
#
# # Or get all features in one list
# all_features = list(d)

with open("Crime.json",'r') as f:
    data = json.load(f)
    subdata = data['features'][:1000]

with open("Part_of_crimes.json",'w') as f:
    for rec in subdata:
        jsstr = json.dumps(rec,ensure_ascii=False)
        f.write(jsstr+"\n")