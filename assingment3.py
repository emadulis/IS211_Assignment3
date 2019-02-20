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
        There were 10000 page hits today, image requests account for 78.77% of
        hits. Google Chrome has the most hits with 4042.
    """

    readpage = csv.reader(url_file)
    linecount = 0
    imgreq = 0

    chrome = ['Google Chrome', 0]
    ie = ['Internet Explorer', 0]
    safari = ['Safari', 0]
    fox = ['Firefox', 0]
    for line in readpage:
        linecount += 1
        if re.search("firefox", line[2], re.I):
            fox[1] += 1
        elif re.search(r"MSIE", line[2]):
            ie[1] += 1
        elif re.search(r"Chrome", line[2]):
            chrome[1] += 1
        elif re.search(r"Safari", line[2]) and not re.search("Chrome", line[2]):
            safari[1] += 1
        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
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

    result = ('There were {} page hits today, image requests account for {}% of '
           'hits. \n{} has the most hits with {}.').format(linecount,
                                                           image_pct,
                                                           top_name,
                                                           top_browser)
    print(result)


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
