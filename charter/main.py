"""Main script for the chart fact checking demo"""

import sys
from charter.src import image_input
from charter.src import chart_extraction
from charter.src import chart_fact_checking
import argparse

def main():
    print(sys.argv)
    parser = argparse.ArgumentParser(description='Chart-based Fact Checker')
    parser.add_argument('--url', type=str, help='Image URL')
    parser.add_argument('--file', type=str, help='Path to the image file')
    parser.add_argument('--assertions', type=str, nargs='*', help='List of assertions for fact-checking')

    args = parser.parse_args()
    print(args)

    if args.url:
        image = image_input.load_image_from_url(args.url)
    elif args.file:
        image = image_input.load_image_from_file(args.file)
    else:
        print("Either --url or --file must be provided.")
        return

    if not image_input.validate_image(image):
        print("Invalid image. Exiting.")
        return

    # Extract text and convert it to different structures
    extracted_text = chart_extraction.extract_text_from_image(image)
    df, md_table, latex_table = chart_extraction.text_to_structures(extracted_text)

    print("Arguments", args.assertions)
    # Perform fact-checking if assertions are provided
    if args.assertions:
        
        # Convert assertions to a dictionary (you might want to improve this part)
        assertions_dict = {assertion: assertion for assertion in args.assertions}

        # Perform fact-checking
        report = chart_fact_checking.fact_check(df, assertions_dict)

        # Print or save the report
        print("Fact-Checking Report:")
        for assertion, result in report.items():
            print(f"{assertion} - Result: {result}")
    else:
        print("No assertions provided. Exiting.")

if __name__ == "__main__":
    main()
