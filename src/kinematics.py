import numpy as np

from data import read_data
from kin_emg_plot import plt_emg, plt_kin, plt_tables


def fix_order(e_hs):
    if (e_hs[0]>e_hs[1]).any():
        idxs = np.where(e_hs[0]>e_hs[1])[0]
        for idx in idxs:
            temp = e_hs[0][idx]
            e_hs[0][idx] = e_hs[1][idx]
            e_hs[1][idx] = temp
    return list(e_hs)


def rms(age, path, run):
    times, scalars, events, kinec_data, emg_data, dh_normal = read_data(age, path, run)
    scalars.iloc[:,:-2] *= 100
    events = events * 1000 + 7
    
    t_stance = times[['tmRSTANCE.M', 'tmLSTANCE.M']].values.tolist()[0]
    e_hs = fix_order(events[['eRHS', 'eLHS']].values.astype(int))             # this result in [[initial_right, initial_left][final_right, final_left]]
    # print(e_hs)
    toe_off = np.round(scalars[['sRSTANCE', 'sLSTANCE']].values.tolist()[0]).astype(int)
    plt_emg(emg_data, t_stance, e_hs) 
    for plane in ['sagittal', 'frontal', 'transverse']:
        plt_tables(kinec_data, plane, toe_off)
        plt_kin(kinec_data, dh_normal, plane, toe_off) 