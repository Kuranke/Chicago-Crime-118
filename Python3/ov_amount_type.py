"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Overview Crime
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
    type_dict = {} # list_amount_crime_2001-2017
    new_dict = {}
    # type_2001to2004
    for i in df_1:
        if i[1] not in type_dict:
            type_dict[i[1]] = 1
        else:
            type_dict[i[1]] += 1

    # type_2005to2007
    for i in df_2:
        if i[1] not in type_dict:
            type_dict[i[1]] = 1
        else:
            type_dict[i[1]] += 1

    # type_2008to2011
    for i in df_3:
        if i[1] not in type_dict:
            type_dict[i[1]] = 1
        else:
            type_dict[i[1]] += 1
    
    # type_2012to2017
    for i in df_4:
        if i[1] not in type_dict:
            type_dict[i[1]] = 1
        else:
            type_dict[i[1]] += 1

    # arrange_non-type_in_same_key
    new_dict['NON-TYPE'] = 0
    for i in type_dict:
        if 'NON' in i:
            new_dict['NON-TYPE'] += type_dict[i]
        else:
            new_dict[i] = type_dict[i]
    # sort_value
    new_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    creat_chart(new_dict)
def creat_chart(new_dict):
    """ Creat Chart """
    count = 0
    for i in new_dict:
        count += i[1]
    # creat_bar_chart_style
    amount_chart = pygal.Pie()  # creat_chart
    for i in new_dict:
        amount_chart.add(i[0], [{'value':i[1], 'label': '{:.2f}%'.format(100*i[1]/count)}])
    amount_chart.legend_at_bottom = True
    # render_to_ov_amount.svg
    amount_chart.render_to_file('ov_type.svg')

main()
