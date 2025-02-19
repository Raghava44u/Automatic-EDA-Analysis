import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(df):
    numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
    fig, ax = plt.subplots(figsize=(12, 6))
    numeric_df.hist(ax=ax, bins=30)
    return fig

def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    return fig

def plot_countplots(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    figs = []
    for col in categorical_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.countplot(data=df, x=col, ax=ax)
        ax.set_title(f"Count Plot of {col}")
        figs.append(fig)
    return figs

def plot_boxplots(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    figs = []
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(data=df, x=col, ax=ax)
        ax.set_title(f"Box Plot of {col}")
        figs.append(fig)
    return figs

def plot_violinplots(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    figs = []
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.violinplot(data=df, x=col, ax=ax)
        ax.set_title(f"Violin Plot of {col}")
        figs.append(fig)
    return figs

def plot_pairplot(df):
    numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
    fig = sns.pairplot(numeric_df)
    return fig

def plot_kde(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    figs = []
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.kdeplot(df[col], ax=ax, fill=True)
        ax.set_title(f"KDE Plot of {col}")
        figs.append(fig)
    return figs
