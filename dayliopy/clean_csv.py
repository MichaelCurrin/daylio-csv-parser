#!/usr/bin/env python
"""
Clean CSV application file.

Read in input CSV, clean it and write out to a new CSV.
"""
import codecs
import csv
import datetime
from typing import Tuple, Union

from lib.config import AppConf

conf = AppConf()

DT_12H = r"%Y-%m-%d %I:%M %p"
DT_24H = r"%Y-%m-%d %H:%M"

CSV_OUT_FIELDS = [
    "timestamp",
    "datetime",
    "date",
    "weekday_label",
    "weekday_num",
    "mood_label",
    "mood_score",
    "note",
]


def parse_datetime(dt_str: str) -> datetime.datetime:
    """
    :param datetime_str: Date and time in one of two possible formats.
    """
    is_12h = dt_str.endswith("am") or dt_str.endswith("pm")
    dt_format = DT_12H if is_12h else DT_24H

    return datetime.datetime.strptime(dt_str, dt_format)


def parse_mood(mood: str) -> Tuple[str, int]:
    # Match the mood label against the configured label and numeric value.
    mood = mood.strip()

    try:
        mood_score = conf.MOODS[mood]
    except KeyError as e:
        raise type(e)(
            f"Each mood label in your CSV must be added to a conf file so that"
            f" it can be assigned a numeric value. Not found:"
            f" {mood}. Configured moods: {conf.MOODS}"
        )

    return mood, mood_score


def format_row(
    row: dict[str, str], datetime_obj, mood: str, mood_score: int
) -> dict[str, Union[str, int]]:
    return {
        "timestamp": datetime_obj.timestamp(),
        "datetime": str(datetime_obj),
        "date": str(datetime_obj.date()),
        "weekday_label": row["weekday"],
        "weekday_num": datetime_obj.weekday(),
        "mood_label": mood,
        "mood_score": mood_score,
        "note": row["note"],
    }


def clean_row(row: dict[str, str], default_activities: list[str]) -> dict[str, str]:
    """
    Expect a CSV row and default activities and return cleaned row.

    :param row: Values as read from source CSV.
    :param default_activities: Activities, initialized to default values.

    :return: Row as field names and values. Includes fields which
        are fixed and also fields which are dynamic, based on activities
        which are used.
    """
    date = row["full_date"]
    time = row["time"]
    datetime_str = f"{date} {time}"

    datetime_obj = parse_datetime(datetime_str)

    mood, mood_score = parse_mood(row["mood"])

    row_activities = default_activities.copy()

    for activity in row["activities"]:
        row_activities[activity] = 1

    out_row = format_row(row, datetime_obj, mood, mood_score)

    return {**out_row, **row_activities}


def read_csv(csv_in_path: str):
    available_activities = set()
    in_data = []

    with codecs.open(csv_in_path, "r", encoding="utf-8-sig") as f_in:
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

    return available_activities, in_data


def clean_csv(csv_in: str, csv_out: str) -> None:
    """
    Read, clean and write data.

    The available activities set must be populated on the first pass through the
    input data, where an activity enters a set the first time is used. Once the
    names and number of columns are known, a default row of 0 (false) for each
    activity is set. Then a second pass of the data is done to set the 1 (true)
    values for relevant activities of a record.

    Note use of codecs with encoding for Windows support. This also means the
    hack on Unix to ignore the first byte of unwanted invisible character is no
    longer needed.

    :param csv_in: Path to source CSV file to read in.
    :param csv_out: Path to cleaned CSV file write out to.
    """
    print(f"Reading CSV: {csv_in}")

    available_activities, in_data = read_csv(csv_in)

    print("Replacing activities column with multiple activity columns")

    default_activities = {key: 0 for key in available_activities}
    out_data = [clean_row(row, default_activities.copy()) for row in in_data]

    out_fields = CSV_OUT_FIELDS.copy()
    activity_columns = sorted(list(available_activities))

    # For readability of the CSV, insert the dynamic activity values before
    # the text note at the end.
    out_fields[-1:-1] = activity_columns

    print(f"Writing cleaned CV to: {csv_out}")

    with open(csv_out, "w") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(out_data)


def main():
    """
    Command-line entry-point.
    """
    csv_in = conf.get("data", "source_csv")
    csv_out = conf.get("data", "cleaned_csv")

    clean_csv(csv_in, csv_out)


if __name__ == "__main__":
    main()
