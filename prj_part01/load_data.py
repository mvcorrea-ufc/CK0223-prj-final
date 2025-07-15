import pandas as pd
import os
from prj_part01.download_data import download_and_extract_data

def load_dataset():
    """
    Ensures the dataset is downloaded and then loads it from the prj_files directory.

    Returns:
        pandas.DataFrame: The loaded dataframe.
    """
    # Ensure the data is present
    download_and_extract_data()

    # Get the absolute path to the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    file_path = os.path.join(project_root, 'prj_files', 'fakeTelegram.BR_2022.csv')
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at {file_path}. The download may have failed.")
        
    df = pd.read_csv(file_path)
    return df

if __name__ == '__main__':
    df = load_dataset()
    print("Dataset loaded successfully!")
    print(df.head())
