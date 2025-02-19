import pandas as pd

def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        return None
