# Daylio Analysis Tool
Process personal data exported from the [Daylio](https://daylio.webflow.io/) app for analysis and reporting.


## Context

[Daylio](https://daylio.webflow.io/) is a mobile app which works as visual diary or journal. It allows one to keep a history of daily activities and moods. Any number of activities can be recorded as binary Yes/No values for that entry, with a custom icon and label. A single mood for the entry is recorded on 5-point scale from low to high. A text note is optional.

This repo's [dayliopy]() application is for users of the Daylio diary app who want to go beyond the app's own built-in reporting to seek a better understanding of one's experiences and emotions. The aim of this project is to use analysis and reporting to improve self-awareness and provide to insights which can drive actions.


## Documention

Note that a `daylio_export.csv` file exported from Daylio is required to use this application. Therefore it is highly recommended to unlock Daylio's _Premium_ mode first.

- [Installation instructions](docs/installation.md).
- [Usage instructions](docs/usage.md)


## Features

The cleaning component can be run independently to read a Daylio-formatted CSV with any number of columns, clean it and then write out a new file.

### Components

There are several reporting components, with different uses and levels of complexity.

- Terminal reporting. _TO BE COMPLETED_
- Visual reporting. _TBC_
- A dashboard view over various time frames. _TBC_
- Measurement of totals or rates against goals. _TBC_
- Automated alerts based on custom conditions. _TBC_
- Forecasting. _TBC_

### Implementation

The features are implemented with the following processes:

- [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) of the data
    1. Clean input CSV
    2. Write out to a new cleaned CSV.
    3. Read cleaned CSV into a database.
- On-demand reporting
    1. Handle user request.
    2. Fetch data.
    3. Process and report on data.
- Automated reporting and notifications
    1. Run weekly or daily job on schedule.
    2. Check condition is met (otherwise always run).
    3. Send alert
      - e.g. Send request with message to _Maker_, so that _IFTTT_ can trigger a mobile alert
      - e.g. Send text or HTML in e-mail using configured Gmail account.


## Other projects

Below are Github repos based around Daylio, which are worth checking out:

- [daylio-visualisations](https://github.com/pajowu/daylio-visualisations) in Python
- [daylio2yearinpixels](https://github.com/pwcazenave/daylio2yearinpixels) in Python 
- [CleanDaylioExport](https://github.com/ecsplendid/CleanDaylioExport) in C#
- [daylio-stats](https://github.com/xdmtk/daylio-stats) in C++

Also, see the curated list of [Quantified Self](https://github.com/woop/awesome-quantified-self) resources.
