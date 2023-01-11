import pandas as pd
import numpy as np
import plotnine as p9
from datetime import date
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
import sys, os

# Name some string contants
amgut_data_path = 'amgut1_data.csv'

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)
# Remove the last column, fold_id, from the dataframe
amgut_data = amgut_data.iloc[:, :-1]

data_dict = {}

n_row = amgut_data.shape[0]

data_dict["amgut_0"] = amgut_data
# should be in the range of 20s
for index in range(1, n_row-20, 20):
    sub_data_df = amgut_data.iloc[:-index, :]
    data_dict[f"amgut{index}"] = sub_data_df
    
    
test_acc_df_list = []
for data_set_name, sub_data_df in data_dict.items():
    cor_df = pd.DataFrame(columns=['taxa1', 'taxa2', 'cor', 'grad', 'intercept'])
    n_col = len(sub_data_df.columns)
    # ## Get cor_df from file system
    # cor_df = pd.read_csv('./code/cor_df.csv')
    # ## Filter it by the data_set_name column
    # cor_df = cor_df[cor_df['dataset']==data_set_name]
    
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

                if abs_calc_cor >= 0:
                    # Append the taxa1, taxa2, cor to the cor_df
                    cor_df = pd.concat([cor_df,
                                        pd.DataFrame({'taxa1': sub_data_df.columns[i],
                                                      'taxa2': sub_data_df.columns[j],
                                                      'cor': abs_calc_cor,
                                                      'grad': grad,
                                                      'intercept': intercept}, index=[0])
                                        ], axis=0, ignore_index=True)
 
    for index_col in range(125,126,125):
        # Let X be all the columns/taxa except the dropped column/taxa of the sub_data dataframe
         index_col = -1
         y_actual = sub_data_df.iloc[:, index_col]
         X_features = sub_data_df.drop(sub_data_df.columns[index_col], axis=1)
        # get the name of y
         y_name = sub_data_df.columns[index_col]
        # Loop through all the columns in X
         y_pred_list = []
         for col_index in range(0, len(X_features.columns)):
            # get the name of the column
            x_name = X_features.columns[col_index]
            # get the column
            x_col = X_features.iloc[:, col_index]
            # find the combination of x_name and y_name in the cor_df
            # and get the gradient and intercept
            grad = cor_df.loc[(cor_df['taxa1'] == x_name) & (
                cor_df['taxa2'] == y_name), 'grad'].values[0]
            intercept = cor_df.loc[(cor_df['taxa1'] == x_name) & (
                cor_df['taxa2'] == y_name), 'intercept'].values[0]
            y_pred = np.array((grad * x_col) + intercept)
            y_pred_list.append(y_pred)

            y_pred_mean = np.mean(y_pred_list, axis = 0)
            ma_error = mean_absolute_error(y_actual.to_numpy(), y_pred_mean)
            test_acc_dict = {
                "test_error": ma_error,
                "# of Samples": sub_data_df.shape[0],
                "Index of Predicted Column": index_col,
                "Algorithm": "Pearson Correlation",
                "Data Set": "American Gut",
            }
            test_acc_df_list.append(pd.DataFrame(test_acc_dict, index=[0]))
            
test_acc_df = pd.concat(test_acc_df_list)


test_acc_df = pd.concat(test_acc_df_list)
print(test_acc_df)
gg = p9.ggplot(test_acc_df, p9.aes(x="# of Samples",
                                     y="test_error" )) +\
    p9.geom_line(color='red')
gg.save("my_pearson_simple_facetted_1.png")
