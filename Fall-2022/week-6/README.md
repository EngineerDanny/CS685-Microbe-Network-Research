This is a table comparing the data analysis performed by each of the methods from the various papers.

| Method      | Paper/Citation | Algorithms Compared        | How they compare              |
|-------------|----------------|----------------------------|-------------------------------|
| SPIEC EASIE |                | SPIEC-EASIE                | Reliability, Hamming Distance |
| COZINE      |                | COZINE, SPIEC-EASIE, ISING | Phylo Tree, Assortativity     |
|             |                |                            |                               |




- The **Consistent Accuracy** is measured by the Frobenius norm distance between the estimated correlation matrices of the first and second step.
- The **Consistent reproducibility** is measured by the fraction of the same edges shared for these two steps in the first gold reference network which only the top 1/4 edges is used.
