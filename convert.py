import pandas as pd

def convert_parquet_to_csv(input_path, output_path):
    df = pd.read_parquet(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")

# Paths to your parquet files
parquet_files = {
    'B/train_targets.parquet': 'B/train_targets_B.csv',
    'B/X_test_estimated.parquet': 'B/X_test_estimated_B.csv',
    'B/X_train_estimated.parquet': 'B/X_train_estimated_B.csv',
    'B/X_train_observed.parquet': 'B/X_train_observed_B.csv'
}

for input_path, output_path in parquet_files.items():
    convert_parquet_to_csv(input_path, output_path)
