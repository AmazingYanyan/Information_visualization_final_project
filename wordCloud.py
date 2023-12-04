import math
from dataCleaning import data_cleaning
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from matplotlib import pyplot as plt
def add_cloud_text(des_wea_rdic, cloud_string_list, properties_count_dic, necessary_prop = 'Description'):
    for description in properties_count_dic[necessary_prop]:
        if description not in cloud_string_list.keys():
            cloud_string_list[description] = ''
        # count total number
        total_number=0
        for i, item in enumerate(des_wea_rdic[description]):
            total_number += des_wea_rdic[description][item]

        # add text based on word ratio
        for i, item in enumerate(des_wea_rdic[description]):
            for j in range(math.ceil(des_wea_rdic[description][item]/total_number*500)):
                cloud_string_list[description] += item
                cloud_string_list[description] += ', '

    return cloud_string_list

def wordcloudfun(properties_count_dic, data):
    # initial relationship dictionaries
    des_wea_rdic = {}
    res_objects = ['Description', 'Race']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0

    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1

    print(des_wea_rdic)

    # update 'UNKNOWN'
    def update_keys_race(d):
        new_d = {}
        for key, value in d.items():
            if key == 'UNKNOWN':
                new_key = 'Race_UNKNOWN'
            else:
                new_key = key
            new_d[new_key] = value
        return new_d

    # 遍历数据并应用更新函数
    des_wea_rdic = {k: update_keys_race(v) for k, v in des_wea_rdic.items()}

    # word cloud
    cloud_string_list = {}
    cloud_string_list = add_cloud_text(des_wea_rdic, cloud_string_list, properties_count_dic)

    # 2
    des_wea_rdic = {}
    res_objects = ['Description', 'Age']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic)

    temp_dic = {}
    age_groups = ["Teenagers", "Young_Adults", "Early_Middle_Age", "Middle_Age", "Late_Middle_Age", "Early_Senior"]
    for pro_name_i in properties_count_dic[res_objects[0]]:
        temp_dic[pro_name_i] = {}
        for pro_name_j in age_groups:
            temp_dic[pro_name_i][pro_name_j] = 0
    for key1, value1 in des_wea_rdic.items():
        for key2 , value2 in des_wea_rdic[key1].items():
            if 16<= int(key2) <=19:
                temp_dic[key1]["Teenagers"]+=1
            elif 20<= int(key2) <=29:
                temp_dic[key1]["Young_Adults"]+=1
            elif 30<= int(key2) <=39:
                temp_dic[key1]["Early_Middle_Age"]+=1
            elif 40<= int(key2) <=49:
                temp_dic[key1]["Middle_Age"]+=1
            elif 50<= int(key2) <=59:
                temp_dic[key1]["Late_Middle_Age"]+=1
            elif 60<= int(key2) <=63:
                temp_dic[key1]["Early_Senior"]+=1

    cloud_string_list = add_cloud_text(temp_dic, cloud_string_list, properties_count_dic)

    # 3
    des_wea_rdic = {}
    res_objects = ['Description', 'Gender']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic)

    # update 'UNKNOWN'
    def update_keys_gender(d):
        new_d = {}
        for key, value in d.items():
            if key == 'M':
                new_key = 'male'
            elif key == 'F':
                new_key = 'female'
            elif key == 'U':
                new_key = 'gender_unknown'
            else:
                new_key = key
            new_d[new_key] = value
        return new_d

    des_wea_rdic = {k: update_keys_gender(v) for k, v in des_wea_rdic.items()}

    cloud_string_list = add_cloud_text(des_wea_rdic, cloud_string_list, properties_count_dic)

    # 4
    des_wea_rdic = {}
    res_objects = ['Description', 'Weapon']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic)

    # update 'UNKNOWN'
    def update_keys_weapon(d):
        new_d = {}
        for key, value in d.items():
            if key == 'UNKNOWN':
                new_key = 'weapon_UNKNOWN'
            else:
                new_key = key
            new_d[new_key] = value
        return new_d

    des_wea_rdic = {k: update_keys_weapon(v) for k, v in des_wea_rdic.items()}

    cloud_string_list = add_cloud_text(des_wea_rdic, cloud_string_list, properties_count_dic)

    # Generate a word cloud image
    print('\n')
    for item in properties_count_dic['Description']:
        print(item)
        print(cloud_string_list[item])
        print('\n')

    wordcloud = WordCloud(background_color="white").generate(cloud_string_list['ROBBERY'])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
