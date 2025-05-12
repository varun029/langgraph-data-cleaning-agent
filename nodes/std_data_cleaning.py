import pandas as pd

def miss_val_column(df):
    return df.columns[df.isnull().any()].tolist()

def miss_val_percentage(df, missing_cols):
    return {col: df[col].isnull().mean() * 100 for col in missing_cols}

def exact_duplicate_rows(df):
    return df[df.duplicated()]

def num_exact_duplicates(df):
    return df.duplicated().sum()

def drop_unnecessary_columns(df, columns_to_keep):
    return df[columns_to_keep].copy()

def data_cleaning(state):
    fd_df = state["fd_df"]
    dt_df = state["dt_df"]

    # Missing values
    print("Missing values in FD data:")
    fd_missing = miss_val_column(fd_df)
    print(miss_val_percentage(fd_df, fd_missing))

    print("Missing values in DT data:")
    dt_missing = miss_val_column(dt_df)
    print(miss_val_percentage(dt_df, dt_missing))

    # Exact Duplicates
    print("Exact duplicate rows in FD data:", num_exact_duplicates(fd_df))
    print("Exact duplicate rows in DT data:", num_exact_duplicates(dt_df))

    # Drop unnecessary columns
    fd_columns_to_keep = ['SKU_ID', 'SKU_NAME', 'CLASS_ID', 'CLASS_NAME', 'SUBCLASS_ID', 'SUBCLASS_NAME']
    dt_columns_to_keep = ['SKU Id', 'SKU Description', 'Class ID', 'Class Description', 'Sub Class Id', 'Sub Class Description']

    fd_df_cleaned = drop_unnecessary_columns(fd_df, fd_columns_to_keep)
    dt_df_cleaned = drop_unnecessary_columns(dt_df, dt_columns_to_keep)

    return {
        "fd_df": fd_df_cleaned,
        "dt_df": dt_df_cleaned,
        "messages": state["messages"],
    }