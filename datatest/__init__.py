import os
import pandas

this_dir = os.path.join(os.path.dirname(__file__))

def get_buildings():
    return pandas.read_csv(os.path.join(this_dir, 'buildings.csv'))

