import pandas as pd
import numpy as np
from datetime import date
from sklearn.model_selection import KFold

# declare some contants
amgut_data_path = "./code/amgut1_data.csv"
n_splits = 3

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)

# Scale the amgut_data
amgut_data_scaled_np = np.where(np.std(amgut_data, axis=0) == 0, amgut_data, (
    amgut_data - np.mean(amgut_data, axis=0)) / np.std(amgut_data, axis=0))

amgut_scaled_df = pd.DataFrame(amgut_data_scaled_np, columns=amgut_data.columns)

# Split amgut_scaled_df into 3 folds
# Add a column to the amgut_scaled_df to store the fold ids
k_fold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
amgut_scaled_df['fold_id'] = 0
# Assign fold ids to each of the elements in the fold_ids column
for fold_id, indices in enumerate(k_fold.split(amgut_scaled_df)):
    amgut_scaled_df.iloc[indices[1], -1] = fold_id

# Calculate the number of 0's, 1's and 2's in the fold_ids column
fold_ids_counts = amgut_scaled_df['fold_id'].value_counts()
print(fold_ids_counts)

# Save the amgut_scaled_df to a csv file
amgut_scaled_df.to_csv(f"scaled_amgut_data_with_fold_ids_{str(date.today())}.csv")
