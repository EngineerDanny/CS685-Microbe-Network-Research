## Next steps in my research is to review some of the papers related to difference network models


### 1. [Demonstrating microbial co-occurrence pattern analyses within and between ecosystems](https://www.frontiersin.org/articles/10.3389/fmicb.2014.00358/full), Ryan et al. 2014

The analysis presented in this paper is designed to test for differences in co-occurrence patterns at the community level across ecosystems, identify modules of co-occurring microorganisms within communities, and identify pairwise co-occurrence patterns within modules that are consistent across ecosystems.

To test for differences in co-occurrence patterns between microbial communities from different ecosystems, we generated a dissimilarity matrix consisting of Spearman correlation coefficient distances (1-correlation coefficient) representing co-occurrence between all pairs of microorganisms from each sample (Figure 1C) using the bioDist package (Ding et al., 2014). 
The calculation of these distances produces a matrix where microbial taxa rather than samples were compared to one another. 
This Spearman's distance matrix represents the strength of correlation among microbial pairs; thus smaller distances represent stronger correlations, which were visualized using non-metric multidimensional scaling (NMDS; Figure 1E). 
We used a permutational multivariate analysis of variance (PERMANOVA; 9999 permutations) (Anderson, 2001) from the vegan package (Oksanen et al., 2013), with ecosystem type (apple flower, bodies, or soils) representing our independent variable to test for differences in co-occurrence patterns at the community level based on the Spearman's distance matrix.

Our analysis does not strictly require the use of Spearman's correlations, and other methods that measure the strength of a relationship between pairs of microbes can be easily incorporated. Additionally, the Spearman's distance may be changed by scaling any other measure (MIC, for example) between 0 and 1, subtracting that value from 1, and thereby creating a distance matrix that can be incorporated into a multivariate framework.

![image](https://github.com/EngineerDanny/CS685-Microbe-Network-Research/blob/main/Fall-2023/fmicb-05-00358-g001.jpg)

Co-Occurrence Network Statistics

We first visualized networks within each ecosystem for both positive and negative co-occurrence relationships (Figure 2, Supplemental Figure 2). We then calculated a normalized degree and betweenness score for nodes within each network and modeled relationships between these variables as a power function, αxβ, using mixed models. 

POWER-FUNCTION RELATIONSHIPS BETWEEN NODE DEGREE AND BETWEENNESS. Figures represent the power-function relationships between node degree and betweenness for microbial orders and families within each ecosystem at the 0.5 correlation level. Scales are log transformed. Each best-fit line represents the predicted values seen in Supplementary Table 4 for each correlation cutoff.

![image](https://github.com/EngineerDanny/CS685-Microbe-Network-Research/blob/main/Fall-2023/fmicb-05-00358-g003.jpg)