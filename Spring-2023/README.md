**TIMELINES AND SHEDULES** 
---

- **Week 1**  : Organize the code and results on monsoon and Github.

- **Week 2**  : Usage of R2 score/RMSE instead of MSE (since it is more widely used and understandable for the microbiome/soil people).
                Add a scatterplot of predicted vs actual label values in the train and test sets useful to explain how the R2 is computed.

"how many samples do we need to gather in order for cross-validation to be useful?" 
To do that I would down-sample each data set, then run the same analyses you have been doing. 
Start with one data set where you can clearly see the difference between Pearson and Lasso. 
At some point when you remove a certain number of samples that difference should disappear (get very small) 
and then at some point both models should be about the same error as featureless. 
That will give us some indication about how many samples would be necessary for our analysis 
to "work" or inform about which algos are more/less accurate.
