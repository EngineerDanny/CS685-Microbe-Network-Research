
**TIMELINES AND SHEDULES** 
---

## Week 1
Review the main [research paper](https://doi.org/10.1016/j.csbj.2021.05.001). 

Make an initial literature review and powerpoint presentation from the paper.

## Week 2
Minor preview of the available correlation-based methods like SparCC, CCLasso, REBACCA, Correlation-Centric Network Command line tool and MENAP online tool. 

Find their corresponding R-packages (If they exist) and state the principle that they operate on.

| Correlation Based Method | SparCC (2012)                                                                  | CCLasso (2015)                                       | REBACCA (2015)                                                                                                                            | CoNet (2016)                                                                                                        | Meta-Network (2019)                                                                                            |
|--------------------------|--------------------------------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **R Package**                | [sparcc](https://rdrr.io/github/zdk123/SpiecEasi/man/sparcc.html)                       | [CCLasso](https://github.com/huayingfang/CCLasso)               | [REBACCA](https://faculty.wcas.northwestern.edu/hji403/REBACCA.htm)                                                                                  | [CoNetinR](https://github.com/ramellose/CoNetinR)                                                                               | [netmeta](https://github.com/guido-s/netmeta)                                                                             |
| **Principle**                | Pearson correlations via Bayesian framework                                    | Latent variable model with l1- norm shrinkage method | Linear system using pairwise log ratios                                                                                                   | Bray and Curtis, Kullback–Leibler dissimilarity measures, Pearson and Spearman correlation, and mutual information. | Hybrid method with Pearson Correlation and graph-based method FS-Weight method to study indirect relationships |
| **Research Paper / Article** | [journal.pcbi.1002687](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002687) | [CCLasso](https://www.math.pku.edu.cn/teachers/dengmh/CCLasso/) | [REBACCA](https://www.researchgate.net/publication/278731609_Investigating_microbial_co-occurrence_patterns_based_on_metagenomic_compositional_data) | [barebonesCoNet](https://hallucigenia-sparsa.github.io/seqgroup/reference/barebonesCoNet.html)                                        | https://link.springer.com/book/10.1007/978-3-319-21416-0                                                       |
| **Link to Data**             | No data available                                                              | No data available                                    | No data available                                                                                                                         | No data available                                                                                                   | [data](https://github.com/guido-s/netmeta/tree/develop/data)                                                           |


## Week 3
Research on existing R packages available on CRAN, Github or Bioconductor that implement the conditional-dependence methods like SPIEC-EASI, MDiNE, MixMPLN, COZINE, etc

| Conditional Dependence Method | R package                                            | Principle                                                                                                           | Link to Data                                            |
|-------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| gCoda (2017)                  | [gCoda](https://github.com/huayingfang/gCoda)        | Logistic normal distribution Majorization-Minimization algorithm                                                    | No Data available                                       |
| NetComi (2020)                | [NetComi](https://github.com/stefpeschel/NetCoMi)    | Integrates extensive methods that take into account the special characteristics of amplicon data.                   | https://github.com/joey711/phyloseq/tree/master/data    |
| SPIEC-EASI (2015)             | [SpiecEasi](https://github.com/zdk123/SpiecEasi)     | Graphical models using selecting neighborhoods or inverse covariance                                                | https://github.com/zdk123/SpiecEasi/tree/master/data    |
| MDiNE (2019)                  | [mdine](https://github.com/kevinmcgregor/mdine)      | Bray and Curtis, Kullback–Leibler dissimilarity measures, Pearson and Spearman correlation, and mutual information. | https://github.com/kevinmcgregor/mdine/tree/master/data |
| MixMPLN (2019)                | [MixPLN](https://github.com/sahatava/MixMPLN)        | Hybrid method with Pearson Cor- relation and graph-based method FS-Weight method to study indirect relationships    | https://github.com/sahatava/MixMPLN/tree/master/data    |
| Mint (2015)                   | [MInt](https://cran.r-project.org/web/packages/MInt) | Poisson-multivariate normal hierarchical model                                                                      | No Data available                                       |
| mLDM (2016)                   | [mLDM](https://github.com/tinglab/mLDM)              | Lognormal-Dirichlet Multinomial hierarchical model                                                                  | https://github.com/tinglab/mLDM/tree/master/CRC         |
| HARMONIES (2020)              | [HARMONIES](https://github.com/shuangj00/HARMONIES)  | Zero-inflated negative binomial distribution with Dirichlet process prior                                           | https://github.com/shuangj00/HARMONIES/tree/master/data |
| COZINE (2020)                 | [COZINE](https://github.com/MinJinHa/COZINE)         | Multivariate Gaussian Hurdle model                                                                                  | https://github.com/MinJinHa/COZINE/tree/master/data     |



## Week 4 
Get all the publicly available microbiome composition datasets and make a table from it with columns, `Data name` , `Package` , `Source` , `Citation` , `No of Samples` and `No of Taxa`

                  PUBLICLY AVAILABLE MICROBIOME COMPOSITION DATASETS


| Data name           | Package    | Source                                                                                            | Citation                                                                                                              | No of Samples                               | No of Taxa                                   |
|---------------------|------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------|
| amgut1.filt         | SPIEC-EASI | [amgut1.filt.rda](https://github.com/zdk123/SpiecEasi/blob/master/data/amgut1.filt.rda)           | [10.1371/journal.pcbi.1004226](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226)        | ```nrow(amgut1.filt) = 289```               | ```ncol(amgut1.filt) = 127```                |
| amgut2.filt.phy.rda | SPIEC-EASI | [amgut2.filt.phy.rda](https://github.com/zdk123/SpiecEasi/blob/master/data/amgut2.filt.phy.rda)   | [10.1371/journal.pcbi.1004226](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226)        | ```ncol(amgut2.filt.phy@otu_table) = 296``` | ```nrow(amgut2.filt.phy@otu_table) = 138```  |
| hmp216S             | SPIEC-EASI | [hmp2.rda](https://github.com/zdk123/SpiecEasi/blob/master/data/hmp2.rda)                         | https://ibdmdb.org/tunnel/public/summary.html                                                                         | ```ncol(hmp216S@otu_table) = 47```          | ```nrow(hmp216S@otu_table) = 45```           |
| hmp2prot            | SPIEC-EASI | [hmp2.rda](https://github.com/zdk123/SpiecEasi/blob/master/data/hmp2.rda)                         | https://ibdmdb.org/tunnel/public/summary.html                                                                         | ```ncol(hmp2prot@otu_table) = 47```         | ```nrow(hmp2prot@otu_table) = 43```          |
| GlobalPatterns      | phyloseq   | [GlobalPatterns.RData](https://github.com/joey711/phyloseq/blob/master/data/GlobalPatterns.RData) | [10.1371/journal.pone.0061217](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061217)             | ```ncol(GlobalPatterns@otu_table) = 26```   | ```nrow(GlobalPatterns@otu_table) = 19216``` |
| enterotype          | phyloseq   | [enterotype.RData](https://github.com/joey711/phyloseq/blob/master/data/enterotype.RData)         | [10.1371/journal.pone.0061217](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061217)             | ```ncol(enterotype@otu_table) = 280```      | ```nrow(enterotype@otu_table) = 553```       |
| esophagus           | phyloseq   | [esophagus.RData](https://github.com/joey711/phyloseq/blob/master/data/esophagus.RData)           | [10.1371/journal.pone.0061217](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061217)             | ```ncol(esophagus@otu_table) = 3```         | ```nrow(esophagus@otu_table) = 58```         |
| soilrep             | phyloseq   | [soilrep.RData](https://github.com/joey711/phyloseq/blob/master/data/soilrep.RData)               | [10.1371/journal.pone.0061217](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061217)             | ```ncol(soilrep@otu_table) = 56```          | ```nrow(soilrep@otu_table) = 16825```        |
| crohns              | mdine      | [crohns.RData](https://github.com/kevinmcgregor/mdine/blob/master/data/crohns.RData)              | https://www.mcgill.ca/statisticalgenetics/software                                                                    | 100                                         | 5                                            |
| Real data           | MixMPLN    | [MixMPLN_real_data.csv](https://github.com/sahatava/MixMPLN/blob/master/data/real_data.csv)               | https://pubmed.ncbi.nlm.nih.gov/31510709/                                                                             | ```nrow(real_data) = 195```                 | ```ncol(real_data) = 129```                  |
| Baxter_CRC          | mLDM       | [Baxter_CRC.RData](https://github.com/tinglab/mLDM/blob/master/CRC/Baxter_CRC.RData)              | http://www.raeslab.org/companion/ocean-interactome.html                                                               | 490                                         | 117                                          |
| glne007             | mLDM       | [glne007.csv](https://github.com/tinglab/mLDM/blob/master/CRC/glne007.csv)                        | http://www.raeslab.org/companion/ocean-interactome.html                                                               | 490                                         | 338                                          |
| iOraldat            | COZINE     | [iOraldat.rda](https://github.com/MinJinHa/COZINE/blob/master/data/iOraldat.rda)                  | [biomedcentral.com/articles/10.1186](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03911-w) | ```nrow(iOraldat) = 86```                   | ```ncol(iOraldat) = 63```                    |


## Week 5
Review the SPIEC-EASI conditional-dependence method. 

Write a literature review of the [main paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226) and assess it with the state-of-the-art methods like the Standard Pearson Correlation, SparCC and CCREPE.

### Literature Review of [Sparse and Compositionally Robust Inference of Microbial Ecological Networks (SPIEC-EASI)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226#pcbi.1004226.s011)

### Background
**SPIEC-EASI** is a statistical method which aims at inferring microbial ecological networks. It infers these networks from amplicon sequencing datasets. Abundances of the Operational Taxonomic Unit (OTU) are composed of several elements. This makes using traditional methods like correlation to infer networks lead to false results. With Microbial sequencing-based studies, only a few OTUs are measured on several samples. This makes additional information or assumption very essential for inference of microbial networks accurately. SPIEC EASI is a conditionally dependent method which assumes that ecological networks are sparse. 

### Previous Work
A commonly used tool to infer a network is **correlation analysis**. In this analysis, Pearson’s correlation coefficient are computed among all pairs of OTU samples. An interaction between microbes is assumed when the absolute value of the correlation coefficient is very high. There are also recent methods like **Sparse Correlations for Compositional data (SparCC)** and **Compositionally Corrected by REnormalization and PErmutation (CCREPE)**. These recent methods are designed to account for the compositional biases and represent the **state of the art** in the field. However, these correlation-based methods are experimentally biased because of sampling depth. Also, correlations can arise between OTUs that are indirectly connected in an ecological network.

### Novelty
SPIEC-EASI inference comprises of two steps. Firstly, OTU data is transformed using compositional data analysis. Secondly, **SPIEC-EASI** estimates the interaction graph from the transformed data using either neighborhood selection or sparse inverse covariance selection. Unlike empirical correlation or covariance estimation, used in SparCC and CCREPE, SPIEC-EASI seeks to infer an underlying graphical model using the concept of **conditional independence** which avoids detection of correlated but indirectly connected OTUs. This ensures parsimony of the resulting network model. The model is an undirected graph where links between nodes represent signed associations between OTUs.

### Results
SPIEC-EASI inference was assessed with the state-of-the-art inference methods (SparCC and CCREPE) and the standard Pearson Correlation. This was done by varying parameters known to influence network recovery (network topology, association strength and sample number) and quantifying performance on resulting networks. 

#### Test 1
An experiment was done to showcase the various methods’ performance on 960 independent synthetic datasets for a total of 48 conditions (4 samples sizes × 2 conditions numbers × 3 network topologies × 2 dimensions). 

![Picture1](https://user-images.githubusercontent.com/47421661/193098230-c624abec-02ea-49df-9271-d45dc64ea741.png)

- Area Under Precision-Recall (AUPR) vs. number of samples n for different κ values are depicted.
- Asterisks denote conditions under which SPIEC-EASI had significantly higher AUPR relative to all other control methods.

To quantify each method’s ability to recover the true underlying association network, performance in terms of precision-recall (P-R) curves and Area Under P-R curves (AUPR) was evaluated.
It can be inferred from the figure above that, all the methods that take the compositional nature of the data into account outperforms the Standard Pearson Correlation. Also, in the large sample limit where n = 1360, S-E(MB) is the only method that averagely recovers a substantial portion of edges under all scenarios.

#### Test 2

The figure below shows the network reproducibility for **SPIEC-EASI** methods, SparCC, and CCREPE. This is measured by computing the Hamming distance between the reference and new network models (the difference between the upper triangular part of the two adjacency matrices).

![Picture2](https://user-images.githubusercontent.com/47421661/193102725-deca7bd1-013d-4b44-84f5-77cc68222593.png)

From the figure above, it can be inferred that the S-E(MB) method has the smallest Hamming distance, followed by S-E(glasso), SparCC and CCREPE. 
The numerical experiments demonstrate that the SPIEC-EASI method is more reproducible than other current methods.
SPIEC-EASI produced more consistent and sparser interaction networks than SparCC and CCREPE when they were tested on the real American Gut Project (AGP) data.


### Future Work
- Most of the experiments were done on datasets that resemble real microbiome samples in terms of taxa dispersion and marginal distributions and generated using the SPIEC-EASIE synthetic data generator. More tests could be done on available realistic datasets like the American Gut Project (AGP) instead of the synthetic datasets. 
- More tests could be done on SPIEC-EASIE in comparison to other non state-of-the-art methods like Mint(2015), Cozine(2020), etc.
- Statistical methods to infer which taxa are responsive to design factors in 16S gene amplicon studies could also be researched.
- Inference of taxa responses from 16S rRNA gene sequencing datasets could be studied and improved.


## Week 6
General review of all the papers and make a table with columns `Method`, `Research Paper`, `Algorithms Compared` and `How they compare`.

This is a table comparing the data analysis performed by each of the methods from the various papers.

| **Method**  | **Research Paper**                                                                                                                                                                                             | **Algorithms Compared**                                   | **How they compare**                                                                                                                                                                                                                                                                                                                                                                        | Category of Evaluation type |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| SPIEC EASIE | [pcbi-1004226-g006](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226#pcbi-1004226-g006)                                                                                          | SPIEC-EASIE, SparCC, CCREPE                               | **Consistency** between two models by computing Hamming Distance (the difference between the upper triangular part of the two adjacency matrices) between reference and new models.                                                                                                                                                                                                         | External data               |
| COZINE      | [ncbi-PMC7768662](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7768662/)                                                                                                                                       | COZINE, SPIEC-EASIE, Ising                                | **Stability** of edges (The stability of each edge is defined by the proportion of bootstrap samples where the resulting networks include the edge)                                                                                                                                                                                                                                         | Bootstrap analysis          |
| CCLasso     | [academic.oup-211784](https://academic.oup.com/bioinformatics/article/31/19/3172/211784)                                                                                                                       | CCLasso, SparCC                                           | **Frobenius Accuracy** with respect to estimating correlation matrix from data using half samples (measured by the Frobenius norm distance between the estimated correlation matrices and a reference correlation matrix).<br>**Reproducibility** (measured by the fraction of the same edges shared for the two steps in the first reference network which only the top 1/4 edges is used) | Sub-sample analysis         |
| SparCC      | [journal.pcbi.1002687](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002687)                                                                                                         | SparCC, Pearson                                           | Computing the number of true-positives (TP), false-positives (FP), true-negatives (TN) and false-negatives (FN) detected in the Pearson network by treating the SparCC network as the true one.                                                                                                                                                                                             | External data               |
| REBACCA     | [researchgate-278731609](https://www.researchgate.net/publication/278731609_Investigating_microbial_co-occurrence_patterns_based_on_metagenomic_compositional_data)                                            | REBACCA, SparCC, BP, ReBoot                               | **Consistency** of correlated pairs identified independently from the three datasets (A correlated pair of OTUs is consistent between two datasets if the pair has the same signs of correlations in both datasets).                                                                                                                                                                        | External data               |
| MDiNE       | [researchgate-337112062](https://www.researchgate.net/publication/337112062_MDiNE_A_model_to_estimate_differential_co-occurrence_networks_in_microbiome_studies)                                               | MDiNE , MInt, COZINE, SPIEC-EASIE                         | The number of edges in a sample. An edge is shown when the co-occurrence between a pair of taxa differs signiﬁcantly between the two groups based on the 90% credible interval.                                                                                                                                                                                                             | Sub-sample analysis         |
| gCoda       | [researchgate-316849033](https://www.researchgate.net/publication/316849033_gCoda_Conditional_Dependence_Network_Inference_for_Compositional_Data)                                                             | gCoda, SPIEC-EASIE                                        | The numbers of **inferred edges** and **edge density** in a sample.                                                                                                                                                                                                                                                                                                                         | Sub-sample analysis         |
| MixMPLN     | [academic.oup-5529264](https://academic.oup.com/bioinformatics/article/35/14/i23/5529264)                                                                                                                      | MixMPLN + glasso, MixMPLN + huge                          | Optimal number of components(taxas) from the sample-taxa matrix is inferred using the [silhouette method](https://rdrr.io/cran/factoextra/man/fviz_silhouette.html) from the [`factoextra`](https://rdrr.io/cran/factoextra/) R package. (Optimal implies highest silhouette width)                                                                                                         | Sub-sample analysis         |
| MINT        | [researchgate-314088430](https://www.researchgate.net/publication/314088430_MINT_A_multivariate_integrative_method_to_identify_reproducible_molecular_signatures_across_independent_experiments_and_platforms) | MINT, PLSDA, sPLSDA, ComBat+sPLSDA, RF, mgPLS, BMC+PLSDA  | **Classification accuracy, Reproducibility and Balanced Error Rates (BER)** with respect to inferring gene signatures from cells.                                                                                                                                                                                                                                                           | External data               |
| mLDM        | [biorxiv-10.1101](https://www.biorxiv.org/content/10.1101/042630v1.full)                                                                                                                                       | mLDM,PCC,SCC,CCREPE, SparCC, CCLasso, glasso, SPIEC-EASIE | Ability to infer OTU-OTU associations(specifically symbiotic interactions like parasitism, mutualism, etc ) from metagenomic sequencing data.                                                                                                                                                                                                                                               | External data               |
| NetCoMi     | [academic.oup-6017455](https://academic.oup.com/bib/article/22/4/bbaa290/6017455)                                                                                                                              | SparCC, SPIEC-EASI, SPRING                                | Variability of microbial networks between the association estimation methods, Aitchison’s distance (Euclidean distance between clr-transformed compositions) between taxas for constructing sample similarity networks.                                                                                                                                                                     | Sub-sample analysis         |


## Week 7
Write code for the **LASSO** method in Python or R for  matrix completion using the American Gut Data set.


## Week 8
Implement the **LASSO** method considering all the columns(p different models). 

For every iteration, predict one column(y) and make the other columns features(X). 

Then find the `average test error` for each of the `number of samples`.

## Week 9
Implement the **Pearson Correlation** method. 

Plot a graph demonstrating the `test error` against the `number of samples`.
 
 ## Week 10
Compare the **LASSO** algorithm with the **Pearson Correlation** method. 

Plot a graph to show which of the methods is accurate.

## Week 11
Regularize the **Pearson Correlation Model** to find the optimal hyper-paramter(s) to use. 

Different ways of training the **Pearson Correlation Model**(Type 2 ?). 

## Week 12_12
Log-transformation and scaling of whole datasets. 

Testing different scaling methods for this sparse datasets. 

Running algorithm/multi-column test-error script for different real datasets.

