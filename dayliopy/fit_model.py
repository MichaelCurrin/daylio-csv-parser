#!/usr/bin/env python
"""
Fit Model application file.

1. Read in an already cleaned CSV
2. Convert it to a DataFrame.
3. Apply encoding.
4. Standardize the data.
5. Fit an Ordinary Least Squares model.
6. Show the model stats.

The model is fitted using X dimensions as numeric values, time and categorical
variables (encoded as numeric values). Text values are ignored. On the fitted
model, each factor has a coefficient, which helps determine the strength and
direction of the factor's influence on the mood score.
"""
import pandas as pd
import statsmodels.api

from .lib.config import AppConf


conf = AppConf()

# Must be lists and pandas now gives an error on a tuple.
DROP_COLUMNS = ["timestamp", "date", "weekday_label", "mood_label", "note"]
OLD_TIME_COLUMNS = ["weekday_num", "month_num", "year"]


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare data for model fitting.

    Expect cleaned Daylio data as DataFrame, remove unneccessary columns, apply
    one-hot encoding to split certain variables into numeric columns (removing
    the base column of 0 to prevent any collinearity issues), then return as a
    DataFrame.

    Note that year could be kept as a single numeric column, but then it needs
    scaling applied and then reverse scaling to intrept the model stats for
    year. Therefore for simplicity, unique year values are split into one-hot
    encoded columns, as with week and month.

    e.g. weekday_1, weekday_7, month_1, month_12

    We no longer set `verify_integrity=False` on the datetime index, as this
    causes errors in the unlikely case that someone sets two records for the
    same time. Which is okay as we only use the index for month and year.
    See issue #25.

    :param df: Cleaned input data.

    :return df: Encoded data.
    """
    # Remove columns that are not needed for training.
    df.drop(DROP_COLUMNS, axis="columns", inplace=True)

    df["datetime"] = pd.to_datetime(df.datetime)

    df.set_index("datetime", inplace=True)
    df["month_num"] = df.index.month
    df["year"] = df.index.year

    encoded_weekdays = pd.get_dummies(
        df["weekday_num"], prefix="weekday", drop_first=True
    )
    encoded_months = pd.get_dummies(df["month_num"], prefix="month", drop_first=True)
    encoded_years = pd.get_dummies(df["year"], prefix="year", drop_first=True)

    weekday_col_names = list(encoded_weekdays.columns)
    month_col_names = list(encoded_months.columns)
    year_col_names = list(encoded_years.columns)

    df[month_col_names] = encoded_months
    df[weekday_col_names] = encoded_weekdays
    df[year_col_names] = encoded_years

    df.drop(OLD_TIME_COLUMNS, axis="columns", inplace=True)

    return df


def fit_model_to_csv(csv_in_path: str):
    """
    Fit an Ordinary Least Squares model to input Daylio data and return it.

    :param csv_in_path: Path to cleaned CSV.
    """
    df = pd.read_csv(csv_in_path)

    encoded_df = prepare_data(df)

    y = encoded_df["mood_score"]
    X = encoded_df.drop(
        ["mood_score"],
        axis="columns",
    )

    model = statsmodels.api.OLS(y, X)

    return model.fit()


def main() -> None:
    """
    Command-line entry-point.
    """
    csv_in_path = conf.get("data", "cleaned_csv")
    model = fit_model_to_csv(csv_in_path)

    # Note the signs and sizes of the co-efficients.
    print(model.summary())


if __name__ == "__main__":
    main()
