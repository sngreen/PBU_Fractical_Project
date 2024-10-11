
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

LOG_FILE = os.environ.get("LOG_FILE")
REPORT_FILE = os.environ.get("REPORT_FILE")
MENU_FILE = os.environ.get("MENU_FILE")

for xxx in [LOG_FILE, REPORT_FILE]:
    Path(xxx).parent.mkdir(parents=True, exist_ok=True)
