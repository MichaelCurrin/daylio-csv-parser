# Usage Instructions

If you have followed the [Installation Instructions](installation.md) and have Daylio's Premium mode activated, you may continue with the usage instructions here.

The main aim of this project is to expand make the Daylio export CSV easier to use, by transforming the data. In particular, the _activities_ column is split out and this application has been set to work on any number activities. Though, the moods for now are restricted to 5.


## Clean a CSV

### 1. Create the data

First, create a `daylio_export.csv` file on your mobile device. This should contain all records, from the first one up to the most recent.

Sample input CSV.

```
year,date,weekday,time,mood,activities,note
2018,18 May,Friday,11:54 pm,happy,"clean | cook | music","Went to a party"
2018,17 May,Wednesday,10:21 pm,average,"cook | stressed ",""
2018,16 May,Tuesday,11:41 pm,horrible,"","Did nothing today."
```

This CSV always has 7 columns. However, the _activities_ value needs further processing to make it easy handle in a CSV editor. Each activity is separated by a pipe symbol and there may be no activities an empty string, or all the available activities may be used. The activities may be a mixture of the built-in labels and the ones defined by a user.

Next, move the CSV form your mobile device to your computer. The simplest is to use a USB cable and plug your device in. Though, you might want to use Google Drive or e-mail.


### 2. Create a clean CSV

Move the CSV to dayliopy's default configured location.

```bash
$ mv daylio_export.csv path/to/repo/dayliopy/var/data_in/daylio_export.csv
```

Read in the above file, clean the data and write out to the default configured location.

```bash
$ cd path/to/repo/dayliopy
$ source ../venv/bin/activate
$ (venv) python clean_csv.py
Reading CSV: /home/.../.../daylio-csv-parser/dayliopy/var/data_in/daylio_export.csv
Replacing activities column with multiple activity columns
Writing cleaned CV to: /home/.../.../daylio-csv-parser/dayliopy/var/data_out/cleaned.csv
```

Example values for a row of the output CSV:

| timestamp | datetime | date | weekday_label | weekday_num | mood_label | mood_score | clean | cook | music | stressed | note |
|--------------|---------------------|------------|---------------|-------------|------------|------------|-------|------|-------|-----------------------|-----------------|
| 1522444920.0 | 2018-03-30 23:22:00 | 2018-03-30 | Friday | 4 | average | 3 | 1 | 0 | 0 | 1 | Did a roadtrip. |
| 1522360440.0 | 2018-03-29 23:54:00 | 2018-03-29 | Thursday | 3 | happy | 4 | 0 | 1 | 0 | 0 |  |

_Formatted using [markdown table tool](https://www.tablesgenerator.com/markdown_tables)._

You can now open the cleaned CSV in a CSV editor and start using it. If you want to get the data into a database or want to fit a stats model to your data, follow the instructions in the sections below.


## Database

### 1. Create

This step requies a cleaned CSV created in the above section.

Use SQLite to create a database and a new table called _daylio_.

```bash
$ cd path/to/repo/dayliopy
$ # Create new empty db file if none exists. Use the project's setup script
  # to import from the default cleaned CSV file location.
$ sqlite3 var/data_out/db.sqlite < ../tools/setup_db.sql
$ sqlite3 var/data_out/db.sqlite '.schema'
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
sqlite> .quit
```

SQLite's default behaviour it to set the affinity for each column to TEXT (see [Datatypes in SQLite Version 3](https://www.sqlite.org/datatype3.html)). Numeric calculations may still be done as if the columns were numeric. You may change the column types if you wish, by altering the table, or by creating a table with the same name manually _before_ doing the import.


### 2. Use

#### Query using SQLite interactive mode.

```bash
$ sqlite3 var/data_out/db.sqlite
sqlite> -- The default most is csv, which is not pretty.
sqlite> .mode columns
sqlite> .headers on
sqlite> SELECT ROUND(AVG(mood_score), 2) AS avg_mood, SUM(cook) AS sum_cook FROM daylio;
avg_mood    sum_cook
----------  ----------
3.27        58
sqlite> .quit
```

#### Query using bash terminal.

```bash
$ sqlite3 var/data_out/db.sqlite -header -column 'SELECT mood_label, date FROM daylio LIMIT 5;'
mood_label  date
----------  ----------
happy       2018-03-30
happy       2018-03-29
average     2018-03-28
happy       2018-03-27
average     2018-03-26
```

#### Use queries to create CSV reports.

```bash
$ sqlite3 var/data_out/db.sqlite -header -csv \
    'SELECT mood_label, date FROM daylio LIMIT 5;' > path/to/report.csv
```


## Fit a stats model

The [fit_model.py](/dayiopy/fit_model.py) script performs the following steps:

1. Read in the cleaned CSV.
2. Run Ordinary Least Squares model.
3. Print model stats to better under factors influencing mood.

```bash
$ (venv) python fit_model.py
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
```

