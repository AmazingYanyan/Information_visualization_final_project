import json
import sys, time, argparse
import numpy as np
from matplotlib import pyplot as plt

from heatMap import heatmap
from dataCleaning import data_cleaning
from ageCrimes import agecrimes
from pieChart import  piechart
from wordCloud import wordcloudfun

import warnings

warnings.filterwarnings("ignore")


def get_args(argv):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-f', '--filename', required=False, default="./Mid/ESRI_OpenData.egisdata.Part1_Crime.json")
    # parser.add_argument('-w', '--window-size', required=False, default=1, type=int)
    # parser.add_argument('-t', '--timeout-interval', required=False,
    #                     default=1.0, type=float, help='timeout interval in seconds')
    return parser.parse_args()





def main(argv):
    args = get_args(argv)
    filename = args.filename
    n = 0  # n is total number of crimes
    # necessary_properties_names = ['Description','Weapon','Gender','Age','Race','Ethnicity','Location','Old_District','New_District','Neighborhood']
    necessary_properties_names = ['Description', 'Weapon', 'Gender', 'Age', 'Race', 'Ethnicity',
                                  'Old_District', 'New_District']
    geo_split_thr = 4
    # initial properties_count_dic
    properties_count_dic = {}
    for pro_name in necessary_properties_names:
        properties_count_dic[pro_name] = []

    # open json
    with open(filename, 'r') as file:
        data = json.load(file)['features']

    # count each necessary properties
    for i in range(len(data)):
        for pro_name in necessary_properties_names:
            pro_value = data[i]['properties'][pro_name]
            pro_value = data_cleaning(pro_name,pro_value)

            if pro_value not in properties_count_dic[pro_name]:
                properties_count_dic[pro_name].append(pro_value)

    # print properties_count_dic
    for pro_name in necessary_properties_names:
        print(pro_name)
        print(properties_count_dic[pro_name])
        print(len(properties_count_dic[pro_name]), '\n')



    # -------- Section: Work on Age, Gender, and Crimes counts
    agecrimes(properties_count_dic, data)

    filtered_data = []
    for i in range(len(data)):
        if 16 <= data_cleaning("Age", data[i]['properties']["Age"]) <= 63:
            filtered_data.append(data[i])
    data = filtered_data
    filtered_data = None



    # # -------- Section: work on pie chart
    # initial relationship dictionaries
    des_wea_rdic = {}
    res_objects = ['Race', 'Gender']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0

    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1

    # print(des_wea_rdic)

    temp_list = []
    race_count_list = []
    for name in des_wea_rdic.keys():
        j = 0
        for i in des_wea_rdic[name].values():
            j += i
        temp_list.append(j)
    for i, name in enumerate(des_wea_rdic.keys()):
        race_count_list.append(round(temp_list[i] / sum(temp_list) * 100, 2))
        print(name, ': ', temp_list[i], '(', race_count_list[i], '%)')
    piechart(properties_count_dic, data, race_count_list)


    # -------- Section: work on word cloud
    wordcloudfun(properties_count_dic, data)


    # -------- Section: work on GeoLocation
    properties_count_dic_geolocation = {}
    max_geo_count = 1
    for i in range(len(data)):
        if data[i]['properties']['Latitude'] == '0' or data[i]['properties']['Longitude'] == '0' or data[i]['properties']['Latitude'] is None or data[i]['properties']['Longitude'] is None:
            continue
        if not data[i]['properties']['Description'] == 'LARCENY':
            continue
        latitude = round(float(data[i]['properties']['Latitude']),geo_split_thr)
        longitude = round(float(data[i]['properties']['Longitude']),geo_split_thr)
        if not latitude in properties_count_dic_geolocation:
            properties_count_dic_geolocation[latitude] = {longitude:1}
        elif longitude not in properties_count_dic_geolocation[latitude]:
            properties_count_dic_geolocation[latitude][longitude]=1
        else:
            properties_count_dic_geolocation[latitude][longitude]+=1
            if properties_count_dic_geolocation[latitude][longitude]>max_geo_count:
                max_geo_count=properties_count_dic_geolocation[latitude][longitude]

    # integrate map data
    mapdata = []

    for latitude in properties_count_dic_geolocation.keys():
        for longitude in properties_count_dic_geolocation[latitude]:
            mapdata.append((latitude,longitude,properties_count_dic_geolocation[latitude][longitude]))

    heatmap(mapdata, max_geo_count)



if __name__ == "__main__":
    main(sys.argv[1:])
