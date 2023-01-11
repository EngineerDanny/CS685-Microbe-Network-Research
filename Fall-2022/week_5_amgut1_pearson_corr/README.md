## Literature Review of [Sparse and Compositionally Robust Inference of Microbial Ecological Networks (SPIEC-EASI)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226#pcbi.1004226.s011)

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

### Reference
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004226#pcbi.1004226.s011


