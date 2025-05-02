import os
import pandas as pd

folder = 'frameworks'

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if filename.endswith('.csv') and os.path.isfile(filepath):
        df = pd.read_csv(filepath)
        df_trimmed = df.head(6)
        df_trimmed.to_csv(filepath, index=False)  # Overwrites original file
