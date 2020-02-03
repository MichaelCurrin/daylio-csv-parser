# Installation

## Project requirements

- _Python_ 3.5+
- _SQLite3_ (optional)

## Install OS-level dependencies

**Ubuntu/Debian**

If you intend to create a SQLite database file from you data, ensure you install/upgrade SQLite.


```bash
$ sudo apt-get update
$ sudo apt-get install libsqlite3-dev
$ sudo apt-get update sqlite3
```

## Install project dependencies

It is usually best-practice in _Python_ projects to install into a sandboxed _virtual environment_, This will be locked to a specific Python version and contain only the _Python_ libraries that you install into it, so that your _Python_ projects do not get affected.

Follow this guide to [Setup a Python 3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).

You can then continue to the [Usage](/docs/usage.md) doc.
