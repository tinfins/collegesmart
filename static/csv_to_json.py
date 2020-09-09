import pandas as pd

def csv_to_json(file_name):
    df = pd.DataFrame(pd.read_csv (file_name + '.csv', sep = ",", header = 0, index_col = False))
    df.to_json (file_name + '.json', orient="records")
    
csv_to_json('links')
