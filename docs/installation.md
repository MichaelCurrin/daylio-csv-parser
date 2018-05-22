# Installation Instructions

How to setup the project on a Linux system.


## OS dependencies

Python 3.5 or above is recommended.

```bash
$ sudo apt-get install python3 virtualenv git
```

If you intend to create a SQLite database file from you data, ensure you install SQLite.

```bash
$ sudo apt-get install sqlite3
```


## Python environment

```bash
$ git clone git@github.com:MichaelCurrin/daylio-csv-parser.git
$ cd daylio-csv-parser
$ virtualenv venv -p python3
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Now you can continue to the [Usage Instructions](usage.md).
