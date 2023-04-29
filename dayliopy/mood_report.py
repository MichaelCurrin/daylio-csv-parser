#!/usr/bin/env python
"""
Mood report application file.
"""
import pandas as pd

from .lib import CSV_ENCODING
from .lib.config import AppConf


conf = AppConf()


def print_aggregate_stats(df: pd.DataFrame, column_name: str) -> None:
    """
    Print aggregate stats for a given DataFrame and column name.

    :param df: Data to work on.
    :param column_name: Name of column to use in `df`. Also used to print a
    heading.
    """
    print(column_name)

    values = df[column_name]
    stats = {
        "mean": values.mean(),
        "median": values.median(),
    }

    for k, v in stats.items():
        print("{k}: {v:3.2f}".format(k=k, v=v))


def get_mood_counts(df: pd.DataFrame):
    """
    Combine configured mood score with actual counts and return.

    :param df: Data that was read in from cleaned CSV.

    :return: DataFrame with index as 'mood_label' and columns as
        ['mood_score', 'count'].
    """
    config_df = pd.DataFrame.from_dict(
        conf.MOODS, orient="index", columns=["mood_score"]
    )
    config_df.sort_values("mood_score", inplace=True)

    return df["mood_label"].value_counts()


def make_report(csv_in_path: str) -> None:
    """
    Make report from input CSV and show.


    :param: csv_in_path: Path to cleaned CSV, as generated by clean_csv.py
        application.

    :return: None
    """
    df = pd.read_csv(
        csv_in_path, usecols=["mood_label", "mood_score"], encoding=CSV_ENCODING
    )

    print_aggregate_stats(df, "mood_score")
    print()
    print(get_mood_counts(df))


def main():
    """
    Command-line entry-point.
    """
    csv_in_path = conf.get("data", "cleaned_csv")

    make_report(csv_in_path)


if __name__ == "__main__":
    main()
