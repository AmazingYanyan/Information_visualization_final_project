from matplotlib import pyplot as plt
from dataCleaning import data_cleaning


def agecrimes(properties_count_dic, data):
    # Age-Description
    des_wea_rdic_1 = {}
    res_objects = ['Age', 'Description']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic_1[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic_1[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic_1[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic_1)

    # Age-Gender
    des_wea_rdic_2 = {}
    res_objects = ['Age', 'Gender']
    for pro_name_i in properties_count_dic[res_objects[0]]:
        des_wea_rdic_2[pro_name_i] = {}
        for pro_name_j in properties_count_dic[res_objects[1]]:
            des_wea_rdic_2[pro_name_i][pro_name_j] = 0
    # work on relationship dictionaries
    for i in range(len(data)):
        des_wea_rdic_2[data_cleaning(res_objects[0], data[i]['properties'][res_objects[0]])][
            data_cleaning(res_objects[1], data[i]['properties'][res_objects[1]])] += 1
    print(des_wea_rdic_2)

    total_crimes_by_age = {age: sum(crimes.values()) for age, crimes in des_wea_rdic_1.items()}

    male_crimes_by_age = {age: gender['M'] for age, gender in des_wea_rdic_2.items()}
    female_crimes_by_age = {age: gender['F'] for age, gender in des_wea_rdic_2.items()}
    unknown_crimes_by_age = {age: gender['U'] for age, gender in des_wea_rdic_2.items()}

    ages = list(total_crimes_by_age.keys())
    ages = [age for age in ages if age >= 1]

    total_crimes = list(total_crimes_by_age.values())
    male_crimes = [male_crimes_by_age.get(age, 0) for age in ages]
    female_crimes = [female_crimes_by_age.get(age, 0) for age in ages]
    unknown_crimes = [unknown_crimes_by_age.get(age, 0) for age in ages]

    plt.figure(figsize=(10, 6))
    # print('\n', ages)
    plt.scatter(ages, male_crimes, color='blue', label='Male', alpha=0.5)
    plt.scatter(ages, female_crimes, color='red', label='Female', alpha=0.5)
    plt.scatter(ages, unknown_crimes, color='green', label='Unknown', alpha=0.5)

    # plot line
    plt.axhline(y=2000, color='gray', linestyle='--', linewidth=1)
    plt.vlines(x=16,ymin=0, ymax=2000, colors='grey', linestyles='dashed', linewidth=1)
    plt.vlines(x=63,ymin=0, ymax=2000, colors='grey', linestyles='dashed', linewidth=1)
    plt.vlines(x=27, ymin=0, ymax=max(female_crimes), colors='grey', linestyles='dashed', linewidth=1)

    # text
    total = sum(male_crimes)+sum(female_crimes)+sum(unknown_crimes)
    plt.text(60, 3000, "Male ratio: {}%".format(round(sum(male_crimes)/total*100),2), color='blue', verticalalignment='bottom',
             horizontalalignment='left')
    plt.text(38, 5800, "Female ratio: {}%".format(round(sum(female_crimes)/total*100),2), color='red', verticalalignment='bottom',
             horizontalalignment='left')
    plt.text(29, 770, "Unknown ratio: {}%".format(round(sum(unknown_crimes)/total*100),2), color='green', verticalalignment='bottom',
             horizontalalignment='left')

    # title and legend
    plt.title('Crime Count by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Crime Count')
    plt.ylim(bottom=0)
    plt.xticks([0, 10, 16, 20, 27, 30, 40, 50, 60, 63, 70, 80, 90, 100])
    plt.legend()

    plt.show()

    print("Age from 16 to 63")
    male_total=0
    male_count=0
    for age, item in zip(ages,male_crimes):
        male_total+=item
        if 16 <= age <= 63:
            male_count+=item
    print(round(male_count/male_total*100,2))


    female_total=0
    female_count=0
    for age, item in zip(ages,female_crimes):
        female_total+=item
        if 16 <= age <= 63:
            female_count+=item
    print(round(female_count / female_total * 100, 2))


    ###
    print("Age from 22 to 40")
    male_total = 0
    male_count = 0
    for age, item in zip(ages, male_crimes):
        male_total += item
        if 22 <= age <= 40:
            male_count += item
    print(round(male_count / male_total * 100, 2))

    female_total = 0
    female_count = 0
    for age, item in zip(ages, female_crimes):
        female_total += item
        if 22 <= age <= 40:
            female_count += item
    print(round(female_count / female_total * 100, 2))

    ###
    print("Age from 18 to 29")
    male_total = 0
    male_count = 0
    for age, item in zip(ages, male_crimes):
        male_total += item
        if 18 <= age <= 29:
            male_count += item
    print(round(male_count / male_total * 100, 2))

    female_total = 0
    female_count = 0
    for age, item in zip(ages, female_crimes):
        female_total += item
        if 18 <= age <= 29:
            female_count += item
    print(round(female_count / female_total * 100, 2))