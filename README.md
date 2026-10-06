# Data Science Expeditions

This repository is a personal collection of exploratory data analysis, machine-learning, statistics, and Python programming work. The projects are organized by the subject they explore rather than by the course or assignment number.

## Contents

### Data science notebooks

The notebooks in [`data_science/notebooks`](data_science/notebooks) cover:

- Python data structures, Iris data, Wavefront OBJ point clouds, and classes
- NumPy vectorization, array axes, dot products, and matrix multiplication
- pandas Series/DataFrames, indexing, sorting, aggregation, and missing values
- Matplotlib/seaborn visualization, scatter plots, and box plots
- Cereal nutrition and ratings
- College football data wrangling and conference comparisons
- Probability, expected value, variance, and Monte Carlo simulation
- Linear regression trained with gradient descent
- K-means clustering implemented from scratch
- scikit-learn clustering, dimensionality reduction, and k-nearest neighbors
- Text feature extraction and classification with scikit-learn
- Linear regression on synthetic and California housing data
- A small `statsmodels` ordinary-least-squares reference notebook

Supporting data and original rubric documents are in [`data_science/data`](data_science/data) and [`data_science/reference`](data_science/reference).

### Python exercises

The [`python`](python) directory contains focused command-line exercises:

- [`environment-setup`](python/environment-setup): Python environment and IDE setup
- [`word-counting`](python/word-counting): punctuation-aware word frequencies written to JSON
- [`cube-sums`](python/cube-sums): sums of cubes selected by their leading digit
- [`mean-and-variance`](python/mean-and-variance): empirical mean and population variance
- [`reverse-strings`](python/reverse-strings): reverse the characters in a string
- [`palindrome-numbers`](python/palindrome-numbers): test whether an integer reads the same backward
- [`text-feature-matrix`](python/text-feature-matrix): build a document-term count matrix

Each project keeps its explanation, implementation, examples, and any supporting assets together.

### Star-data analysis

[`star-data-analysis`](star-data-analysis) contains an exploratory notebook and data set for examining stellar temperatures, luminosities, radii, magnitudes, colors, spectral classes, and star types.

## Running the work

The notebooks are standard Jupyter notebooks and can be opened with JupyterLab, Jupyter Notebook, or Google Colab. Some notebooks download public data at runtime; others use the local files documented beside them. The Python exercises use ordinary command-line arguments shown in their project documentation.

The exact package versions are not pinned, so a modern Python environment with NumPy, pandas, Matplotlib, seaborn, statsmodels, and scikit-learn may be needed depending on the project.
