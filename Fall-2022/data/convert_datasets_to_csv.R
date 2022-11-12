# Load the libraries
library(dplyr)
library(ggpubr)
library(SpiecEasi)
library(phyloseq)

data("amgut1.filt")
amgut1_data <- data.frame(amgut1.filt)
write.csv(amgut1_data, "amgut1_data.csv")


data("amgut2.filt.phy")
amgut2_data <- as.data.frame(amgut2.filt.phy@otu_table)
write.csv(amgut2_data, "amgut2_data.csv")

data("hmp2")
hmp216S_data <- as.data.frame(hmp216S@otu_table)
hmp2prot_data <- as.data.frame(hmp2prot@otu_table)
write.csv(hmp216S_data, "hmp216S_data.csv")
write.csv(hmp2prot_data, "hmp2prot_data.csv")

data("GlobalPatterns")
global_patterns_data <- as.data.frame(GlobalPatterns@otu_table)
write.csv(global_patterns_data, "global_patterns_data.csv")

data("enterotype")
enterotype_data <- as.data.frame(enterotype@otu_table)
write.csv(enterotype_data, "enterotype_data.csv")

data("esophagus")
esophagus_data <- as.data.frame(esophagus@otu_table)
write.csv(esophagus_data, "esophagus_data.csv")

data("soilrep")
soilrep_data <- as.data.frame(soilrep@otu_table)
write.csv(soilrep_data, "soilrep_data.csv")

load("~/iOraldat.rda")
ioral_data <- as.data.frame(iOraldat)
write.csv(ioral_data, "ioral_data.csv")

load("~/crohns.RData")
crohns_data <- as.data.frame(crohns$otu.counts)
write.csv(crohns_data, "crohns_data.csv")

load("~/Baxter_CRC.RData")
baxter_crc_data <- as.data.frame(X)
write.csv(baxter_crc_data, "baxter_crc_data.csv")

