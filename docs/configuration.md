# Configuration


## Config files 

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


## Configuring moods

The Daylio app lets you override the labels for moods, which then appears in your export.

If you do that, you need to configure this Dayliopy tool to know which level from 1 to 5 corresponds to that label.

So set the moods in the `[daylio]` section to exactly match the labels in your CSV. You only need to set values in the local config if they differ from the base config.

### Basic

You could replace mood level 3 from "meh" default in Daylio with "average".

```ini
[daylio]
mood3: average 
```

### Multiple moods

If you use more than 5 moods and want to map multiple labels for the same level, you can configure this in the config too.

```ini
mood5: amazing
mood4: good, refreshed
mood3: ok, ok but sleepy
mood2: sad, bad, anxious
mood1: horrible
```

Note use of comma and optional space to separate values.

NB. Make sure in the Daylio app to take out any commas from the mood label, to avoid issues here.
