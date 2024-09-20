import json
from pathlib import Path


with open(Path(".") / "schemas" / "schema.json") as f:
    schema = json.load(f)