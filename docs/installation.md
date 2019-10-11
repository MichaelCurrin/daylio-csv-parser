# Installation

## Project requirements

- Python 3.5 or above is recommended.
- SQLite3 (optional)

## Install OS-level dependencies

**Ubuntu/Debian**

If you intend to create a SQLite database file from you data, ensure you install/upgrade SQLite.


```bash
$ sudo apt-get update
$ sudo apt-get install libsqlite3-dev
$ sudo apt-get update sqlite3
```

## Install project dependencies

It is usually best-practice in Python projects to install into a sandboxed _virtual environment_, which is set to a specific Python version and contains on the packages you install into it so that your Python projects do not get affected.

Follow this guide to [Setup a Python 3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).

You can then continue to the [Usage](/docs/usage.md) doc.
