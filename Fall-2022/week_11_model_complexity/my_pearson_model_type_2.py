import pandas as pd
import numpy as np
import plotnine as p9
from datetime import date
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error,mean_squared_error
import sys, os
import time

# Name some string contants
out_dir = "/scratch/da2343/cs685fall22/data"
out_file = out_dir + f'/my_pearson_algorithm_model_T2_{str(date.today())}_results.csv'
amgut_data_path = './amgut1_data_scaled.csv'
n_splits = 3

# Import the csv file of the amgut1_data
amgut_data = pd.read_csv(amgut_data_path, header=0, index_col=0)
(n_rows, n_cols) = amgut_data.shape
sub_data_dict = {}
# drop only one column per every iteration to form the input matrix
# make the column you removed the output
# print the size of the input matrix
for index_col in range(n_cols):
    output_vec = amgut_data.iloc[:, index_col].to_frame()
    input_mat = amgut_data.drop(amgut_data.columns[index_col], axis=1)
    # Subset the data by decreasing the number of rows per iteration
    for index_row in range(0, n_rows-20, 20):
        input_mat_update = input_mat.iloc[:-index_row, :].to_numpy() if index_row != 0 else input_mat.to_numpy()
        output_vec_update = output_vec.iloc[:-index_row, :].to_numpy().ravel() if index_row != 0 else output_vec.to_numpy().ravel()
        sub_data_dict[f"amgut_r_{index_row}_c_{index_col}"] = (
            input_mat_update, output_vec_update, index_col)
        
data_dict= {
    'Amgut1' : sub_data_dict
}  

class MyPearsonT2:
    def fit(self,X, y):
        grad_list = []
        intercept_list = []
        for index_col in range(X.shape[1]):
            X_col = X[:, index_col]
            calc_grad, calc_intercept = self.find_model_params(X_col, y)
            grad_list.append(calc_grad)
            intercept_list.append(calc_intercept)
        # Find the mean of the gradients and intercepts
        self.gradient = grad_list
        self.intercept = intercept_list
        return self
    
    def find_model_params(self, X_col, y_col):
        calc_cor = np.corrcoef(X_col, y_col)[0, 1]
        calc_grad = calc_cor * np.std(y_col) / np.std(X_col)
        calc_intercept = (- calc_grad * np.mean(X_col)) + np.mean(y_col)
        return calc_grad, calc_intercept

    def predict(self, X):
        pred_y_list = []
        for index_col in range(X.shape[1]):
            X_col = X[:, index_col]
            calc_y = self.gradient[index_col] * X_col + self.intercept[index_col]
            pred_y_list.append(calc_y)
        return np.array(pred_y_list)  
      
test_err_list = []

for data_set_name, data_dict_val in data_dict.items():
    for sub_data_set, (input_mat, output_vec, pred_col) in data_dict_val.items():
        k_fold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
        for fold_id, indices in enumerate(k_fold.split(input_mat)):
            index_dict = dict(zip(["train", "test"], indices))
            set_data_dict = {}
            for set_name, index_vec in index_dict.items():
                set_data_dict[set_name] = {
                    "X": input_mat[index_vec],
                    "y": output_vec[index_vec]
                }
            my_pearson = MyPearsonT2()
            my_pearson.fit(**set_data_dict["train"])           
            
            test_data_x = set_data_dict["test"]['X']
            test_data_y = set_data_dict["test"]['y']
            pred_y_list = my_pearson.predict(test_data_x)
            
            # Find the mean of the mean_squared_error of the predicted columns with the actual test_data_y
            mse_list = []
            for pred_y in pred_y_list:
                mse_list.append(mean_squared_error(test_data_y, pred_y))
            mean_mse = np.mean(mse_list)    

            pred_vec = np.mean(pred_y_list, axis=0)
            # ymin is the mse - std
            ymin = mean_mse - np.std(pred_vec)
            ymax = mean_mse + np.std(pred_vec)

            test_err_dict = {
                "Mean Squared Error": mean_mse,
                "FoldID" : fold_id,
                "ymin" : ymin,
                "ymax" : ymax,
                "# of Samples": input_mat.shape[0],
                "Dataset" : data_set_name,
                "Index of Predicted Column": pred_col,
                "Algorithm": "Pearson Correlation Type 2",
            }
            print(test_err_dict)
            test_err_list.append(pd.DataFrame(test_err_dict, index=[0]))

test_err_df = pd.concat(test_err_list)
# Save dataframe as a csv to output directory
os.system("mkdir -p " + out_dir)
test_err_df.to_csv(out_file, encoding='utf-8', index=False)
print("Done!!")
