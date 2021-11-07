# CSV format

See [sample.csv][] for an example of what gets exported by the Daylio app.

The standard CSV always has 8 columns:

- `full_date 	date 	weekday 	time 	mood 	activities 	note_title 	note`

The `activities` column will have zero or more activities. That needs further processing to make it easy to handle in a CSV editor or database. That is why this Daylio parser project exists.

Each activity is separated by a pipe symbol and there may be no activities an empty string, or all the available activities may be used. The activities may be a mixture of the built-in labels and the ones defined by a user.

e.g.

- `clean | music | movies / tv | bad sleep | tired`


[sample.csv]: https://github.com/MichaelCurrin/daylio-csv-parser/blob/master/dayliopy/sample.csv
