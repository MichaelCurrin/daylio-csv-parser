# Daylio CSV Parser ☺️ 📆 🐍
> Improve the usability of the Daylio CSV export and explore reports around your data

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/daylio-csv-parser?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/daylio-csv-parser/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![Made with SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![dependency - statsmodels](https://img.shields.io/badge/dependency-statsmodels-blue)](https://pypi.org/project/statsmodels)
[![dependency - pandas](https://img.shields.io/badge/dependency-pandas-blue)](https://pypi.org/project/pandas)


This Python 3 CLI took will convert a Daylio CSV export into a more usable CSV and a SQLite database.


## About Daylio CSV

What is Daylio? Read on this [doc](https://michaelcurrin.github.io/daylio-csv-parser/what-is-daylio.html) page.

This _daylio-csv-parser_ application parses a CSV exported from _Daylio_ (in premium mode) to create a more useful CSV.

In particular, the _activities_ column with multiple activities listed in a single cell is split out into multiple columns, with appropriate names and values as `0` or `1`.


## Sample usage

A summary of the command-line API is covered below.

### Main feature

Run the main script to read CSV exported from _Daylio_ at a configured location and create a clean CSV.

```sh
$ make csv
```

### Other features

Assuming you have created a clean CSV using the step above, you can run any of these commands if you wish to. The order does not matter.

#### Database

Create a database file from the cleaned CSV. You can then access data in the database.

```sh
$ make db
```

#### Aggregate mood report

View a report around mood score aggregate stats.

```sh
$ ./mood_report.py
```

#### Regression report

View a report on a stats model which was fitted your data.

```sh
$ ./fit_model.py
```


## Documentation

<div align="center">

[![view - Online docs](https://img.shields.io/badge/view-Online_docs-blue?style=for-the-badge)](https://michaelcurrin.github.io/daylio-csv-parser/ "Go to docs site")

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
