# Daylio CSV Parser
>Improve the usability of the Daylio CSV export and explore reports around your data.

What is [Daylio](docs/what_is_daylio.md)?

This _dayliopy_ application parses a CSV exported from _Daylio_ (in premium mode) to create a more useful CSV. In particular, the _activities_ column with multiple activities listed in a single cell is split out into multiple columns, with appropriate names and values as `0` or `1`.

For interest, see related mood tracking projects by other developers [here](docs/related_projects.md).

## Installation

See the [Installation Instructions](docs/installation.md) doc.

## Usage example

A summary of the command-line API is covered below (assuming that you are in the app directory with an activated environment). See [Usage Instructions](docs/usage.md) doc for more detailed steps.

### Main feature

Run the main script to read CSV exported from _Daylio_ at a configured location and create a clean CSV.

```bash
$ ./clean_csv.py
```

### Other features

Assuming you have created a clean CSV using the step above, you can run any of these commands if you wish to. The order does not matter.

#### Database

Create a database file from the cleaned CSV. You can then access data in the database.

```bash
$ sqlite3 var/data_out/db.sqlite < ../tools/setup_db.sql
```

#### Aggregate mood report

View a report around mood score aggregate stats.

```bash
$ ./mood_report.py
```

#### Regression report

View a report on a stats model which was fitted your data.

```bash
$ ./fit_model.py
```

## License

Distributed under the MIT license. See [LICENSE](LICENSE) for more information.
