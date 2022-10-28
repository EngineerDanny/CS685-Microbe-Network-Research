import pandas as pd
import numpy as np
from datetime import date
from sklearn.model_selection import KFold

# declare some contants
amgut_data_path = "amgut1_data.csv"
n_splits = 3

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)
# Split amgut_data into 3 folds
# Add a column to the amgut_data to store the fold ids
k_fold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
amgut_data['fold_id'] = 0
# Assign fold ids to each of the elements in the fold_ids column
for fold_id, indices in enumerate(k_fold.split(amgut_data)):
    amgut_data.iloc[indices[1], -1] = fold_id

# Calculate the number of 0's, 1's and 2's in the fold_ids column
fold_ids_counts = amgut_data['fold_id'].value_counts()
print(fold_ids_counts)

# Save the amgut_data to a csv file
amgut_data.to_csv(f"amgut_data_with_fold_ids_{str(date.today())}.csv")
