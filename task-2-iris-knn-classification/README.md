# Iris Flower Classification with KNN

Project 2 of the DecodeLabs AI Engineering Internship (2026 Batch).

This notebook classifies Iris flowers into three species using the **K-Nearest Neighbors (KNN)** algorithm.

## Dataset

The model uses four features to predict the species:

- Sepal length
- Sepal width
- Petal length
- Petal width

The three species are *Iris setosa*, *Iris versicolor* and *Iris virginica*.

## Tech stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn

## How it works

KNN is a supervised learning algorithm. It classifies a point by looking at the classes of its nearest neighbours. The notebook:

1. Loads the Iris dataset.
2. Separates the features from the labels.
3. Splits the data into training and test sets.
4. Standardises the features.
5. Trains a KNN classifier.
6. Predicts the species for the test data.
7. Evaluates the model.

## Results

The model is evaluated with:

- an accuracy score,
- a classification report,
- a confusion matrix.

The graphs and outputs are in [`screenshots/`](screenshots/).

## Files

| File | Purpose |
|---|---|
| `iris_knn_classification.ipynb` | The full notebook: code, graphs and results |
| `screenshots/` | Graphs and code output |

## Running it

Open the notebook in Jupyter or Google Colab and run all cells:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook iris_knn_classification.ipynb
```

## Author

Khadija Jawad, AI Engineering Intern, DecodeLabs (2026 Batch)
