#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WeeK3 Module"""

import csv
import argparse
import urllib2
import re


def downloadData(url):
    """Function fetches csv data.
    Args:
        url(str): url where contents is found.
    Returns:
           CSV file
    """
    url_file = urllib2.urlopen(url)
    return url_file


def processData(url_file):
    """Processes csv file from the URL link.
    Args:
        url_file(file): A csv file.
    Returns:
           A string result with the number of page hits,
        the percentage of image requests, the browser with the most hits.
    Example:
        >>> runtest = downloadData('http://s3.amazonaws.com/cuny-is211-spring2015
        /weblog.csv')
        >>> processData(runtest)
        There's a total of 10000 page hits today.
        Images account for 96.69 % percent of all requests.
        Google Chrome is the top used browser with 331 hits.
    """

    readpage = csv.reader(url_file)
    linecount = 0
    imgreq = 0

    chrome = ['Google Chrome', 0]
    ie = ['Internet Explorer', 0]
    safari = ['Safari', 0]
    fox = ['Firefox', 0]

    for page in readpage:
        linecount += 1
        if re.search("firefox", page[2]):
            fox[1] += 1
        elif re.search(r"Internet Explorer", page[2]):
            ie[1] += 1
        elif re.search(r"chrome", page[2]):
            chrome[1] += 1
        elif re.search(r"safari", page[2]):
            safari[1] += 1
        elif re.search('([.jpg]|[.jpeg]|[.png]|[.gif]|[.JPG]|[.JPEG]|[.PNG]|[.GIF])', page[0]):
            imgreq += 1

    image_pct = ((float(imgreq) / linecount) * 100)

    browsers = [chrome, ie, safari, fox]

    top_browser = 0
    top_name = ' '
    for browser in browsers:
        if browser[1] > top_browser:
            top_browser = browser[1]
            top_name = browser[0]
        else:
            continue

    report = ("There's a total of {} page hits today.\n"
              "Images account for {} % percent of all requests.\n"
              "{} is the top used browser with {} hits.").format(linecount,
                                                             image_pct,
                                                             top_name,
                                                             top_browser)

    print(report)


def main():
    """This function will test both downloadData() and processData() functions."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="Enter a URL linking to a .csv file.")
    args = parser.parse_args()
    
    if args.url:
        try:
            data = downloadiData(args.url)
            processData(data)
        except urllib2.URLError as url_error:
            print 'URL is INVALID'
            raise URLError
    else:
        print 'Please enter a valid URL.'

if __name__ == '__main__':
    main()
