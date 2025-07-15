# Project Part 1: Data Processing and Feature Engineering

This directory contains the scripts for the first part of the data mining project, which corresponds to the tasks outlined in "Lista 1". The focus is on data ingestion, cleaning, and the creation of new features from the raw dataset.

## Scripts

### `download_data.py`

-   **Purpose:** This script is responsible for downloading the project's dataset from a shared Google Drive link.
-   **Functionality:**
    -   It checks if the dataset already exists locally to avoid redundant downloads.
    -   If the data is not present, it downloads a `.zip` archive.
    -   It extracts the required `.csv` file from the archive into the `prj_files` directory.
    -   It cleans up by deleting the downloaded `.zip` file after extraction.
-   **Note:** This script is not meant to be run directly but is called by `load_data.py`.

### `load_data.py`

-   **Purpose:** Acts as a data loader module for the main processing script.
-   **Functionality:**
    -   It first calls the `download_and_extract_data()` function from `download_data.py` to ensure the dataset is available.
    -   It then loads the `fakeTelegram.BR_2022.csv` file into a pandas DataFrame.
-   **Usage:** This module is imported by `process_data.py`.

### `process_data.py`

-   **Purpose:** This is the main script for this project part. It executes all the data transformation and analysis tasks required by the assignment.
-   **Functionality:**
    -   Loads the data using the `load_data` module.
    -   Performs data quality checks, including identifying missing values, duplicates, and data type inconsistencies.
    -   Creates several new features (`caracteres`, `words`, `sharings`, `viral`, `sentiment`).
    -   Filters out irrelevant data based on specific criteria (e.g., "trava-zaps").
    -   Saves the final, processed DataFrame to `prj_files/fakeTelegram.BR_2022_processed.csv`.

---

For full setup and execution instructions, please refer to the main `README.md` file in the project's root directory.
