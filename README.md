# Daylio CSV Parser
_Convert a Daylio CSV export into a more usable CSV and a SQLite database._


## What is Daylio?

Daylio is mobile app and their [website](https://daylio.webflow.io/) says:

>"Daylio enables you to keep a private diary without having to write a single line".

Entries are created at a specific date and time and may have the following attributes:

- **Mood:** Choose a value from radio button selection of face icons. These follow a 5-point high to low scale and may be relabelled within the mobile app.
- **Activities:** Tick checkboxes for your custom set of activities. These are only recorded as boolean values, not as counts (though could later be aggregated for a day, week, etc). They can each have custom icon and label and additional activities can be added. An activity might be what you did or how you felt physically/emotionally that day.
- **Note:** An optional text note.

For a guide on using the app, see the [Daylio quick tips](https://medium.com/@helpfuldad/heres-how-i-m-using-the-daylio-app-to-ensure-my-life-is-in-balance-i-m-on-372-days-and-counting-336b960a34ee) post.


## Features

This [dayliopy]() Python application provides to two services.

1. CSV cleaning
    1. Read a Daylio CSV (Premium mode is required to export it).
    2. Clean it.
    3. Write out a new CSV.
2. Read the new CSV into a SQLite3 database.

Those two services may be run separately. The resulting CSV and database files are intended to be a format which is much easier to work with than the standard export.


## Documentation

- [Installation instructions](docs/installation.md).
- [Usage instructions](docs/usage.md)


## Other projects

Below are Github repos based around Daylio, which are worth checking out:

- Python
    * [daylio-visualisations](https://github.com/pajowu/daylio-visualisations)
    * [daylio2yearinpixels](https://github.com/pwcazenave/daylio2yearinpixels)
- C#
    * [CleanDaylioExport](https://github.com/ecsplendid/CleanDaylioExport)
- C++
    * [daylio-stats](https://github.com/xdmtk/daylio-stats)
- Other
    * [Quantified Self](https://github.com/woop/awesome-quantified-self) is a curated list of resources for various tools in the diary area.

Any contributions to the above list are welcome.
