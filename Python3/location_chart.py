"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Location - Top 10 Type
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
    creat_list(df_1, df_2, df_3, df_4)

def creat_list(df_1, df_2, df_3, df_4):
    """ Creat List of type """
    # data_top_10_form_ov_amount_type.py
    list_type = ['THEFT', 'BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'OTHER OFFENSE', 'ASSAULT', 'BURGLARY', 'MOTOR VEHICLE THEFT', 'ROBBERY', 'DECEPTIVE PRACTICE']
    list_num = [1640506, 1442716, 923000, 885431, 491922, 481661, 470958, 370548, 300453, 280931]
    
    location_dict = {}
    # location_2001to2004
    for i in df_1:
        index = 0 * (i[1] == list_type[0]) + 1 * (i[1] == list_type[1]) + 2 * (i[1] == list_type[2]) + 3 * (i[1] == list_type[3]) + 4 * (i[1] == list_type[4]) +\
        5 * (i[1] == list_type[5]) + 6 * (i[1] == list_type[6]) + 7 * (i[1] == list_type[7]) + 8 * (i[1] == list_type[8]) + 9 * (i[1] == list_type[9])
        if i[3] not in location_dict:
            location_dict[i[3]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            location_dict[i[3]][index] += 1
        else:
            location_dict[i[3]][index] += 1

    # location_2005to2007
    for i in df_2:
        index = 0 * (i[1] == list_type[0]) + 1 * (i[1] == list_type[1]) + 2 * (i[1] == list_type[2]) + 3 * (i[1] == list_type[3]) + 4 * (i[1] == list_type[4]) +\
        5 * (i[1] == list_type[5]) + 6 * (i[1] == list_type[6]) + 7 * (i[1] == list_type[7]) + 8 * (i[1] == list_type[8]) + 9 * (i[1] == list_type[9])
        if i[3] not in location_dict:
            location_dict[i[3]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            location_dict[i[3]][index] += 1
        else:
            location_dict[i[3]][index] += 1

    # location_2008to2011
    for i in df_3:
        index = 0 * (i[1] == list_type[0]) + 1 * (i[1] == list_type[1]) + 2 * (i[1] == list_type[2]) + 3 * (i[1] == list_type[3]) + 4 * (i[1] == list_type[4]) +\
        5 * (i[1] == list_type[5]) + 6 * (i[1] == list_type[6]) + 7 * (i[1] == list_type[7]) + 8 * (i[1] == list_type[8]) + 9 * (i[1] == list_type[9])
        if i[3] not in location_dict:
            location_dict[i[3]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            location_dict[i[3]][index] += 1
        else:
            location_dict[i[3]][index] += 1
    # location_2012to2017
    for i in df_4:
        index = 0 * (i[1] == list_type[0]) + 1 * (i[1] == list_type[1]) + 2 * (i[1] == list_type[2]) + 3 * (i[1] == list_type[3]) + 4 * (i[1] == list_type[4]) +\
        5 * (i[1] == list_type[5]) + 6 * (i[1] == list_type[6]) + 7 * (i[1] == list_type[7]) + 8 * (i[1] == list_type[8]) + 9 * (i[1] == list_type[9])
        if i[3] not in location_dict:
            location_dict[i[3]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            location_dict[i[3]][index] += 1
        else:
            location_dict[i[3]][index] += 1
    
    # Creat_chart
    creat_chart(list_type, list_num, location_dict)

def creat_chart(list_type, list_num, location_dict):
    """ Creat Chart """
    chart = pygal.StackedBar()
    chart.x_labels = map(str, list_type)
    chart.title = 'Location'
    chart.x_title = 'Type'
    chart.y_title = 'Number of events'
    # format_data
    count = 0
    for i in location_dict:
        if count == 20:
            break
        count += 1
        chart.add(i, [{'value': location_dict[i][j], 'label': '{:.2f}%'.format(100*location_dict[i][j]/list_num[j])} for j in range(10)])
    # render_to_time_chart.svg
    chart.legend_at_bottom = True
    chart.render_to_file('location_chart.svg')
main()
