# Daylio CSV Parser
>Improve the usability of the Daylio CSV export and explore reports around your data.

[What is Daylio?](docs/what_is_daylio.md)

Daylio's standard export is limited, so the main feature of this application is to handle that file. In particular, it splits out values in the _activities_ column into multiple activity columns.


## Installation

See the [Installation Instructions](docs/installation.md) doc for more detail.

```bash
$ git clone git@github.com:MichaelCurrin/daylio-csv-parser.git
```

## Usage example

See [Usage Instructions](docs/usage.md) doc for more detailed steps.

### Main feature

Create a clean CSV using a CSV exported from Daylio (in premium mode).

```bash
$ cd dayliopy
$ python clean_csv.py
```

### Other features

These may be run independently, but all require the output from the main feature above.

Create a database file from the cleaned CSV.

```bash
$ sqlite3 var/data_out/db.sqlite < ../tools/setup_db.sql
```

View a report around mood score aggregate stats.

```bash
$ python mood_report.py
```

View a report on a stats model fitted your data.

```bash
$ python fit_model.py
```

## Meta

Michael Currin - [@michaelcurrin](https://twitter.com/michaelcurrin)

Distributed under the MIT licence. See [LICENSE](LICENSE) for more information.

See related projects by other developers [here](docs/related_projects.md).


