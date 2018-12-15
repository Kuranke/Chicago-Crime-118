"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Overview Location
"""
import pandas as pd
import numpy as np
import pygal
def main():
    """ Main function """
    df_1 = np.array(pd.read_csv('2001to2004.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_2 = np.array(pd.read_csv('2005to2007.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_3 = np.array(pd.read_csv('2008to2011.csv', error_bad_lines=False, low_memory=False)).tolist()
    df_4 = np.array(pd.read_csv('2012to2017.csv', error_bad_lines=False, low_memory=False)).tolist()
    creat_dict(df_1, df_2, df_3, df_4)

def creat_dict(df_1, df_2, df_3, df_4):
    """ Creat List of type """
    location_dict = {}

    for i in df_1:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    for i in df_2:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    for i in df_3:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    for i in df_4:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1


main()
