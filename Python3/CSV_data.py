"""
Chicago-Crime-118 (PSIT Data Analysis Project)
CSV Script
"""

import csv

    new_1, new_2, new_3, new_4 = [], [], [], []
    db_1 = np.array(pd.read_csv('Chicago_Crimes_2001_to_2004.csv', error_bad_lines=False, low_memory=False)).tolist()
    db_2 = np.array(pd.read_csv('Chicago_Crimes_2005_to_2007.csv', error_bad_lines=False, low_memory=False)).tolist()
    db_3 = np.array(pd.read_csv('Chicago_Crimes_2008_to_2011.csv', error_bad_lines=False, low_memory=False)).tolist()
    db_4 = np.array(pd.read_csv('Chicago_Crimes_2012_to_2017.csv', error_bad_lines=False, low_memory=False)).tolist()

    # file_Chicago_Crimes_2001_to_2004.csv
    for i in db_1:
        new_1.append([i[3], i[6], i[7], i[8], i[9], i[10], int(i[18])])
    df_1 = pd.DataFrame.from_records(new_1, columns=title)
    df_1.to_csv('2001to2004.csv', index=False)

    # file_Chicago_Crimes_2005_to_2007.csv
    for i in db_2:
        new_2.append([i[3], i[6], i[7], i[8], i[9], i[10], i[18]])
    df_2 = pd.DataFrame.from_records(new_2, columns=title)
    df_2.to_csv('2005to2007.csv', index=False)

    # file_Chicago_Crimes_2008_to_2011.csv
    for i in db_3:
        new_3.append([i[3], i[6], i[7], i[8], i[9], i[10], i[18]])
    df_3 = pd.DataFrame.from_records(new_3, columns=title)
    df_3.to_csv('2008to2011.csv', index=False)

    # file_Chicago_Crimes_2012_to_2017.csv
    for i in db_4:
        new_4.append([i[3], i[6], i[7], i[8], i[9], i[10], i[18]])
    df_4 = pd.DataFrame.from_records(new_4, columns=title)
    df_4.to_csv('2012to2017.csv', index=False)
main()
