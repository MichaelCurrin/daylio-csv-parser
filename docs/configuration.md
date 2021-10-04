
# Configuration

This project uses Python's built-in [ConfigParser](https://docs.python.org/3/library/configparser.html) format, which is easy for end-users to edit.

The [clean_csv.py](/dayiopy/clean_csv.py) script will dynamically handle any number of activities in the _activities_ column without any configuration needed. However, the labels for moods should be configured, as below. Also, you may optionally override any paths for CSV and db files.

View the built-in [app.conf](/dayliopy/etc/app.conf) config file to see what options can be set.

```bash
$ view dayliopy/etc/app.conf
```

Create an unversioned local config file, to override fields in `app.conf`.

```sh
$ nano dayliopy/etc/app.local.conf
```

Or use the template as a starting point:

```sh
$ cp dayliopy/etc/app.template.conf dayliopy/etc/app.local.conf
```

Even though the _Daylio_ mobile app does allow more, a maximum of 5 mood levels is allowed in this application. Any others will raise an error.

You must set the moods in the `[daylio]` section to exact match the labels in your CSV.

e.g. the configured default for `mood3` is `meh`, based on Daylio default. But if you configured Daylio to use `happy` for `mood3`, then you must also set that in `app.local.conf`.
