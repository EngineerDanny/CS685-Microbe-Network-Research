import glob
import os
import pandas as pd

# Prepare amgut2_data.csv
amgut2_data = pd.read_csv('./amgut2_data.csv', header=0, index_col=0)

# Make the columns into rows and vice versa
amgut2_data = amgut2_data.T
# amgut2_data = amgut2_data.iloc[:, 1:]
amgut2_data.to_csv('./amgut2_data_update.csv', index=False)

baxter_crc_data = pd.read_csv('./baxter_crc_data.csv', header=0, index_col=0)
baxter_crc_data.to_csv('./baxter_crc_data_update.csv', index=False)

crohns_data = pd.read_csv('./crohns_data.csv', header=0, index_col=0)
# Remove the last column
crohns_data = crohns_data.iloc[:, :-1]
crohns_data.to_csv('./crohns_data_update.csv', index=False)

glne007_data = pd.read_csv('./glne007.csv', header=0, index_col=0)
# Remove first 2 columns
glne007_data = glne007_data.iloc[:, 3:]
glne007_data.to_csv('./glne007_data_update.csv', index=False)

hmp2prot_data = pd.read_csv('./hmp2prot_data.csv', header=0, index_col=0)
hmp2prot_data = hmp2prot_data.T
hmp2prot_data.to_csv('./hmp2prot_data_update.csv', index=False)

hmp216S_data = pd.read_csv('./hmp216S_data.csv', header=0, index_col=0)
hmp216S_data = hmp216S_data.T
hmp216S_data.to_csv('./hmp216S_data_update.csv', index=False)

mixmpln_real_data = pd.read_csv('./mixmpln_real_data.csv', header=0, index_col=0)
# Remove the first column
mixmpln_real_data = mixmpln_real_data.iloc[:, 1:]
mixmpln_real_data.to_csv('./mixmpln_real_data_update.csv', index=False)

soilrep_data = pd.read_csv('./soilrep_data.csv', header=0, index_col=0)
soilrep_data = soilrep_data.T
mixmpln_real_data.to_csv('./soilrep_data_update.csv', index=False)

esophagus_data = pd.read_csv('./esophagus_data.csv', header=0, index_col=0)
esophagus_data = esophagus_data.T
esophagus_data.to_csv('./esophagus_data_update.csv', index=False)

enterotype_data = pd.read_csv('./enterotype_data.csv', header=0, index_col=0)
enterotype_data = enterotype_data.T
enterotype_data = enterotype_data.iloc[:, 1:]
enterotype_data.to_csv('./enterotype_data_update.csv', index=False)
