/* When importing a multiple times, it is useful to clear existing any data
 first. */
DROP TABLE IF EXISTS daylio;

.mode csv

/* Usage: .import FILE TABLE */
.import 'var/data_out/cleaned.csv' daylio
