#!/usr/bin/env python

from jsonschema import validate
import os
import json
import sys

DEFAULT_SCHEMAFILE = 'schemas/part.schema.json'
SCHEMAFILE = os.getenv('SCHEMAFILE', DEFAULT_SCHEMAFILE)
JSONFILE = sys.argv[1]

def main():
    schema = json.load(open(SCHEMAFILE, "r"))
    jsonfile = json.load(open(JSONFILE, "r"))
    try:
        validate(instance=jsonfile, schema=schema)
        print(f"{JSONFILE}: Validation succeeded")
    except Exception as e :
        print(f"{JSONFILE}: Validation failed")
        raise(e)

if __name__ == "__main__":
    main()
