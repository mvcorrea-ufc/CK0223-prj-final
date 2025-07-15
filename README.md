# 2025-01 Data Mining Project - Part 1

This project focuses on the initial steps of a data mining pipeline: data cleaning, preprocessing, and feature engineering. The tasks are based on the "Lista 1" assignment from the Introduction to Data Science course (CKP9011/CK0223).

## Project Structure

- `prj_files/`: Contains project-related files, including the original and processed datasets.
- `prj_part01/`: Contains the Python scripts developed for this part of the project. See the [README in this directory](./prj_part01/README.md) for detailed information about each script.
- `requirements.txt`: A list of Python dependencies for this project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## How to Run

1.  **Set up the environment:**
    It is recommended to use a virtual environment. This project uses `uv`.
    ```bash
    # Create the virtual environment
    python3 -m uv venv

    # Activate the environment
    source .venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

3.  **Run the processing script:**
    To execute the data processing pipeline, run the following command from the project root:
    ```bash
    python3 prj_part01/process_data.py
    ```
    The script will automatically download and extract the dataset if it's not found locally. It will then perform all the cleaning and feature engineering steps, print a summary of the operations, and save the processed data to `prj_files/fakeTelegram.BR_2022_processed.csv`.

## Tasks Completed (Lista 1)

- ✅ **(a)** Dataset downloaded and read.
- ✅ **(b, c, d)** Missing values identified and counted.
- ✅ **(e)** Duplicate rows identified.
- ✅ **(f)** Domain/type errors checked.
- ✅ **(g)** `caracteres` column created.
- ✅ **(h)** `words` column created.
- ✅ **(i)** `viral` column created.
- ✅ **(j)** `sharings` column created.
- ✅ **(k)** `sentiment` column created using a basic keyword approach.
- ✅ **(l)** Rows containing "trava-zaps" searched for and removed.
- ✅ **(m)** Inconsistencies between features identified.
- ✅ Processed DataFrame saved to a new CSV file.
