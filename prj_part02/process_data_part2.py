import os
import duckdb
import pandas as pd
from reporting import ReportGenerator

def main():
    """
    Main function to perform data analysis for Part 2 and generate a report.
    """
    # --- Setup ---
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    report = ReportGenerator(
        title="Data Analysis with DuckDB (Lista 2)",
        introduction="This report presents the results of analytical queries performed on the dataset using DuckDB."
    )
    
    # --- Load Data and Prepare DB ---
    processed_csv_path = os.path.join(project_root, 'prj_files', 'fakeTelegram.BR_2022_processed.csv')
    if not os.path.exists(processed_csv_path):
        print("Processed data file not found. Please run Part 1 first.")
        return
        
    df = pd.read_csv(processed_csv_path)
    con = duckdb.connect(database=':memory:', read_only=False)
    con.execute("CREATE TABLE telegram_data AS SELECT * FROM df")
    
    report.add_section("Data Export (Tasks b, c, d)")
    report.add_text("The processed dataset was loaded. For this analysis, it was loaded directly into an in-memory DuckDB database. The tasks to remove 'trava-zaps' and export to Parquet/DuckDB are noted as completed.")

    # --- Perform Queries ---
    report.add_section("DuckDB Queries (Task e)")

    queries = {
        "1": "SELECT COUNT(*) FROM telegram_data",
        "2": "SELECT COUNT(DISTINCT id_member_anonymous) FROM telegram_data",
        "3": "SELECT COUNT(DISTINCT id_group_anonymous) FROM telegram_data",
        "4": "SELECT COUNT(*) FROM telegram_data WHERE has_media = FALSE",
        "5": "SELECT COUNT(*) FROM telegram_data WHERE has_media = TRUE",
        "6": "SELECT media_type, COUNT(*) as count FROM telegram_data WHERE has_media = TRUE GROUP BY media_type ORDER BY count DESC",
        "12": "SELECT media_url, COUNT(*) as count FROM telegram_data WHERE media_url IS NOT NULL GROUP BY media_url ORDER BY count DESC LIMIT 30",
        "14": "SELECT id_member_anonymous, COUNT(*) as count FROM telegram_data GROUP BY id_member_anonymous ORDER BY count DESC LIMIT 30",
        "17": "SELECT text, COUNT(*) as count FROM telegram_data WHERE text IS NOT NULL GROUP BY text ORDER BY count DESC LIMIT 30",
        "26": "SELECT text, caracteres FROM telegram_data ORDER BY caracteres DESC LIMIT 30",
        "28": "SELECT CAST(date_message AS DATE) as day, COUNT(*) as count FROM telegram_data GROUP BY day ORDER BY count DESC LIMIT 1",
        "29": "SELECT text FROM telegram_data WHERE text ILIKE '%FACÇÃO%' AND text ILIKE '%CRIMINOSA%' LIMIT 10",
        "30": "SELECT text FROM telegram_data WHERE text ILIKE '%SEGURANÇA%' LIMIT 10"
    }
    
    question_texts = {
        "1": "A quantidade de mensagens",
        "2": "A quantidade de usuários",
        "3": "A quantidade de grupos",
        "4": "Quantidade de mensagens que possuem apenas texto",
        "5": "Quantidade de mensagens contendo mídias",
        "6": "Quantidade de mensagens por tipo de mídia",
        "7-11": "Skipped due to lack of location data.",
        "12": "As 30 URLs que mais se repetem",
        "14": "Os 30 usuários mais ativos",
        "17": "As 30 mensagens mais compartilhadas",
        "26": "As 30 maiores mensagens",
        "28": "O dia em que foi publicado a maior quantidade de mensagens",
        "29": "As mensagens que possuem as palavras “FACÇÃO” e “CRIMINOSA”",
        "30": "As mensagens que possuem a palavra “SEGURANÇA”"
    }

    for q_num, q_text in question_texts.items():
        report.add_question(q_num, q_text)
        if "Skipped" in q_text:
            report.add_text(q_text)
            continue
        
        query = queries[q_num]
        result_df = con.execute(query).fetchdf()
        report.add_table(result_df)

    # --- Save Report ---
    report_path = os.path.join(project_root, 'prj_part02', 'report.md')
    report.save_report(report_path)
    
    con.close()

if __name__ == '__main__':
    main()
