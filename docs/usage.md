# Usage Instructions

If you have followed the [Installation Instructions](installation.md) and have Daylio's Premium mode activated, you may continue with the usage instructions here.

The main aim of this project is to expand make the Daylio export CSV easier to use, by transforming the data. In particular, the _activities_ column is split out and this application has been set to work on any number activities. Though, the moods for now are restricted to 5. TODO: Show the defaults.


## 1. Create the data

First, create a `daylio_export.csv` file on your mobile device. 

Sample input CSV:

```
year,date,weekday,time,mood,activities,note
2018,29 March,Thursday,11:54 pm,happy,"socialise | eat out | drinks | music | tired | dreamt",""
2018,28 March,Wednesday,10:21 pm,average,"tired | dreamt | stressed / frustrated ",""
```

This CSV always has 7 columns. However, the _activities_ value needs further processing to make it easy handle in a CSV editor. Each activity is separated by a pipe symbol and there may be no activities an empty string, or all the available activities may be used. The activities may be a mixture of the built-in labels and the ones defined by a user.


## 2. Read the data

Get the CSV to your computer. The simplest is to use a USB cable and plug your device in. Though, you might want to use Google Drive or e-mail.


## 3. Create a clean CSV

Sample output CSV:

```
TBC
```


## 4. Create a database

TBC
