# Installation


## Install system dependencies

### Python

Python 3.6 or above.

**Debian/Ubuntu**

```bash
$ sudo apt-get install python3
```

**Mac OS X**

```bash
$ brew install python
```

### SQLite

If you intend to create a SQLite database file from you data, ensure you install SQLite if it not builtin.

**Debian/Ubuntu**

```bash
$ sudo apt-get update
$ sudo apt-get install libsqlite3-dev
$ sudo apt-get update sqlite3
```

**Mac OS X**

```bash
$ brew install sqlite3
```

## Clone

```bash
$ git clone git@github.com:MichaelCurrin/daylio-csv-parser.git
```


## Install project dependencies

It is usually best-practice in _Python_ projects to install into a sandboxed _virtual environment_, This will be locked to a specific Python version and contain only the _Python_ libraries that you install into it, so that your _Python_ projects do not get affected.

See can see this guide on how to [Setup a Python 3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7) if you want to install/upgrade Python or want to understand more about virtual environments. Otherwise continue below.

Create virtual environment:

```bash
$ cd <PATH_TO_REPO>
$ python3 -m venv venv
$ source venv/bin/activate
```

Install packages:

```bash
$ make install
```

You can now continue to the [Usage](/docs/usage.md) doc.
