import os
import pandas as pd
from tkinter import Tk, filedialog

def FocusUserMerge() -> None:
    root = Tk()
    root.wm_attributes('-topmost', True)
    root.withdraw()

    # Select the first CSV file (FOCUS Users)
    file_path1 = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select FOCUS Users CSV file")
    # Select the second CSV file
    file_path2 = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select the second CSV file")

    try:
        df1 = pd.read_csv(file_path1)
        df2 = pd.read_csv(file_path2)
    except pd.errors.EmptyDataError:
        print("One or both of the selected CSV files is empty.")
        # Handle this case as per your requirement
    except pd.errors.ParserError:
        print("Error parsing one or both of the selected CSV files.")
        # Handle this case as per your requirement
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Define the merging criteria/columns
    merge_columns = ['User ID']

    try:
        merged_df = pd.merge(df1, df2, on=merge_columns, how='inner')
    except pd.errors.MergeError:
        print("Error merging DataFrames. Check if the specified columns exist in both files.")
        # Handle this case as per your requirement
    except Exception as e:
        print(f"An unexpected error occurred during merging: {e}")

    try:
        print(merged_df)
        # Prompt user to save the merged DataFrame as a new CSV file
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Merged CSV As")
        if save_path:
            merged_df.to_csv(save_path, index=False)
            print(f"The merged DataFrame has been successfully saved to {save_path}")
        else:
            print("No file selected. The merged DataFrame has not been saved.")
    except Exception as e:
        print(f"An error occurred while displaying/saving the merged DataFrame: {e}")
