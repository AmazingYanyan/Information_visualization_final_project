def data_cleaning(pro_name, pro_value):
    if pro_name == "Weapon":
        if pro_value is None:
            pro_value = "UNKNOWN"
        elif pro_value == 'NA':
            pro_value = 'UNKNOWN'
    elif pro_name == "Gender":
        if pro_value not in ['M', 'F', 'U']:
            if pro_value == "Male":
                pro_value = 'M'
            elif pro_value == "Female":
                pro_value = "F"
            else:
                pro_value = 'U'
    elif pro_name == "Age":
        if pro_value is not None:
            pro_value = int(pro_value)
            if pro_value < 0 or pro_value > 100:
                pro_value = 0
        else:
            pro_value = 0
    elif pro_name == "Race":
        if pro_value is None:
            pro_value = "UNKNOWN"
    elif pro_name == "Ethnicity":
        if pro_value is None:
            pro_value = "UNKNOWN"
    elif pro_name == "Old_District":
        if pro_value is None:
            pro_value = 'N/A'
        elif pro_value == 'SD5':  # I can't determine what is SD5
            pro_value = 'SOUTHERN'
        elif pro_value == 'ND':
            pro_value = 'NORTHERN'
        elif pro_value == 'NWD':
            pro_value = 'NORTHWEST'
    elif pro_name == "New_District":
        if pro_value is None:
            pro_value = 'N/A'
    return pro_value