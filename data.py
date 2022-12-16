import os
import pandas as pd


def read_data(age: int, path: str, run_selected: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    '''read_data This Function 

    Parameters
    ----------
    age :
        patient age
    path : 
        files path
    run_selected : 
        the run selected for individual report
        
    Returns
    -------
    tuple(pd.Dataframe*6)
        Returns all dataframes from the txt files.
    '''
    columns = [
        'Frame', 'Time', 'Recto Femoral Derecho', 'Semitendinoso Derecho', 'Tibial anterior Derecho', 'Gastronemio Derecho', 
        'Recto Femoral Izquierdo', 'Semitendinoso Izquierdo', 'Tibial anterior Izquierdo', 'Gastronemio Izquierdo'
    ]
    emg_data = pd.read_fwf(f'{path}{os.sep}emg.emt', skiprows=11, names=columns).drop(columns='Frame', axis=1)
    times = pd.read_fwf(f'{path}{os.sep}times.emt', skiprows=6)
    scalars = pd.read_fwf(f'{path}{os.sep}scalars.emt', skiprows=6)
    events = pd.read_fwf(f'{path}{os.sep}events.emt', skiprows=6).set_index('Item')
    kin_data = pd.read_fwf(f'{path}{os.sep}graficas{run_selected}.emt', skiprows=6).drop(['Cycle'], axis=1).set_index(['Sample'])
    if age < 18:
        dh = pd.read_excel('dh_normal.xlsx', sheet_name = 'DH_Children',  header = 7, index_col = 0).dropna()
        return times, scalars, events, kin_data, emg_data, dh
    dh = pd.read_excel('dh_normal.xlsx', sheet_name = 'DH_Adults',  header = 7, index_col = 0).dropna()
    return times, scalars, events, kin_data, emg_data, dh
