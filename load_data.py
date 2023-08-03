def load_data():
    # Importing the packages necessary
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    import itertools
    import matplotlib.colors as mcolors
    from pyvis.network import Network  
    # Import dataset from .csv file
    df = pd.read_csv('network_data.csv')
    df['Source'] = df['Source'].astype(str)
    df['Destination'] = df['Destination'].astype(str)
    # aggregate data for 2022
    df_agg = \
        df.groupby(['Source','Destination','Platform']).agg(
        total_vol = ('Volume', 'sum'),
        total_val  = ('Value', 'sum'),
        total_fees = ('Revenues','sum')\
        ).reset_index().sort_values(by = 'total_vol',ascending = False)
    # return the two objects
    return df, df_agg
