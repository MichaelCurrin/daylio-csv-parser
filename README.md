# Daylio CSV Parser
>Improve the usability of the Daylio CSV export and explore reports around your data.

[What is Daylio?](docs/what_is_daylio.md)

This _dayliopy_ application parses a CSV exported from Daylio (in premium mode) to create a more useful CSV. In particular, the _activities_ column with multiple activities listed in a single cell is split out into multiple columns, with appropriate names and values as `0` or `1`.


## Installation

See the [Installation Instructions](docs/installation.md) doc.

## Usage example

See [Usage Instructions](docs/usage.md) doc for more detailed steps.

### Main feature

Run the main script to read CSV exported from _Daylio_ at a configured location and create a clean CSV.

```bash
$ cd dayliopy
$ ./clean_csv.py
```

### Other features

These commands may be run independently, but all require the output from the main feature above.

Create a database file from the cleaned CSV.

```bash
$ sqlite3 var/data_out/db.sqlite < ../tools/setup_db.sql
```

View a report around mood score aggregate stats.

```bash
$ ./mood_report.py
```

View a report on a stats model fitted your data.

```bash
$ ./fit_model.py
```

## Meta

Distributed under the MIT license. See [LICENSE](LICENSE) for more information.

See related projects by other developers [here](docs/related_projects.md).
