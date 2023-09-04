# Charter: Demo Chart Fact Checker

## Overview

`Charter` is a Python package that allows users to automatically extract data from charts in images and perform fact-checking on various assertions related to the chart. The package uses state-of-the-art machine learning models for data extraction and natural language processing for fact-checking.

> Note: Charter is experimental and currently for proof of concept only. 

## Features

- Load charts from URLs or local files
- Extract textual data from charts using Optical Character Recognition (OCR)
- Convert the extracted data into a structured format (DataFrame)
- Perform fact-checking on a list of assertions provided by the user

## Installation

\`\`\`bash
pip install charter
\`\`\`

To install the package, simply run:

\`\`\`bash
pip install charter
\`\`\`


## Usage

### Command-Line Interface

You can run `Charter` from the command line using the following command:

\`\`\`bash
charter --file path/to/image.png --assertions "Your assertion 1" "Your assertion 2"
\`\`\`

Arguments:

- `--url`: Provide a URL to load the chart image from the internet
- `--file`: Provide a local file path to load the chart image from your system
- `--assertions`: List of assertions you want to fact-check

> Note: Either `--url` or `--file` must be provided depending on where you're taking the chart from. 

Example:

\`\`\`bash
charter --file ./chart.png --assertions "More than 2 people have siblings." "The average age is above 30."
\`\`\`

### Python

You can also use the package in your Python code:

\`\`\`python
from charter.src import image_input, chart_extraction, chart_fact_checking

#Load image and validate
image = image_input.load_image_from_file("path/to/image.png")

#Extract text and transform it to DataFrame
extracted_text = chart_extraction.extract_text_from_image(image)
df, _, _ = chart_extraction.text_to_structures(extracted_text)

#Define assertions and perform fact-checking
assertions = {
    "More than 2 people have siblings.": "how many people have more than 0 siblings?",
    "The average age is above 30.": "what is the average age?"
}
report = chart_fact_checking.fact_check(df, assertions)

#Print the report
print("Fact-Checking Report:")
for assertion, result in report.items():
    print(f"{assertion} - Result: {result}")
\`\`\`
