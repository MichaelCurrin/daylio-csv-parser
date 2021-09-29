#!/usr/bin/env python
"""
Clean CSV application file.

Read in input CSV, clean it and write out to a new CSV.
"""
import csv
import datetime

from lib.config import AppConf

conf = AppConf()


def clean_row(row, default_activities):
    """
    Expect a CSV row and default activities and return cleaned row.

    @param row: dict of values as read from source CSV.
    @param default_activities: list of activities, initialised to default
        values.

    @return: row as a dict of field names and values. Includes fields which
        are fixed and also fields which are dynamic, based on activities
        which are used.
    """
    datetime_str = "{date} {time}".format(
        date=row['full_date'],
        time=row['time']
    )
    # Detect if time is 24H or 12H time.
    datetime_format = ""
    if 'm' in datetime_str:
        datetime_format = r"%Y-%m-%d %I:%M %p"
    else: 
        datetime_format = r"%Y-%m-%d %H:%M"

    datetime_obj = datetime.datetime.strptime(
        datetime_str,
        datetime_format
    )

    # Match the mood label against the configured label and numeric value.
    mood = row["mood"].strip()

    try:
        mood_score = conf.MOODS[mood]
    except KeyError as e:
        raise type(e)(
            f"Each mood label in your CS must be added to a conf file so that"
            f" it can be assigned a numeric value. Not found:"
            f" {mood}. Configured moods: {conf.MOODS}"
        )

    row_activities = default_activities.copy()
    for activity in row["activities"]:
        row_activities[activity] = 1

    out_row = {
        "timestamp": datetime_obj.timestamp(),
        "datetime": str(datetime_obj),
        "date": str(datetime_obj.date()),
        "weekday_label": row["weekday"],
        "weekday_num": datetime_obj.weekday(),
        "mood_label": mood,
        "mood_score": mood_score,
        "note": row["note"],
    }

    return {**out_row, **row_activities}


def clean_csv(csv_in, csv_out):
    """
    Read, clean and write data.

    The available activities set must be populated on the first pass through
    the input data, where an activity enters a set the first time is
    used. Once the names and number of columns are known, a default row
    of 0 (false) for each activity is set. Then a second pass of the data
    is done to set the 1 (true) values for relevant activities of a record.

    @param csv_in: Path to source CSV file to read in.
    @param csv_out: Path to cleaned CSV file  write out to.

    @return: None
    """
    available_activities = set()
    in_data = []

    print("Reading CSV: {}".format(csv_in))

    with open(csv_in) as f_in:
        # Ignore first byte which is an unwanted invisible character.
        f_in.read(1)
        reader = csv.DictReader(f_in)

        for row in reader:
            activities = row["activities"].split(" | ")

            # Ignore row of no activities, which will be a single null string
            # after splitting.
            if len(activities) == 1 and activities[0] == "":
                activities = []
            else:
                activities = [activity.strip() for activity in activities]
                available_activities.update(activities)

            row["activities"] = activities
            in_data.append(row)

    print("Replacing activities column with multiple activity columns")

    default_activities = {key: 0 for key in available_activities}
    out_data = [clean_row(row, default_activities.copy()) for row in in_data]

    out_fields = [
        "timestamp",
        "datetime",
        "date",
        "weekday_label",
        "weekday_num",
        "mood_label",
        "mood_score",
        "note",
    ]

    activity_columns = sorted(list(available_activities))
    # For readability of the CSV, insert the dynamic acitvity values before
    # the text note.
    out_fields[-1:-1] = activity_columns

    print(f"Writing cleaned CV to: {csv_out}")

    with open(csv_out, "w") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(out_data)


def main():
    """
    Main command-line function.
    """
    csv_in = conf.get("data", "source_csv")
    csv_out = conf.get("data", "cleaned_csv")

    clean_csv(csv_in, csv_out)


if __name__ == "__main__":
    main()
