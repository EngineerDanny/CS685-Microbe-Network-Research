import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotnine as p9
from sklearn.metrics import mean_absolute_error

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv("./code/amgut1_data.csv", header=0, index_col=0)
data_dict = {}

total_row_nos = amgut_data.shape[0]
for index in range( 1, total_row_nos-10):
    sub_data = amgut_data.iloc[:-index, :]
    data_dict[f"amgut{index+1}"] = sub_data


test_acc_df_list = []
for data_set, sub_data in data_dict.items():    
    cor_df = pd.DataFrame(columns=['taxa1', 'taxa2', 'cor'])
    for i in range(0, len(sub_data.columns)):
        for j in range(0, len(sub_data.columns)):
            if i != j:
                taxa1_col = sub_data.iloc[:, i] 
                taxa2_col = sub_data.iloc[:, j] 
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
                    print(abs_calc_cor)
                    # Append the taxa1, taxa2, cor to the cor_df
                    cor_df = cor_df.append({'taxa1': sub_data.columns[i], 
                                            'taxa2': sub_data.columns[j], 
                                            'cor': abs_calc_cor, 
                                            'grad': grad, 
                                            'intercept': intercept, 
                                            }, ignore_index=True)
                    
    # Let y be the last column/taxa of the amgut1_data dataframe
    y_actual = sub_data.iloc[:, -1]
    # get the name of y
    y_name = sub_data.columns[-1]
    # Let x be all the columns/taxa except the last column/taxa of the amgut1_data dataframe
    X = sub_data.iloc[:, :-1]

    # Loop through all the columns in X
    y_pred_list = []
    for col_index in range(0, len(X.columns)):
        
        # get the name of the column
        x_name = X.columns[col_index]
        # get the column
        x_col = X.iloc[:, col_index]
        
        # find the combination of x_name and y_name in the cor_df
        # and get the gradient and intercept
        grad = cor_df.loc[(cor_df['taxa1'] == x_name) & (cor_df['taxa2'] == y_name), 'grad'].values[0]
        intercept = cor_df.loc[(cor_df['taxa1'] == x_name) & (cor_df['taxa2'] == y_name), 'intercept'].values[0]
        y_pred = np.array((grad * x_col) + intercept)
        y_pred_list.append(y_pred)
        # print("Got Y pred here")

    y_pred_mean = np.mean(y_pred_list, axis = 0)
    ma_error = mean_absolute_error(y_actual.to_numpy(), y_pred_mean)

    test_acc_dict = {
        "test_error": ma_error,
        "# of Samples": sub_data.shape[0],
        "algorithm": "Pearson Correlation"
    }

    test_acc_df_list.append(pd.DataFrame(test_acc_dict, index=[0]))

test_acc_df = pd.concat(test_acc_df_list)
print(test_acc_df)
gg = p9.ggplot(test_acc_df, p9.aes(x="# of Samples",
                                     y="test_error" )) +\
    p9.geom_smooth(color='blue')
gg.save("./code/my_pearson_facetted.png")
