# Daylio CSV Parser
_Convert a Daylio CSV export into a more usable CSV and a SQLite database._


## What is Daylio?

[Daylio](https://daylio.webflow.io/) is a mobile app which works as visual diary or journal. It allows one to keep a history of daily activities and moods. 

For a single entry at a date and time, the following can be stored in the app.

- A _mood_ selection. By default, on 5-point scale from low to high with labels. Labels may be changed and additional moods may be added. TODO: Check the default labels.
- Checkboxes for all user-defined _activities_. These are only recorded as boolean values, not as counts (though could later be aggregated for a day, week, etc). They can each have custom icon and label and additional activities can be added. An activity might be what you did or how you felt physically/emotionally that day.
- A text _note_. This may be left blank.

## Features

This [dayliopy]() Python application provides to two services.

1. CSV cleaning
    1. Read a Daylio CSV (Premium mode is required to export it).
    2. Clean it.
    3. Write out a new CSV.
2. Read new CSV into a SQLite3 database.

Those two services may be run separately. The resulting CSV and database files are intended to be a format which is much easier to work with than the standard export.


## Documentation

- [Installation instructions](docs/installation.md).
- [Usage instructions](docs/usage.md)


## Other projects

Below are Github repos based around Daylio, which are worth checking out:

- [daylio-visualisations](https://github.com/pajowu/daylio-visualisations) in Python
- [daylio2yearinpixels](https://github.com/pwcazenave/daylio2yearinpixels) in Python 
- [CleanDaylioExport](https://github.com/ecsplendid/CleanDaylioExport) in C#
- [daylio-stats](https://github.com/xdmtk/daylio-stats) in C++

Also, see the curated list of [Quantified Self](https://github.com/woop/awesome-quantified-self) resources.
