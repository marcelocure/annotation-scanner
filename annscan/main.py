#!/usr/bin/env python

from __future__ import print_function
import argparse
import sys
import metadata
import io_file
import scanner
import charts
import matplotlib.pyplot as plt


def parse_input(argv):

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description)

    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))

    arg_parser.add_argument('PROJECTPATH',
                            help='Path of the project to be scanned')

    args = arg_parser.parse_args()
    
    project_path = args.PROJECTPATH
    return project_path


def main(argv):
    path = parse_input(argv)
    file_list = io_file.scan_path(path)
    total_files = len(file_list)
    print('{0} java files'.format(total_files))
    occurrencies = scanner.scan_annotation(file_list)
    print('{0} java files containing @Refactoring annotation'.format(occurrencies))
    charts.generate_chart(total_files, occurrencies)


if __name__ == '__main__':
    main(sys.argv)
