# metrology
Repository for grimdarkscaling metrology data. This is the primary source of truth for [grimdarkscaling.com](https://grimdarkscaling.com).

# Contributing
## Files and filenames
- New entries should be added to the `data` directory.
- 1 JSON object per file.
- Filenames should be ascii characters only, no spaces.

## Format
A full, commented, [json-schema](https://json-schema.org/) compatible schema is provided in schema [schemas/part.schema.json](schemas/part.schema.json). Here is a quick example:

    {
      "partName": "My descriptive part name",
      "dimensions": {
        "partHeight": 6.2, # measurement in millimeters
        "partWidth": 4.8,
        "partLength": 2.6
      },
      "partNotes": "This is a test part and measurements are inaccurate!!",
      "partParentKit": "Manufacturer Boxed Product Name",
      "partMeasurementMethod": "Height measured from top of neck collar to bottom of belly creases",
      "tags": ["fake", "testing", "documentation"]
    }

## Merge Policy
- Open a pull request and tag [itsgc](https://github.com/itsgc) as reviewer.
- Wait for PR validation steps to go green.
