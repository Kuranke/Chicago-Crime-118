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
    # list_[0]=True,[1]=False
    num_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    # 2001to2004
    for i in df_1:
        index = (0 * (i[6] == 2001)) + (1 * (i[6] == 2002)) + (2 * (i[6] == 2003)) + (3 * (i[6] == 2004)) 
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    # 2005to2007
    for i in df_2:
        index = (4 * (i[6] == 2005)) + (5 * (i[6] == 2006)) + (6 * (i[6] == 2007))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    # 2008to2011
    for i in df_3:
        index = (7 * (i[6] == 2008)) + (8 * (i[6] == 2009)) + (9 * (i[6] == 2010)) + (10 * (i[6] == 2011))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    # 2012to2017
    for i in df_4:
        index = (11 * (i[6] == 2012)) + (12 * (i[6] == 2013)) + (13 * (i[6] == 2014)) + (14 * (i[6] == 2015)) + (15 * (i[6] == 2016)) + (16 * (i[6] == 2017))
        if i[4]:
            num_list[index][0] += 1
        else:
            num_list[index][1] += 1

    # data_amount_crime_each_years_from_ov_amount_crime.py
    data_year = [568518, 490879, 475913, 388205, 455811, 794684, 621848, 852053, 783900, 700691, 352066, 335670, 306703, 274527, 262995, 265462, 11357]
    # creat_bar_chart_style
    amount_chart = pygal.Bar()  # creat_chart
    amount_chart.x_labels = map(str, range(2001, 2018))
    amount_chart.x_title = 'Year'
    amount_chart.y_title = 'Amount'
    # format_data
    arrest_list = []
    fail_list = []
    for i in range(17):
        arrest_list.append({'value': num_list[i][0], 'label': '{:.2f}%'.format(100*num_list[i][0]/data_year[i])})
        fail_list.append({'value': num_list[i][1], 'label': '{:.2f}%'.format(100*num_list[i][1]/data_year[i])})
    amount_chart.add('Arrest', arrest_list)
    amount_chart.add('Fail', fail_list)

    # creat_every_yrs_arrest.svg
    arrest, fail = 0, 0
    for i in num_list:
        arrest += i[0]
        fail += i[1]
    chart = pygal.Pie()
    chart.add('Arrest', [{'value': arrest, 'label': '{:.2f}%'.format(100*arrest/sum(data_year))}])
    chart.add('Fail', [{'value': fail, 'label': '{:.2f}%'.format(100*fail/sum(data_year))}])

    # render_to_arrest.svg
    amount_chart.render_to_file('arrest_chart.svg')
    chart.render_to_file('every_yrs_arrest.svg')
main()
