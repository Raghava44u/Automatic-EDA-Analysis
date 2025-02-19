import missingno as msno
import matplotlib.pyplot as plt

def plot_missing_values(df):
    fig, ax = plt.subplots()
    msno.heatmap(df, ax=ax)
    return fig
