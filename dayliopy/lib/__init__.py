"""
Lib module initialization file.
"""
import os


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

# Encoding added to avoid error on Windows
#     https://github.com/MichaelCurrin/daylio-csv-parser/issues/25

CSV_ENCODING = "latin-1"
