#!/usr/bin/env python
"""
Fit Model application file.

1. Read in an already cleaned CSV
2. Convert it to a Dataframe.
3. Apply encoding.
4. Standardize the data.
5. Fit an Ordinary Least Squares model.
6. Show the model stats.

The model is fitted using X dimensions as numeric values, time and categorical
variables (encoded as numeric values). Text values are ignored. On the fitted
model, each factor has a coefficient, which helps determine the strength and
direction of the factor's influence on the mood score.

# TODO Get coeff and print that and not other fields.
# Can I apply to 5 point scale?
Years and months have over 1 - is the range not -1 to 1 correlation?
"""
import pandas as pd
import statsmodels.api

from lib.config import AppConf
conf = AppConf()


def prepare_data(df):
    """Prepare data for model fitting.

    Expect cleaned Daylio data as DataFrame, remove unneccessary columns, apply
    one-hot encoding to split certain variables into numeric columns (removing
    the base column of 0 to prevent any collinearity issues), then return as a
    Dataframe.

    Note that year could be kept as a single numeric column, but then it needs
    scaling applied and then reverse scaling to intrept the model stats for
    year. Therefore for simplicity, unique year values are split into one-hot
    encoded columns, as with week and month.

    @param df: Dataframe of cleaned input data.

    @return df: Dataframe of encoded data.
    """
    # Remove time and text columns which are not needed for training.
    df.drop(
        ['timestamp', 'date', 'weekday_label', 'mood_label', 'note', ],
        axis=1,
        inplace=True
    )
    df['datetime'] = pd.to_datetime(df.datetime)
    df.set_index(
        'datetime',
        inplace=True,
        verify_integrity=True
    )
    # TODO Why is month 1 missing across years?
    df['month_num'] = df.index.month
    df['year'] = df.index.year

    encoded_weekdays = pd.get_dummies(
        df['weekday_num'],
        prefix='weekday',
        drop_first=True
    )
    encoded_months = pd.get_dummies(
        df['month_num'],
        prefix='month',
        drop_first=True
    )
    encoded_years = pd.get_dummies(
        df['year'],
        prefix='year',
        drop_first=True
    )

    df[list(encoded_weekdays.columns)] = encoded_weekdays
    df[list(encoded_months.columns)] = encoded_months
    df[list(encoded_years.columns)] = encoded_years

    df.drop(
        ['weekday_num', 'month_num', 'year'],
        axis=1,
        inplace=True
    )

    return df


def fit(csv_in_path):
    """Fit an Ordinary Least Squares model to input Daylio data and return it.

    @param csv_in_path: Path to cleaned CSV.

    @return: None.
    """
    df = pd.read_csv(csv_in_path)

    encoded_df = prepare_data(df)

    y = encoded_df['mood_score']
    X = encoded_df.drop(
        ['mood_score'],
        axis=1,
    )
    return statsmodels.api.OLS(y, X).fit()


def main():
    """Main command-line function.

    TODO: Use argparse to read in a custom value rather than use the default.
    """
    csv_in_path = conf.get('data', 'cleaned_csv')
    model = fit(csv_in_path)

    # Note the signs and sizes of the co-efficients.
    print(model.summary())


if __name__ == '__main__':
    main()
