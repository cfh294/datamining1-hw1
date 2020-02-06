#!/usr/bin/env python3
"""
google-app.py

01 July 2018     - Written by Robert Preuss (preuss93@students.rowan.edu)
05 February 2020 - Updates from Connor Hornibrook (hornibrookc@rowan.edu) 
"""
import argparse
import configparser
import datetime
from apiclient import discovery


def print_to_file(filename, result):
    """
    Write search information to file.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        request_info = result['queries']['request'][0]
        date = datetime.datetime.now().strftime("%c")

        file.write("Search Terms: {}\n".format(request_info['searchTerms']))
        file.write("Result Count: {}\n".format(request_info['totalResults']))
        file.write("Timestamp: {}\n\n".format(date))

    # Write search results to file
    items = result['items']
    with open(filename, 'a', encoding="utf-8") as file:
        for counter, item in enumerate(items):
            file.write("Item #{}\n".format(counter+1))
            file.write("Title: {}\n".format(item['title']))
            file.write("Snippet: {}\n".format(item['snippet']))
            file.write("Link: {}\n\n".format(item['link']))


def main():
    """
    Main method logic
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='Search query')
    parser.add_argument("-c", "--config-file",
                        help="Path to configuration file containing API information.",
                        required=True)
    args = parser.parse_args()

    # Parse values from configuration file
    config = configparser.ConfigParser()
    config.read(args.config_file)
    key = config['GOOGLE']['developerKey']
    engine = config['GOOGLE']['searchEngine']

    # Construct search
    query = args.query
    service = discovery.build("customsearch", "v1", developerKey=key)
    resource = service.cse()

    # Perform search and print results
    result = resource.list(q=query, cx=engine, num=10).execute()
    filename = "Google_Output.txt"
    print_to_file(filename, result)

# RUn the program
if __name__ == '__main__':
    main()
