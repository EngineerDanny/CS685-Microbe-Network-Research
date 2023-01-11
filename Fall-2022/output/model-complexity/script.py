import pandas as pd
import numpy as np
from glob import glob
import os
import pandas as pd
import numpy as np
import plotnine as p9
import matplotlib.pyplot as plt

model_complexity_df = pd.read_csv("multi_alogrithms_model_complexity_results_2022-12-06_15:03.csv")

algorithm_list = model_complexity_df["algorithm"].unique()

for algorithm in algorithm_list:
    filtered_algorithm_df = model_complexity_df[model_complexity_df["algorithm"] == algorithm]
    # Get unique values as list from column name `Dataset`
    dataset_list = filtered_algorithm_df["data_set_name"].unique().tolist()
    for dataset in dataset_list:
        # Get new dataframe with only the dataset
        sub_dataset_df = filtered_algorithm_df[filtered_algorithm_df["data_set_name"] == dataset]
        fold_id_list = sub_dataset_df["fold_id"].unique().tolist()
        
        for fold_id  in fold_id_list :
            test_error_df_list = []
            filtered_fold_id_df = sub_dataset_df[sub_dataset_df["fold_id"] == fold_id]
            
            reg_param_list = filtered_fold_id_df["reg_param"].unique().tolist()
            for reg_param in reg_param_list:
                filtered_reg_param = filtered_fold_id_df[filtered_fold_id_df["reg_param"] == reg_param]
                subtrain_loss = filtered_reg_param['subtrain_loss'].mean()
                validation_loss = filtered_reg_param['validation_loss'].mean()
        
                test_error_dict = {
                    'fold_id': fold_id,
                    'subtrain' :  subtrain_loss,
                    'validation' : validation_loss,
                    'data_set_name': dataset,
                    'reg_param': reg_param if algorithm == "Pearson Correlation" else np.log10(reg_param),
                    'algorithm' : algorithm,
                }
                test_error_df_list.append(pd.DataFrame(test_error_dict, index=[0]))
            test_err_df = pd.concat(test_error_df_list).reset_index()
            
            reg_param = "reg_param"
            # make a plot of the mean train score and mean test score for each reg_param
            test_err_df.plot(x=reg_param, y=['subtrain', 'validation'], title=f'{algorithm} Model Complexity of {dataset} Dataset, FoldID:{fold_id}', 
                             xlabel='log(alpha)' if algorithm == "LassoCV" else 'threshold', 
                             ylabel='Mean Squared Error', color = ['red', 'blue'],figsize=(10, 5),  grid=True, legend=True)
            
            # mark only the best reg_param with a blue dot
            # the best reg_param is the one that gives the minimum validation loss
            best_reg_param = test_err_df.loc[test_err_df['validation'].idxmin()]['reg_param']
            print(f"Best reg_param for {dataset} FoldID:{fold_id} is {best_reg_param}")
            plt.scatter(best_reg_param, test_err_df.loc[test_err_df['validation'].idxmin()]['validation'], color='blue')
            
   
            #reverse the scale of the x axis,
            plt.gca().invert_xaxis()
            plt.show()
        
            
