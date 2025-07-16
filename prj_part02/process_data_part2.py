import os
import duckdb
import pandas as pd

def get_project_root() -> str:
    """Returns the absolute path to the project root."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def main():
    """
    Main function to perform data analysis for Part 2.
    """
    project_root = get_project_root()
    processed_csv_path = os.path.join(project_root, 'prj_files', 'fakeTelegram.BR_2022_processed.csv')
    parquet_path = os.path.join(project_root, 'prj_files', 'data.parquet')
    duckdb_path = os.path.join(project_root, 'prj_files', 'telegram.duckdb')

    # --- Step 1: Load the processed data from Part 1 ---
    if not os.path.exists(processed_csv_path):
        print(f"Processed data file not found at {processed_csv_path}")
        print("Please run the Part 1 processing script first.")
        # Optionally, run the part 1 script here
        # from prj_part01.process_data import main as process_part1
        # print("Running Part 1 processing...")
        # process_part1()
        return
    
    df = pd.read_csv(processed_csv_path)
    print("Successfully loaded processed data from Part 1.")

    # --- Step 2: Export to Parquet ---
    df.to_parquet(parquet_path, index=False)
    print(f"Data exported to Parquet format at {parquet_path}")

    # --- Step 3: Export to DuckDB ---
    con = duckdb.connect(duckdb_path)
    # Create a table and insert the data
    con.execute("CREATE OR REPLACE TABLE telegram_data AS SELECT * FROM df")
    print(f"Data exported to DuckDB at {duckdb_path}")

    # --- Step 4: Perform Queries using DuckDB ---
    print("\n--- Starting DuckDB Queries ---")

    # 1. A quantidade de mensagens;
    total_messages = con.execute("SELECT COUNT(*) FROM telegram_data").fetchone()[0]
    print(f"1. Total messages: {total_messages}")

    # 2. A quantidade de usuários;
    total_users = con.execute("SELECT COUNT(DISTINCT id_member_anonymous) FROM telegram_data").fetchone()[0]
    print(f"2. Total unique users: {total_users}")

    # 3. A quantidade de grupos;
    total_groups = con.execute("SELECT COUNT(DISTINCT id_group_anonymous) FROM telegram_data").fetchone()[0]
    print(f"3. Total unique groups: {total_groups}")

    # 4. Quantidade de mensagens que possuem apenas texto;
    text_only_messages = con.execute("SELECT COUNT(*) FROM telegram_data WHERE has_media = FALSE").fetchone()[0]
    print(f"4. Text-only messages: {text_only_messages}")

    # 5. Quantidade de mensagens contendo mídias;
    media_messages = con.execute("SELECT COUNT(*) FROM telegram_data WHERE has_media = TRUE").fetchone()[0]
    print(f"5. Messages with media: {media_messages}")

    # Close the connection
    con.close()

    print("\n--- DuckDB Queries Complete ---")


if __name__ == '__main__':
    main()
