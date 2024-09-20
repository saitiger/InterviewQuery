import pandas as pd

def empty_neighborhoods(neighborhoods: pd.DataFrame, users: pd.DataFrame):
    merged_df = neighborhoods.merge(users,how = 'left',left_on='id',right_on='neighborhood_id')            

    filt = merged_df[merged_df['id_y'].isna()].rename(columns={'name_x':'name'})

    return filt['name']
