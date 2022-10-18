import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_absolute_error
import plotnine as p9


amgut_data = pd.read_csv('./code/amgut1_data.csv')
# remove first column
amgut_data = amgut_data.iloc[:, 1:]

data_dict = {}

(n_rows, n_cols) = amgut_data.shape

# drop only one column per every iteration to form the input matrix
# make the column you removed the output
# print the size of the input matrix
for index_col in range(n_cols):
    input_mat = amgut_data.drop(amgut_data.columns[index_col], axis=1)
    output_vec = amgut_data.iloc[:, index_col].to_frame()
    for index_row in range(1, n_rows-10):
        input_mat_update = input_mat.iloc[:-index_row, :].to_numpy()
        output_vec_update = output_vec.iloc[:-index_row, :].to_numpy()
        print(output_vec_update.shape)
        data_dict[f"amgut_r_{index_row}_c_{index_col}"] = (input_mat_update, output_vec_update)


n_splits = 3
test_acc_df_list = []
for data_set, (input_mat, output_vec) in data_dict.items():
    k_fold = KFold(n_splits=n_splits, shuffle=True, random_state=1)
    mean_test_error = 0
    for fold_id, indices in enumerate(k_fold.split(input_mat)):
        index_dict = dict(zip(["train", "test"], indices))
        set_data_dict = {}
        for set_name, index_vec in index_dict.items():
            set_data_dict[set_name] = {
                "X": input_mat[index_vec],
                "y": output_vec[index_vec]
            }

        lasso_cv = LassoCV(cv=5, random_state=0, max_iter=10000)
        lasso_cv.fit(**set_data_dict["train"])

        test_data_x = set_data_dict["test"]['X']
        test_data_y = set_data_dict["test"]['y']
        
        pred_vec = lasso_cv.predict(test_data_x)
        mean_abs_error = mean_absolute_error(test_data_y, pred_vec)
        mean_test_error += mean_abs_error
      
    mean_test_error /= 3
    test_acc_dict = {
        "test_error": mean_test_error,
        "# of Taxas": input_mat.shape[0],
        "algorithm": "LassoCV"
    }
    test_acc_df_list.append(pd.DataFrame(test_acc_dict, index=[0]))
test_acc_df = pd.concat(test_acc_df_list)
print(test_acc_df)

gg = p9.ggplot(test_acc_df, p9.aes(x="# of Samples",
                                     y="test_error")) +\
    p9.geom_line(color='blue')
gg.save("./code/my_lasso_facetted.png")
