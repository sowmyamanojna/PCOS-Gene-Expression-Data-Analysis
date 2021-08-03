# PCOS Gene Expression Data Analysis

The main of the project is: *Capturing biological patterns from gene expression data of Polycystic Ovarian  Syndrome using unsupervised dimensionality reduction algorithms*

## Motivation
Polycystic Ovarian Syndrome (PCOS) is an endocrine disorder that affects almost one-tenth of women of reproductive age globally. The exact cause of PCOS is still uncertain. Although the aetiology of PCOS isn’t known, patients diagnosed with PCOS are generally found to exhibit elevated levels of the androgen and lower levels of progesterone. In order to understand the pathophysiology of PCOS, we have explored PCOS gene expression data comprising 9 datasets from the NCBI GEO database.

We have used unsupervised linear dimensionality reduction techniques such as Principal Component Analysis (PCA), Independent Component Analysis (ICA) & Non-negative Matrix Factorization and non-linear dimensionality reduction techniques such as Variational Auto Encoders (VAE) & Denoising Auto Encoders (DAE) to extract biologically important signals from the data.

## Results
The model is able to identify the following genes - `FAM163A`, `FOLR2`, `S100A6`, `AKR1A1` and `MCL1`, that correspond to the latent dimensions that maximally separate the PCOS data points from the control data points. Out of these 5 genes, we got literature evidence for the role of the following genes - `FOLR2`, `S100A6` in PCOS.


The gene `FOLR2` (Gene ID 2350), is known to code for the protein - folate receptor beta. The folate receptor beta protein is known to play a key role in the pathways associated with vitamin digestion and absorption. Perturbations of this pathway, results in low folate production, affecting the utilization of Vitamin B12 and other B vitamins. This in turn affects the extent of the maturation egg released during ovulation. Incomplete maturation, prevents the ovaries from releasing adequate amount of progesterone that is essential in maintaining normal menstrual cycle in women.


Additionally, vitamin B12 deficiency is also associated with insulin resistance and obesity. The high levels of insulin in the blood results in enhanced production of androgen by the theca cells. This starts a cascade of actions affecting the progesterone levels, extent of maturation of the eggs. This role of folic acid in insulin
resistance and PCOS has been further ratified here.

The gene `S100A6` (Gene ID 6277) is also known to code for the S100 Calcium binding protein. This protein is known to play a key role in the stimulation of calcium dependent insulin release and prolactin secretion. They are also known to participate in the estrous cycle.

## Conclusion
We analyzed gene expression data of PCOS patients as well as non-PCOS controls using unsupervised dimensionality reduction techniques such as PCA, ICA, NMF, DAE and VAE, across a range of different latent dimensions. We found that the different models in different latent dimensional representations were able to extract interesting biological patterns about the pathophysiology of PCOS, such as the folate receptor gene and the S100 Calcium binding protein. Hence, we concluded that, in order to derive new and meaningful insights into biological data from gene expression analysis, it is essential to explore different dimensionality reduction algorithms as well as latent dimensions.

---
This work is inspired and based on the pipeline *BioBombe*.
> Compressing gene expression data using multiple latent space dimensionalities learns complementary biological representations
Way, G.P., Zietz, M., Rubinetti, V., Himmelstein, D.S., Greene, C.S.
Genome Biology (2020) [doi:10.1186/s13059-020-02021-3](https://doi.org/10.1186/s13059-020-02021-3)
