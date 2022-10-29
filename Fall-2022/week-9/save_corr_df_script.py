import pandas as pd
import numpy as np
import sys
import os

 
    
amgut_data_path = "./amgut1_data.csv"

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)
data_dict = {}

n_row = amgut_data.shape[0]

# Set the max dataset to amgut_full
data_dict["amgut_0"] = amgut_data
# should be in the range of 26s
for index in range(1, n_row-20, 20):
    sub_data_df = amgut_data.iloc[:-index, :]
    data_dict[f"amgut_{index}"] = sub_data_df
    print(f"amgut_{index} is done , shape is {sub_data_df.shape}")

cor_df_list = []
cor_df = pd.DataFrame(columns=['taxa1', 'taxa2', 'cor', 'dataset'])
for data_set_name, sub_data_df in data_dict.items():
    n_col = len(sub_data_df.columns)
    for i in range(n_col):
        for j in range(n_col):
            if i != j:
                taxa1_col = sub_data_df.iloc[:, i]
                taxa2_col = sub_data_df.iloc[:, j]
                calc_cor = taxa1_col.corr(taxa2_col, method='pearson')
                abs_calc_cor = abs(calc_cor)

                # Calculate the standard deviation of taxa1 and taxa2 columns respectively
                sd_taxa1 = np.std(taxa1_col)
                sd_taxa2 = np.std(taxa2_col)

                mean_taxa1 = np.mean(sd_taxa1)
                mean_taxa2 = np.mean(sd_taxa2)

                grad = (calc_cor * sd_taxa2) / sd_taxa1
                intercept = (-grad * mean_taxa1) + mean_taxa2

                # Append the taxa1, taxa2, cor to the cor_df
                cor_dict = {'taxa1': sub_data_df.columns[i],
                            'taxa2': sub_data_df.columns[j],
                            'cor': abs_calc_cor,
                            'dataset': data_set_name,
                            'grad': grad,
                            'intercept': intercept}
                cor_df_list.append(pd.DataFrame(cor_dict, index=[0]))

cor_df = pd.concat(cor_df_list)


# Save dataframe as a csv to output directory
cor_df.to_csv("cor_df.csv", encoding='utf-8', index=False)
print("Done!!")
