import yaml
from yaml.loader import SafeLoader
from bs4 import BeautifulSoup
import pandas as pd
import os

with open('config.yaml', encoding='utf8') as yaml_file:
        config = yaml.load(yaml_file, Loader=SafeLoader)

        # Headers for excel file 
        
        kinematics_headers = config['Headers']['Kinematics']

for file in os.listdir(os.getcwd()): 
    if file.endswith('.mdx') and int(file[-5]) == 4:
        file2read = file
print(file2read)
def read_mdx(filename: str, keys: list, data2read: str) -> pd.DataFrame:
    with open(filename, "r") as mdx:
        # Read each line in the file, readlines() returns a list of lines
        content = mdx.readlines()
        # Combine the lines in the list into a string
        content = "".join(content)
        bs_content = BeautifulSoup(content, features= "xml")

    values_dict = {}
    data = []
    for joint in keys:
        try:
            data = bs_content.find(data2read, label=joint)['data'].split('S ')[1:]
            print(data)
            values_dict[joint] = [int(value)/10 if value != '' else 0 for value in data ]
        except:
            print('hola')
    
    return pd.DataFrame(values_dict)

with open('6538~aa~Walking 01.mdx', "r") as mdx:
    # Read each line in the file, readlines() returns a list of lines
    content = mdx.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = BeautifulSoup(content, features= "xml")
angles = read_mdx(file2read, list(kinematics_headers.keys()), 'angle')
print(bs_content.find('event', label='eRHS')['data'].split('I ')[1:])

print(angles)

