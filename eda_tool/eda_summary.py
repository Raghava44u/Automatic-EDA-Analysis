def dataset_summary(df):
    summary = {
        "Shape": df.shape,
        "Columns": list(df.columns),
        "Missing Values": df.isnull().sum().to_dict(),
        "Data Types": df.dtypes.to_dict(),
        "Summary Statistics": df.describe().to_dict()
    }
    return summary
