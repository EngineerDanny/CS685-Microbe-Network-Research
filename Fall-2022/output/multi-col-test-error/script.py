import pandas as pd
import numpy as np
from glob import glob
import os
import pandas as pd
import numpy as np
import plotnine as p9

error_df = pd.read_csv("results.csv")

# Get unique values as list from column name `Dataset`
dataset_list = error_df["Dataset"].unique().tolist()
for dataset in dataset_list:
    test_error_df_list = []
    # Get new dataframe with only the dataset
    sub_dataset_df = error_df[error_df["Dataset"] == dataset]
    n_samples_list = sub_dataset_df["# of Samples"].unique().tolist()
    
    for n_sample in n_samples_list:
        filtered_csv = sub_dataset_df[sub_dataset_df["# of Samples"] == n_sample]
        algo_list = filtered_csv["Algorithm"].unique().tolist()
        
        for algorithm in algo_list:
            sub_filtered_csv = filtered_csv[filtered_csv["Algorithm"] == algorithm]
            # Get new dataframe with only the dataset and n_sample
            mean_mse = sub_filtered_csv['Mean Squared Error'].mean()
            std_mse = sub_filtered_csv['Mean Squared Error'].std()
            mse_min = mean_mse - std_mse
            mse_max = mean_mse + std_mse
            
            test_error_dict = {'# of Samples': n_sample,
                            'Mean Squared Error': mean_mse,
                            'ymin' : mse_min,
                            'ymax' : mse_max,
                            'Dataset': dataset,
                            'Algorithm': algorithm,
                            }
            test_error_df_list.append(pd.DataFrame(test_error_dict, index=[0]))
    my_combined_results_df = pd.concat(test_error_df_list).reset_index()
    
    gg = p9.ggplot(my_combined_results_df) +\
    p9.aes(x='# of Samples', y='Mean Squared Error', ymin="ymin", ymax= "ymax",  fill = "Algorithm") +\
    p9.facet_wrap('~Dataset') +\
    p9.geom_line( p9.aes(color = "Algorithm") ) +\
    p9.geom_ribbon(alpha = 0.1) +\
    p9.scale_fill_manual(values=["green", "red", "blue", "orange"]) +\
    p9.scale_color_manual(values=["green",  "red", "blue", "orange"]) +\
    p9.ggtitle(f"Multi-Col Test Error for {dataset} Dataset") +\
    p9.xlab("# of Samples") +\
    p9.ylab("Mean Squared Error") 
    # show the plot
    print(gg)
    gg.save(f"{dataset}_updated_graph.png")
    
    
