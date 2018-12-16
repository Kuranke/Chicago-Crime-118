"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Overview Location - Type
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
    location_dict = {} # list_location_2001-2017
    # location_2001to2004
    for i in df_1:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    # location_2005to2007
    for i in df_2:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    # location_2008to2011
    for i in df_3:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1

    # location_2012to2017
    for i in df_4:
        if i[3] not in location_dict:
            location_dict[i[3]] = 1
        else:
            location_dict[i[3]] += 1
    # sort_value
    new_dict = sorted(location_dict.items(), key=lambda x: x[1], reverse=True)
    creat_chart(new_dict)

def creat_chart(new_dict):
    """ Creat Chart """
    count = 0      # sum_location
    for i in new_dict:
        count += i[1]
    # creat_bar_chart_style
    amount_chart = pygal.Pie()
    amount_chart.title = 'Overview Location'
    for i in range(10):
        amount_chart.add(new_dict[i][0], [{'value':new_dict[i][1], 'label': '{:.2f}%'.format(100*new_dict[i][1]/count)}])
    amount_chart.legend_at_bottom = True
    # render_to_ov_location.svg
    amount_chart.render_to_file('ov_location.svg')
main()
