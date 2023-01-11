import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="white")

hmp2prot_data_path = 'crohns_data_log_standard_scaled_transformed.csv'
df = pd.read_csv(hmp2prot_data_path)

# remove the f__ and g__ from the column names
df.columns = df.columns.str.replace('f__', '')

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Generate a mask for the whole matrix
# mask = np.zeros_like(corr, dtype=bool)

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

#set title
plt.title('Crohns Dataset Pearson Correlation Lower Triangular Matrix', fontsize=20)

# change the angle of the x axis labels
plt.xticks(rotation=-40)

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1.0, vmax=1.0, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
