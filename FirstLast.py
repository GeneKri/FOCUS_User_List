import pandas as pd
from tkinter import Tk, filedialog

def split_user_column_fillna(input_csv: str, output_csv: str) -> pd.DataFrame:
    """
    Split the "User" column into "First" and "Last" columns in a CSV file,
    filling in blanks where necessary.

    Args:
        input_csv (str): The path to the input CSV file.
        output_csv (str): The path to save the output CSV file.

    Returns:
        pd.DataFrame: The DataFrame with "First" and "Last" columns added.
    """
    try:
        # Read the input CSV file into a DataFrame
        df = pd.read_csv(input_csv)

        # Split the "User" column into "First" and "Last"
        split_names = df['User'].str.split(', ', expand=True)
        
        # Fill in blanks in "First" and "Last" columns where necessary
        df['First'] = df['First'].fillna(split_names[1])
        df['Last'] = df['Last'].fillna(split_names[0])

        # Save the updated DataFrame to the output CSV file
        df.to_csv(output_csv, index=False)

        # Return the updated DataFrame
        return df

    except pd.errors.EmptyDataError as ede:
        # Handle the case where the CSV file is empty
        print(f"Error: {ede}")
        return pd.DataFrame()

    except pd.errors.ParserError as pe:
        # Handle the case where there is an issue parsing the CSV
        print(f"Error: {pe}")
        return pd.DataFrame()

# Example usage:

if __name__ == "__main__":
    # Use Tkinter filedialog to select input and output files
    root = Tk()
    root.wm_attributes('-topmost', True)
    root.withdraw()

    # Select the input CSV file (FOCUS Users)
    file_path1 = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select FOCUS Users CSV file")

    # Select the output CSV file to save the merged data
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Merged CSV As")

    # Perform the split and fill operation, and save the result
    result_df = split_user_column_fillna(file_path1, save_path)

    # Output the updated DataFrame
    print(result_df)