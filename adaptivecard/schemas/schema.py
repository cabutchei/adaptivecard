import json
from pathlib import Path


with open(Path(".") / "adaptivecard" / "schemas" / "schema.json") as f:
    schema = json.load(f)