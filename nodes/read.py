import pandas as pd

def read_excel_files(state):
    fd_path = state.get("fd_path", "datasets/Only_FD_Data 3.xlsx")
    dt_path = state.get("dt_path", "datasets/Only_DT_Data 3.xlsx")
    
    fd_df = pd.read_excel(fd_path)
    dt_df = pd.read_excel(dt_path)

    print("FD and DT datasets read successfully.")
    # --- Output ---
    print("FD DataFrame head and shape:")
    print(fd_df.head())
    print(fd_df.shape)
    print("\nDT DataFrame head and shape:")
    print(dt_df.head())
    print(dt_df.shape)
    return {"fd_df": fd_df, "dt_df": dt_df}
