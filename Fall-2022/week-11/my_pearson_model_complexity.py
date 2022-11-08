
import pandas as pd
import numpy as np
import plotnine as p9
from datetime import date
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import sys, os
import time

# Name some string contants
out_dir = "/scratch/da2343/cs685fall22/data"
test_df_file = out_dir + '/my_pearson_test_df.csv'
amgut_data_path = './amgut1_data_scaled.csv'
n_splits = 3


class MyPearsonLearner:
    def __init__(self, threshold_list):
      self.threshold_list = threshold_list
    
    def train(self, X, y, data_set_name, data_col_index):
        train_features = X
        train_labels = y
        np.random.seed(1)
        n_folds = 2
        # generate random integers between 0 and 1
        fold_vec = np.random.randint(
            low=0, high=n_folds, size=train_labels.size)
        is_set_dict = {
            "subtrain": fold_vec != (n_folds-1),
            "validation": fold_vec == (n_folds-1),
        }
        set_features = {}
        set_labels = {}
        for set_name, is_set in is_set_dict.items():
            set_features[set_name] = train_features[is_set, :]
            set_labels[set_name] = train_labels[is_set]
        loss_df_list = []    
        
        for threshold in self.threshold_list:
            grad_list = []
            intercept_list = []
            subtrain_features = set_features["subtrain"]
            subtrain_labels = set_labels["subtrain"]
            
            for index_col in range(subtrain_features.shape[1]):
                X_col = subtrain_features[:, index_col]
                calc_grad, calc_intercept = self.find_model_params(X_col, subtrain_labels, threshold)
                grad_list.append(calc_grad)
                intercept_list.append(calc_intercept)
                
            # Find the mean of the gradients and intercepts
            self.gradient = grad_list
            self.intercept = intercept_list
            
            for set_name in set_features:
                feature_mat = set_features[set_name]
                label_vec = set_labels[set_name]
                y_hat = self.predict(feature_mat)
                set_loss = mean_squared_error(label_vec, y_hat)
                
                loss_df_list.append(pd.DataFrame({
                    "set_name": set_name,
                    "loss": set_loss,
                    "threshold": threshold,
                    "data_set_name": data_set_name,
                    "index_col": data_col_index
                }, index=[0]))
                print(f"threshold: {threshold}, set_name: {set_name}, loss: {set_loss}, data_col_index: {data_col_index}")
        self.loss_df = pd.concat(loss_df_list)
        
    def find_model_params(self, X_col, y_col, threshold):
        calc_cor = np.corrcoef(X_col, y_col)[0, 1]
        # If the correlation is greater than the threshold, then calculate the gradient and intercept
        if abs(calc_cor) > threshold:
            calc_grad = calc_cor * np.std(y_col) / np.std(X_col)
            calc_intercept = np.mean(y_col) - calc_grad * np.mean(X_col)
        else:
            calc_grad = 0
            calc_intercept = 0     
        return calc_grad, calc_intercept

    def predict(self, X):
        pred_y_list = []
        for index_col in range(X.shape[1]):
            X_col = X[:, index_col]
            calc_y = self.gradient[index_col] * X_col + self.intercept[index_col]
            pred_y_list.append(calc_y)
        # Find the mean of the predicted y values
        pred_y = np.mean(pred_y_list, axis=0)
        return pred_y

def hyperparameter_training_and_diagnostic_plot():
    amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)
    (n_rows, n_cols) = amgut_data.shape
    sub_data_dict = {}
    # drop only one column per every iteration to form the input matrix
    # make the column you removed the output
    # print the size of the input matrix
    for index_col in range(n_cols):
        output_vec = amgut_data.iloc[:, index_col].to_frame()
        input_mat = amgut_data.drop(amgut_data.columns[index_col], axis=1)
        sub_data_dict[f"amgut_c_{index_col}"] = (
                input_mat.to_numpy(), output_vec.to_numpy().ravel(), index_col)   
        
    data_dict= {
        'Amgut1' : sub_data_dict
    }  


    main_test_df_list = []    
    for data_set_name, data_dict_val in data_dict.items():
        for sub_data_set, (input_mat, output_vec, index_col) in data_dict_val.items():
            threshold_list = [0.0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
            my_pearson_learner = MyPearsonLearner(threshold_list)
            my_pearson_learner.train(input_mat, output_vec, data_set_name, index_col)
            test_loss_df = my_pearson_learner.loss_df
            main_test_df_list.append(test_loss_df)
    
    main_test_df = pd.concat(main_test_df_list)        
    
    # Save dataframe as a csv to output directory
    os.system("mkdir -p " + out_dir)
    main_test_df.to_csv(test_df_file, encoding='utf-8', index=False)
    print("Done!!")
        
hyperparameter_training_and_diagnostic_plot()                
