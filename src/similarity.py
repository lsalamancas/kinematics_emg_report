from math import sqrt
from kin_emg_plot import planes

import pandas as pd
import statsmodels.api as sm


def find_cmc(data1, data2, data3, joint):

    df = pd.DataFrame([data1[joint],  data2[joint],  data3[joint]]).transpose()
    df.columns =  ['X1', 'X2', 'X3']
    cmc_v = []
    for run in range(df.shape[1]):
        if run == 2:
            X, y = df[df.columns[run]], df[df.columns[run - 2]]
        else:
            X, y = df[df.columns[run]], df[df.columns[run + 1]] 
        X1 = sm.add_constant(X)
        model = sm.OLS(y, X1).fit()
        rsa = model.rsquared_adj
        cmc_v.append(sqrt(abs(rsa))) 
    # print(cmc_v, cmc_avg)
    cmc_v = [round(cmc_v[_], 3) for _ in range(len(cmc_v))]
    return cmc_v


def cmc(df1, df2, df3, runs): 
    cmc_total = []
    cmc_avg_total = []
    index = []
    planes_dict = planes()
    planes_v = planes_dict['sagittal'] + planes_dict['frontal'] + planes_dict['transverse']   
    joints = ['ac' + joint for joints in planes_v for joint in joints]

    for joint in joints:
        cmc_v = find_cmc(df1, df2, df3, joint)
        cmc_avg = round(sum(cmc_v) / len(cmc_v), 3)
        cmc_total.append(cmc_v)
        cmc_avg_total.append(cmc_avg)
        index.append(joint)

    planes_titles =  planes_dict['sagittal_titles'] + planes_dict['frontal_titles'] + planes_dict['transverse_titles']
    index_2d = [[title + ' Derecha', title + ' Izquierda'] for title in planes_titles]
    index = [title for titles in index_2d for title in titles]      #flatten vector
    columns = [f'{runs[0]}-{runs[1]}', f'{runs[1]}-{runs[2]}', f'{runs[0]}-{runs[2]}']

    df = pd.DataFrame(cmc_total, columns=columns, index=index)
    df2 = pd.DataFrame(cmc_avg_total, columns=['Total'], index=index)
    df2save = pd.concat([df, df2], axis=1)

    return df2save