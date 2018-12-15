"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Arrest Chart
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
    chart(df_1, df_2, df_3, df_4)

def chart(df_1, df_2, df_3, df_4):
    """ Creat chart of arrest """

    num_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for i in df_1:
        index = (0 * (i[6] == 2001)) + (1 * (i[6] == 2002)) + (2 * (i[6] == 2003)) + (3 * (i[6] == 2004))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    for i in df_2:
        index = (4 * (i[6] == 2005)) + (5 * (i[6] == 2006)) + (6 * (i[6] == 2007))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    for i in df_3:
        index = (7 * (i[6] == 2008)) + (8 * (i[6] == 2009)) + (9 * (i[6] == 2010)) + (10 * (i[6] == 2011))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    for i in df_4:
        index = (11 * (i[6] == 2012)) + (12 * (i[6] == 2013)) + (13 * (i[6] == 2014)) + (14 * (i[6] == 2015)) + (15 * (i[6] == 2016)) + (16 * (i[6] == 2017))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1
main()
