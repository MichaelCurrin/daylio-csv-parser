# Daylio Analysis Tool
Process personal data exported from the [Daylio](https://daylio.webflow.io/) app for analysis and reporting.

## Context

[Daylio](https://daylio.webflow.io/) is a mobile app which works as visual diary or journal. It allows one to keep a history of daily activities and moods. Activities are recorded using customised icons with binary Yes/No values. Mood is recorded on 5-point scale from low to high. A text note is optional.

This _daylio_ application is for users of the Daylio diary app who want to go beyond the app's own built-in reporting to seek a better understanding of one's experiences and emotions. Users of this application need to have Daylio Premium unlocked in order to export the `daylio_export.csv` file.

## Structure

The application is broken up into the following logical areas:

1. [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) of the data (CSV to cleaned CSV to database)
2. Personalised reporting (database queries for create reports)
3. Additional functionality to improve awareness and provide insights which can drive actions. Such as a dashboard view over various time frames, measurement against goals, automated alerts and forecasting.

## Documentation

- [Installation instructions](docs/installation.md)
- [Usage instructions](docs/usage.md]
