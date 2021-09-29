# Daylio CSV Parser
> Improve the usability of the Daylio CSV export and explore reports around your data

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/daylio-csv-parser?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/daylio-csv-parser/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![Made with SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)


## About

What is Daylio? Read in this [doc](/docs/what_is_daylio.md).

This _dayliopy_ application parses a CSV exported from _Daylio_ (in premium mode) to create a more useful CSV.

In particular, the _activities_ column with multiple activities listed in a single cell is split out into multiple columns, with appropriate names and values as `0` or `1`.

For interest, see related mood tracking projects by other developers [here](/docs/related_projects.md).


## Sample usage

A summary of the command-line API is covered below.

### Main feature

Run the main script to read CSV exported from _Daylio_ at a configured location and create a clean CSV.

```bash
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

[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](/docs/ "Go to docs")

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
