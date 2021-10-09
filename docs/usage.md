# Usage

If you have followed the [Installation Instructions](installation.md) and have the **Daylio premium mode** activated, you may continue with the usage instructions here.

This doc assumes you have activate the virtual environment and are in the app directory

```bash
$ cd PATH_TO_REPO
$ source venv/bin/activate
```

## Parse a CSV

This section covers the main feature of this project. The later features require this _Clean a CSV_ sections steps to be completed first.

### 1. Export your data

Export the data on your mobile device.

1. Open the Daylio app.
1. Tap _More_.
1. Tap _Export Entries_.
1. Select a download option such as e-mail, Google Drive or Dropbox.

You will now have a file named `daylio_export.csv` which contains all your entries from the most recent back to the first. See [CSV format](/docs/csv-format.md) for more info.

Download the file on your computer and then move CSV to _dayliopy's_ configured CSV input location.

```sh
$ mv daylio_export.csv PATH_TO_REPO/dayliopy/var/data_in/daylio_export.csv
```

### 2. Import the data

Use the commands below to read in the above export file, clean the data and write out a new CSV to the configured location.

Note that this will overwrite the existing output file. This should be fine though, since the input file always contains all data to date.

```sh
$ make csv
```
    python -m dayliopy.clean_csv
    Reading CSV: /Users/mcurrin/repos/daylio-csv-parser/dayliopy/var/data_in/daylio_export.csv
    Replacing the activities column with multiple activity columns
    Writing cleaned CSV to: /Users/mcurrin/repos/daylio-csv-parser/dayliopy/var/data_out/cleaned.csv

Example values for a row of the output CSV:

| timestamp    | datetime            | date       | weekday_label | weekday_num | mood_label | mood_score | clean | cook | music | stressed | note            |
| ------------ | ------------------- | ---------- | ------------- | ----------- | ---------- | ---------- | ----- | ---- | ----- | -------- | --------------- |
| 1522444920.0 | 2018-03-30 23:22:00 | 2018-03-30 | Friday        | 4           | average    | 3          | 1     | 0    | 0     | 1        | Did a roadtrip. |
| 1522360440.0 | 2018-03-29 23:54:00 | 2018-03-29 | Thursday      | 3           | happy      | 4          | 0     | 1    | 0     | 0        |                 |

_Formatted using [markdown table tool](https://www.tablesgenerator.com/markdown_tables)._

You can now open the cleaned CSV in a CSV editor and start using it. If you want to get the data into a database or want to fit a stats model to your data, follow the instructions in the sections below.


## Mood report

```sh
$ make mood
```

    python -m dayliopy.mood_report
    mood_score
    mean: 3.28
    median: 3.00

    average     926
    happy       781
    sad         269
    amazing      84
    horrible     49
    Name: mood_label, dtype: int64


## Fit a stats model

The [fit_model.py](/dayiopy/fit_model.py) script performs the following steps:

1. Read in the cleaned CSV.
1. Fit Ordinary Least Squares model using the data.
1. Print model stats, to better under factors influencing mood.

```bash
$ make fit
```

                                OLS Regression Results
    ==============================================================================
    Dep. Variable:             mood_score   R-squared:                       0.955
    ...
    ...
    ==============================================================================================
                                    coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------------------
    cook                           0.5807      0.104      5.581      0.000       0.376       0.785
    clean                          0.3392      0.131      2.597      0.010       0.083       0.596
    music                          0.2331      0.096      2.432      0.015       0.045       0.421
    ...
    weekday_1                      0.5355      0.111      4.840      0.000       0.318       0.753
    weekday_2                      0.7794      0.107      7.316      0.000       0.570       0.989
    ...
    weekday_6                      0.5772      0.125      4.622      0.000       0.332       0.822
    month_2                        0.6454      0.132      4.889      0.000       0.386       0.905
    month_3                        0.9950      0.123      8.068      0.000       0.753       1.237
    ...
    month_12                       1.5238      0.126     12.083      0.000       1.276       1.771
    year_2017                      0.6669      0.079      8.465      0.000       0.512       0.822
    year_2018                      1.4733      0.129     11.451      0.000       1.221       1.726
    ==============================================================================
    Omnibus:                        6.218   Durbin-Watson:                   1.591
    Prob(Omnibus):                  0.045   Jarque-Bera (JB):                6.075
    Skew:                           0.206   Prob(JB):                       0.0480
    Kurtosis:                       3.166   Cond. No.                         20.0
    ==============================================================================


## Development

```bash
$ pylint *
```



## Database

Make sure to follow the clean CSV section above otherwise this section will not work.

### 1. Create

Use SQLite to create a database and a new table called _daylio_.

```sh
$ cd PATH_TO_REPO
```

Create new empty DB file if none exists. Use the project's set up script
to import from the default cleaned CSV file location.

```sh
$ make db
```

View the schema:

```console
$ make schema
CREATE TABLE daylio(
  "timestamp" TEXT,
  "datetime" TEXT,
  "date" TEXT,
  "weekday_label" TEXT,
  "weekday_num" TEXT,
  "mood_label" TEXT,
  "mood_score" TEXT,
  "cook" TEXT,
  "clean" TEXT,
  "music" TEXT,
  "stressed" TEXT,
  "note" TEXT
);
```

SQLite's default behavior it to set the affinity for each column to `TEXT` - see [Datatypes in SQLite Version 3](https://www.sqlite.org/datatype3.html).

Numeric calculations may still be done as if the columns were numeric. You may change the column types if you wish, by altering the table, or by creating a table with the same name manually _before_ doing the import.

### 2. Use

#### Query using SQLite interactive mode.

```sh
$ make interactive
```

    sqlite> -- The default most is csv, which is not pretty.
    sqlite> .mode columns
    sqlite> .headers on
    sqlite> SELECT ROUND(AVG(mood_score), 2) AS avg_mood, SUM(cook) AS sum_cook FROM daylio;
    avg_mood    sum_cook
    ----------  ----------
    3.27        58
    sqlite> .quit

#### Query using bash terminal.

```sh
$ cd dayliopy
$ sqlite3 var/data_out/db.sqlite -header -column \
    'SELECT mood_label, date FROM daylio LIMIT 5;'
```

    mood_label  date
    ----------  ----------
    happy       2018-03-30
    happy       2018-03-29
    average     2018-03-28
    happy       2018-03-27
    average     2018-03-26

#### Use ad hoc queries to create CSV reports

```bash
$ sqlite3 var/data_out/db.sqlite -header -csv \
    'SELECT mood_label, date FROM daylio LIMIT 5;' \
    > path/to/report.csv
```
