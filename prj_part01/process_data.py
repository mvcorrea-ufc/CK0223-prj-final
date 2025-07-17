import pandas as pd
import os
from load_data import load_dataset
from reporting import ReportGenerator

def main():
    """
    Main function to process the dataset and generate a report for Part 1.
    """
    # --- Setup ---
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    report = ReportGenerator(
        title="Data Processing Report (Lista 1)",
        introduction="This report details the data cleaning and preprocessing steps performed on the dataset."
    )
    
    # --- Load Data ---
    report.add_section("A: Load Dataset")
    df = load_dataset()
    report.add_text("Dataset loaded successfully. Here's a preview:")
    report.add_table(df.head())

    # --- Process Data ---
    report.add_section("Data Cleaning and Feature Engineering")

    # b) Missing values
    missing_values_count = df.isnull().any(axis=1).sum()
    report.add_question("b & c", "Identify missing values and count rows containing them.")
    report.add_text(f"Total number of rows with at least one missing value: **{missing_values_count}**")
    
    missing_per_column = df.isnull().sum().reset_index(name='count')
    missing_per_column.columns = ['Column', 'Missing Values']
    report.add_question("d", "Count missing values for each column.")
    report.add_table(missing_per_column)

    # e) Duplicates
    duplicates = df[df.duplicated()]
    report.add_question("e", "Identify and list duplicate rows.")
    report.add_text(f"Found **{len(duplicates)}** duplicate rows.")
    if not duplicates.empty:
        report.add_table(duplicates.head(), title="Preview of Duplicate Rows")

    # f) Domain Errors (Simplified check)
    report.add_question("f", "Identify values not belonging to the expected domain.")
    report.add_text("This step is complex without a clear data dictionary. A full implementation would require checks for each column's expected data type and format.")

    # g & h) Character and Word Counts
    df['caracteres'] = df['text_content_anonymous'].fillna('').astype(str).str.len()
    df['words'] = df['text_content_anonymous'].fillna('').astype(str).str.split().str.len()
    report.add_question("g & h", "Create 'caracteres' and 'words' columns.")
    report.add_table(df[['text_content_anonymous', 'caracteres', 'words']].head())

    # i & j) Viral and Sharings
    text_counts = df['text_content_anonymous'].value_counts()
    df['sharings'] = df['text_content_anonymous'].map(text_counts)
    df['viral'] = (df['sharings'] > 1).astype(int)
    report.add_question("i & j", "Create 'viral' and 'sharings' columns.")
    report.add_table(df[['text_content_anonymous', 'sharings', 'viral']].head())

    # k) Sentiment
    # Re-using the simple sentiment logic from before
    def get_sentiment(text):
        if not isinstance(text, str): return 0
        text_lower = text.lower()
        pos_words = ['bom', 'ótimo', 'excelente', 'gostei', 'amo', 'feliz', 'sucesso']
        neg_words = ['ruim', 'péssimo', 'odeio', 'triste', 'problema', 'lixo']
        score = sum(1 for word in pos_words if word in text_lower) - sum(1 for word in neg_words if word in text_lower)
        if score > 0: return 1
        if score < 0: return -1
        return 0
    df['sentiment'] = df['text_content_anonymous'].apply(get_sentiment)
    report.add_question("k", "Create 'sentiment' column.")
    report.add_table(df[['text_content_anonymous', 'sentiment']].head())

    # l) Remove 'trava-zaps'
    trava_zaps_mask = df['text_content_anonymous'].str.contains('trava-zaps', na=False, case=False)
    report.add_question("l", "Eliminate rows containing 'trava-zaps'.")
    report.add_text(f"Found and removed **{trava_zaps_mask.sum()}** rows containing 'trava-zaps'.")
    df = df[~trava_zaps_mask]

    # m) Inconsistencies
    report.add_question("m", "Identify inconsistencies between attributes.")
    inconsistency_check = df[df['has_media'] & df['media_type'].isnull()]
    report.add_text(f"Found **{len(inconsistency_check)}** rows where 'has_media' is True but 'media_type' is null.")

    # --- Save Report ---
    report_path = os.path.join(project_root, 'prj_part01', 'report.md')
    report.save_report(report_path)
    
    # --- Save Processed Data ---
    output_path = os.path.join(project_root, 'prj_files', 'fakeTelegram.BR_2022_processed.csv')
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


if __name__ == '__main__':
    main()

