import gdown
import zipfile
import os

def download_and_extract_data():
    """
    Downloads and extracts the dataset from Google Drive.
    """
    # --- Configuration ---
    file_id = '10BqWokUD2hvWkosiebduOc4xFqqrqKvx'
    
    # Get the absolute path to the project root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    output_dir = os.path.join(project_root, 'prj_files')
    zip_path = os.path.join(output_dir, 'dataset.zip')
    # Assuming the CSV file inside the zip has the same name as before
    expected_csv_path = os.path.join(output_dir, 'fakeTelegram.BR_2022.csv')

    # --- Ensure output directory exists ---
    os.makedirs(output_dir, exist_ok=True)

    # --- Check if data is already extracted ---
    if os.path.exists(expected_csv_path):
        print(f"Dataset already exists at {expected_csv_path}. Skipping download and extraction.")
        return

    # --- Download the file ---
    print(f"Downloading dataset to {zip_path}...")
    gdown.download(id=file_id, output=zip_path, quiet=False)
    print("Download complete.")

    # --- Extract the zip file ---
    print(f"Extracting {zip_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Assuming there's one CSV file in the zip, find and extract it.
        csv_files = [name for name in zip_ref.namelist() if name.endswith('.csv')]
        if not csv_files:
            raise Exception("No CSV file found in the downloaded zip archive.")
        
        # Extract the first CSV found
        zip_ref.extract(csv_files[0], path=output_dir)
        # Rename it to the expected name if it's different
        if csv_files[0] != os.path.basename(expected_csv_path):
             os.rename(os.path.join(output_dir, csv_files[0]), expected_csv_path)

        print(f"Successfully extracted to {expected_csv_path}")

    # --- Clean up the zip file ---
    os.remove(zip_path)
    print(f"Removed temporary file {zip_path}.")

if __name__ == '__main__':
    download_and_extract_data()
