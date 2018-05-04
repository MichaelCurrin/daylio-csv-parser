# Daylio Analysis Tool
Process personal data exported from the [Daylio](https://daylio.webflow.io/) app for analysis and reporting.

## Context

[Daylio](https://daylio.webflow.io/) is a mobile app which works as visual diary or journal. It allows one to keep a history of daily activities and moods. Any number of activities can be recorded as binary Yes/No values for that entry, with a custom icon and label. A single mood for the entry is recorded on 5-point scale from low to high. A text note is optional.

This [dayliopy]() application is for users of the Daylio diary app who want to go beyond the app's own built-in reporting to seek a better understanding of one's experiences and emotions. Users of this application need to have Daylio Premium unlocked in order to export the `daylio_export.csv` file. There are existing Python projects around Daylio data such as [daylio-visualisations](https://github.com/pajowu/daylio-visualisations) and [https://github.com/pwcazenave/daylio2yearinpixels]() which are worth checking out.

## Structure

The application is broken up into the following areas:

1. [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) of the data (input CSV to cleaned CSV and then a database)
2. Personalised reporting (database queries for create reports)
3. Additional functionality, to improve awareness and provide insights which can drive actions. Such as a dashboard view over various time frames, measurement against goals, automated alerts and forecasting.

## Documentation

- [Installation instructions](docs/installation.md)
- [Usage instructions](docs/usage.md)
