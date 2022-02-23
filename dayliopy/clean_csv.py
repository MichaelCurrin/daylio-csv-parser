#!/usr/bin/env python
"""
Clean CSV application file.

Read in input CSV, clean it and write out to a new CSV.
"""
import codecs
import csv
import datetime
from typing import Optional, Sequence

from .lib.config import AppConf


TStrDict = dict[str, str]
TIntDict = dict[str, int]
TDictRows = list[TStrDict]

conf = AppConf()

DT_12H = r"%Y-%m-%d %I:%M %p"
DT_24H = r"%Y-%m-%d %H:%M"

ACTIVITIES_KEY = "activities"
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


def to_dt(date: str, time: str) -> datetime.datetime:
    """
    Convert date and time to datetime object.

    :param date: Date in format like '2021-09-28'.
    :param time: Time in format like '10:00 pm' or '22:00'.
    """
    dt_str = f"{date} {time}"

    is_12h = time.endswith("am") or time.endswith("pm")
    dt_format = DT_12H if is_12h else DT_24H

    return datetime.datetime.strptime(dt_str, dt_format)


def interpret_moods() -> TIntDict:
    result = {}
    for key in conf.MOODS.keys():
        for mood in key.split(","):
            result[mood.strip()] = conf.MOODS[key]
    return result


def get_score(mood: str, interpreted_moods: TIntDict) -> int:
    """
    Get mood score.
    """
    # Match the mood label against the configured label and numeric value.
    mood = mood.strip()

    try:
        mood_score = interpreted_moods[mood]
    except KeyError as e:
        raise type(e)(
            f"Each mood label in your CSV must be added to a conf file so that"
            f" it can be assigned a numeric value. Not found:"
            f" {mood}. Configured moods: {conf.MOODS}"
        )

    return mood_score


def format_row(
    row: TStrDict, dt: datetime.datetime, mood: str, mood_score: int
) -> dict:
    """
    Convert Daylio row data for writing to CSV.
    """
    return {
        "timestamp": dt.timestamp(),
        "datetime": str(dt),
        "date": str(dt.date()),
        "weekday_label": row["weekday"],
        "weekday_num": dt.weekday(),
        "mood_label": mood,
        "mood_score": mood_score,
        "note": row["note"],
    }


def clean_row(
    row: TStrDict,
    default_activities: TIntDict,
    interpreted_moods: TIntDict,
) -> TStrDict:
    """
    Expect a CSV row and default activities and return cleaned row.

    :param row: Values as read from source CSV.
    :param default_activities: Activities, initialized to default values.

    :return combined: Row as field names and values. Includes fields which are
        fixed and also fields which are dynamic, based on activities which are
        used. A separate variable had to be used here to avoid getting a type
        error.
    """
    dt = to_dt(row["full_date"], row["time"])

    mood = row["mood"]
    mood_score = get_score(mood, interpreted_moods)

    row_activities = default_activities.copy()

    for activity in row["activities_list"]:
        row_activities[activity] = 1

    out_row = format_row(row, dt, mood, mood_score)

    combined = {**out_row, **row_activities}

    return combined


def process_activities(activities_str: str) -> list:
    """
    Split activities as a pipe-separated string into a list of activities.
    """
    activities_split = activities_str.split(" | ")

    # Ignore row of no activities, which will be a single null string after
    # splitting.
    if len(activities_split) == 1 and activities_split[0] == "":
        activities_list = []
    else:
        activities_list = [activity.strip() for activity in activities_split]

    return activities_list


def validate_input_csv(fieldnames: Optional[Sequence[str]]) -> None:
    """
    Validate the input CSV has appropriate fields.

    The fields are unlikely to be missing by checking that here helps for the
    Mypy check.
    """
    if not fieldnames:
        raise ValueError("Column names are missing")

    if ACTIVITIES_KEY not in fieldnames:
        raise ValueError(f"{ACTIVITIES_KEY} column missing - found: {fieldnames}")


def read_csv(csv_in_path: str) -> tuple[set[str], TDictRows]:
    """
    Read Daylio CSV.

    Ignore types because the row's type if fixed with strings as values and
    we are adding the activities list to it as a list.
    """
    available_activities: set[str] = set()
    in_data: list[TStrDict] = []

    with codecs.open(csv_in_path, "r", encoding="utf-8-sig") as f_in:
        reader = csv.DictReader(f_in)

        validate_input_csv(reader.fieldnames)

        for row in reader:
            # TODO: break out block into a function.

            original_activities_str = row[ACTIVITIES_KEY]
            if original_activities_str is None:
                raise ValueError(
                    f"The {ACTIVITIES_KEY} column is present but blank."
                    " Fix the formatting of your CSV. Got row: \n  {row}"
                )
            activities_list = process_activities(original_activities_str)

            available_activities.update(activities_list)

            row["activities_list"] = activities_list  # type: ignore
            in_data.append(row)

    return available_activities, in_data


def clean_daylio_data(available_activities: set, in_data: TDictRows):
    """
    Convert Daylio CSV file to a more usable CSV report.
    """
    default_activities = {key: 0 for key in available_activities}
    moods = interpret_moods()
    out_data = [clean_row(row, default_activities.copy(), moods) for row in in_data]

    out_fields = CSV_OUT_FIELDS.copy()
    activity_columns = sorted(list(available_activities))

    # For readability of the CSV, insert the dynamic activity values before
    # the text note at the end.
    out_fields[-1:-1] = activity_columns

    return out_data, out_fields


def write_csv(
    csv_out_path: str, out_data: list[TStrDict], out_fields: list[str]
) -> None:
    """
    Write rows to a CSV.
    """
    with open(csv_out_path, "w") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(out_data)


def process(csv_in: str, csv_out: str) -> None:
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

    print("Replacing the activities column with multiple activity columns")
    out_data, out_fields = clean_daylio_data(available_activities, in_data)

    print(f"Writing cleaned CSV to: {csv_out}")
    write_csv(csv_out, out_data, out_fields)


def main():
    """
    Command-line entry-point.
    """
    csv_in = conf.get("data", "source_csv")
    csv_out = conf.get("data", "cleaned_csv")

    process(csv_in, csv_out)


if __name__ == "__main__":
    main()
