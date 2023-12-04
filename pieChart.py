from matplotlib import pyplot as plt
from dataCleaning import data_cleaning

def custom_autopct(pct):
    return '{:.1f}%'.format(pct) if pct > 1 else ''

def piechart(properties_count_dic, data, race_count_list):
    # Race-Description
    des_wea_rdic = {}
    res_objects = ['Race', 'Description']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        race_name = data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])
        des_wea_rdic[race_name][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic)

    del des_wea_rdic["AMERICAN_INDIAN_OR_ALASKA_NATIVE"]
    del des_wea_rdic["ASIAN"]
    del des_wea_rdic["NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER"]


    plt.figure(figsize=(18, 8))
    for i, (race, crimes) in enumerate(des_wea_rdic.items(), start=1):
        plt.subplot(1, 3, i)
        labels = crimes.keys()
        sizes = crimes.values()

        explode = [0.04] * len(crimes)

        patches, texts, autotexts = plt.pie(sizes, explode=explode, autopct=custom_autopct, startangle=240,
                                            pctdistance=0.65,labeldistance=1.1)
        for autotext in autotexts:
            autotext.set_fontsize(14)

        centre_circle = plt.Circle((0, 0), 0.20, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.text(0, 1.2, race, horizontalalignment='center', verticalalignment='center', fontsize=15)


        plt.text(0, -1.2, f"Overall ratio: {race_count_list[i - 1]}%",fontsize=14, horizontalalignment='center', verticalalignment='center',
                 bbox=dict(facecolor='white', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.5'))

        plt.axis('equal')

    fig = plt.gcf()
    fig.legend(patches, labels, loc='center right',fontsize=12, bbox_to_anchor=(1.0, 0.5))

    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()