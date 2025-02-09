"""
split_data.py

This script reads a CSV dataset and splits it into K folds using KFold.
For each fold, one part is saved as the validation set and the remaining parts as the training set.
"""

from sklearn.model_selection import KFold
from utils import DEFAULT_LOCATION_DATAS_FOLDER, DEFAULT_LOCATION_DATASET
import argparse
import pandas as pd


DEFAULT_FOLDS = 2
DEFAULT_TRAIN_FILE_NAME = "train.csv"
DEFAULT_VALIDATION_FILE_NAME = "validation.csv"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Split a CSV dataset into training and validation sets."
    )
    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_LOCATION_DATASET,
        help=f"Path to the input CSV file containing the dataset (default: {DEFAULT_LOCATION_DATASET}).",
    )
    parser.add_argument(
        "--folds",
        type=int,
        default=DEFAULT_FOLDS,
        help=f"Number of folds for K-Fold cross-validation (default: {DEFAULT_FOLDS}).",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=DEFAULT_LOCATION_DATAS_FOLDER,
        help=f"Directory to save the output files (default: {DEFAULT_LOCATION_DATAS_FOLDER}).",
    )
    parser.add_argument(
        "--output-validation",
        type=str,
        default=DEFAULT_VALIDATION_FILE_NAME,
        help=f"Name of the validation file (default: {DEFAULT_VALIDATION_FILE_NAME}).",
    )
    parser.add_argument(
        "--output-train",
        type=str,
        default=DEFAULT_TRAIN_FILE_NAME,
        help=f"Name of the training file (default: {DEFAULT_TRAIN_FILE_NAME}).",
    )

    return parser.parse_args()


def main():
    try:
        args = parse_args()

        # TODO - Verify if there is no problem with the dataset
        # TODO Read the dataset
        # TODO Split the dataset

    #     try:
    #         df = pd.read_csv(args.input)
    #     except Exception as e:
    #         print(f"Error reading {args.input}: {e}")
    #         return

    #     for train_index, val_index in KFold(
    #         n_splits=args.folds, shuffle=True, random_state=42
    #     ).split(df):
    #         train_df = df.iloc[train_index]
    #         val_df = df.iloc[val_index]

    except Exception as e:
        print(f"Error splitting data: {e}")


if __name__ == "__main__":
    main()
