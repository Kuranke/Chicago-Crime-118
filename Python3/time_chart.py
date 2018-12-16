"""
Chicago-Crime-118 (PSIT Data Analysis Project)
Time Chart
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
    new_dict = {}  # Arrage-Non-type
    time_lst = []
    # type_2001to2004
    for i in df_1:
        if i[1] not in type_dict:
            type_dict[i[1]] = [1, 0, 0, 0, 0]
        else:
            type_dict[i[1]][0] += 1
        # count_time
        time = i[0].split()             # xx/xx/xx 00:00:00 XX
        digit = time[1].split(':')      # split 00:00:00
        digit = [int(i) for i in digit]
        ampm = time[2]
        index = 1 * (6 <= digit[0] <= 11 and ampm == 'AM') + 2 * ((1 <= digit[0] <= 4 or digit[0] == 12) and ampm == 'PM') +\
        3 * (5 <= digit[0] <= 9 and ampm == 'PM') +  4 * ((10 <= digit[0] <= 11 and ampm == 'PM') or ((1 <= digit[0] <= 5 or digit[0] == 12) and ampm == 'AM'))
        type_dict[i[1]][index] += 1

    # type_2005to2007
    for i in df_2:
        if i[1] not in type_dict:
            type_dict[i[1]] = [1, 0, 0, 0, 0]
        else:
            type_dict[i[1]][0] += 1
        # count_time
        time = i[0].split()             # xx/xx/xx 00:00:00 XX
        digit = time[1].split(':')      # split 00:00:00
        digit = [int(i) for i in digit]
        ampm = time[2]
        index = 1 * (6 <= digit[0] <= 11 and ampm == 'AM') + 2 * ((1 <= digit[0] <= 4 or digit[0] == 12) and ampm == 'PM') +\
        3 * (5 <= digit[0] <= 9 and ampm == 'PM') +  4 * ((10 <= digit[0] <= 11 and ampm == 'PM') or ((1 <= digit[0] <= 5 or digit[0] == 12) and ampm == 'AM'))
        type_dict[i[1]][index] += 1


    # type_2008to2011
    for i in df_3:
        if i[1] not in type_dict:
            type_dict[i[1]] = [1, 0, 0, 0, 0]
        else:
            type_dict[i[1]][0] += 1
        # count_time
        time = i[0].split()             # xx/xx/xx 00:00:00 XX
        digit = time[1].split(':')      # split 00:00:00
        digit = [int(i) for i in digit]
        ampm = time[2]
        index = 1 * (6 <= digit[0] <= 11 and ampm == 'AM') + 2 * ((1 <= digit[0] <= 4 or digit[0] == 12) and ampm == 'PM') +\
        3 * (5 <= digit[0] <= 9 and ampm == 'PM') +  4 * ((10 <= digit[0] <= 11 and ampm == 'PM') or ((1 <= digit[0] <= 5 or digit[0] == 12) and ampm == 'AM'))
        type_dict[i[1]][index] += 1


    # type_2012to2017
    for i in df_4:
        if i[1] not in type_dict:
            type_dict[i[1]] = [1, 0, 0, 0, 0]
        else:
            type_dict[i[1]][0] += 1
        # count_time
        time = i[0].split()             # xx/xx/xx 00:00:00 XX
        digit = time[1].split(':')      # split 00:00:00
        digit = [int(i) for i in digit]
        ampm = time[2]
        index = 1 * (6 <= digit[0] <= 11 and ampm == 'AM') + 2 * ((1 <= digit[0] <= 4 or digit[0] == 12) and ampm == 'PM') +\
        3 * (5 <= digit[0] <= 9 and ampm == 'PM') +  4 * ((10 <= digit[0] <= 11 and ampm == 'PM') or ((1 <= digit[0] <= 5 or digit[0] == 12) and ampm == 'AM'))
        type_dict[i[1]][index] += 1

    # arrange_non-type_in_same_key
    new_dict['NON-TYPE'] = [0, 0, 0, 0, 0]
    for i in type_dict:
        if 'NON' in i:
            new_dict['NON-TYPE'][0] += type_dict[i][0]
            new_dict['NON-TYPE'][1] += type_dict[i][1]
            new_dict['NON-TYPE'][2] += type_dict[i][2]
            new_dict['NON-TYPE'][3] += type_dict[i][3]
            new_dict['NON-TYPE'][4] += type_dict[i][4]
        else:
            new_dict[i] = type_dict[i]
    # sort_value
    new_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    creat_chart(new_dict)

def creat_chart(new_dict):
    """ Creat Chart """
    # creat_chart
    chart = pygal.StackedBar()
    mor, noon, even, night = [], [], [], []
    chart.x_labels = map(lambda x: x, [new_dict[i][0] for i in range(10)])
    chart.title = 'Duration'
    chart.x_title = 'Type'
    chart.y_title = 'Number of events'
    for i in range(10):
        mor.append({'value': new_dict[i][1][1], 'label': '{:.2f}%'.format(100*new_dict[i][1][1]/new_dict[i][1][0])})
        noon.append({'value': new_dict[i][1][2], 'label': '{:.2f}%'.format(100*new_dict[i][1][2]/new_dict[i][1][0])})
        even.append({'value': new_dict[i][1][3], 'label': '{:.2f}%'.format(100*new_dict[i][1][3]/new_dict[i][1][0])})
        night.append({'value': new_dict[i][1][4], 'label': '{:.2f}%'.format(100*new_dict[i][1][4]/new_dict[i][1][0])})
    chart.add('6AM - 11AM', mor)
    chart.add('12PM - 4PM', noon)
    chart.add('5PM - 9PM', even)
    chart.add('10PM - 11PM & 12AM - 5AM', night)
    # render_to_time_chart.svg
    chart.legend_at_bottom = True
    chart.render_to_file('time_chart.svg')
main()
