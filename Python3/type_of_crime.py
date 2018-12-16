"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Type of crime each year
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
    type_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}] # list_type
    # type_2001to2004
    for i in df_1:
        # select_dict
        index = (0 * (i[6] == 2001)) + (1 * (i[6] == 2002)) + (2 * (i[6] == 2003)) + (3 * (i[6] == 2004)) 
        if i[1] not in type_dict[index] and 'NON' not in i[1]:
            type_dict[index][i[1]] = 1
        elif i[1] not in type_dict[index] and 'NON' in i[1]:
            type_dict[index]['NON-TYPE'] = 1
        else:
            type_dict[index][i[1]] += 1

    # type_2005to2007
    for i in df_2:
        index = (4 * (i[6] == 2005)) + (5 * (i[6] == 2006)) + (6 * (i[6] == 2007))
        if i[1] not in type_dict[index] and 'NON' not in i[1]:
            type_dict[index][i[1]] = 1
        elif i[1] not in type_dict[index] and 'NON' in i[1]:
            type_dict[index]['NON-TYPE'] = 1
        else:
            type_dict[index][i[1]] += 1

    # type_2008to2011
    for i in df_3:
        index = (7 * (i[6] == 2008)) + (8 * (i[6] == 2009)) + (9 * (i[6] == 2010)) + (10 * (i[6] == 2011))
        if i[1] not in type_dict[index] and 'NON' not in i[1]:
            type_dict[index][i[1]] = 1
        elif i[1] not in type_dict[index] and 'NON' in i[1]:
            type_dict[index]['NON-TYPE'] = 1
        else:
            type_dict[index][i[1]] += 1

    # type_2012to2017
    for i in df_4:
        index = (11 * (i[6] == 2012)) + (12 * (i[6] == 2013)) + (13 * (i[6] == 2014)) + (14 * (i[6] == 2015)) + (15 * (i[6] == 2016)) + (16 * (i[6] == 2017))
        if i[1] not in type_dict[index] and 'NON' not in i[1]:
            type_dict[index][i[1]] = 1
        elif i[1] not in type_dict[index] and 'NON' in i[1]:
            type_dict[index]['NON-TYPE'] = 1
        else:
            type_dict[index][i[1]] += 1

    for i in range(17):
        type_dict[i] = sorted(type_dict[i].items(), key=lambda x: x[1], reverse=True)
    creat_chart(type_dict)

def creat_chart(type_dict):
    """ Creat Chart """
    # data_amount_crime_each_years_from_ov_amount_crime.py
    data_year = [568518, 490879, 475913, 388205, 455811, 794684, 621848, 852053, 783900, 700691, 352066, 335670, 306703, 274527, 262995, 265462, 11357]
    keep = {}
    for i in range(17):
        for j in range(10):
            if type_dict[i][j][0] not in keep:
                keep[type_dict[i][j][0]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                keep[type_dict[i][j][0]][i] = type_dict[i][j][1]
            else:
                keep[type_dict[i][j][0]][i] += type_dict[i][j][1]
    # creat_chart
    chart = pygal.StackedBar()
    chart.x_labels = map(str, range(2001, 2018)) 
    chart.x_title = 'Year'
    chart.y_title = 'Number of events'
    for i in keep:
        chart.add(i, [{'value': keep[i][yr], 'label': '{:.2f}%'.format(100*keep[i][yr]/data_year[yr])} for yr in range(17)])
    # render_to_type_chart.svg
    chart.legend_at_bottom = True
    chart.render_to_file('type_chart.svg')
main()
