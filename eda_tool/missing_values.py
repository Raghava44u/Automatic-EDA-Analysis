import missingno as msno
import matplotlib.pyplot as plt

def plot_missing_values(df):
    """Plots missing values heatmap."""
    fig, ax = plt.subplots()
    msno.heatmap(df, ax=ax)
    return fig
