#!/usr/bin/env python

from pydub import AudioSegment
import os
import argparse


def find_all_wmas(directory):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('wma'):
                files.append(os.path.join(dirpath, filename))
    return files


def convert_wma_to_mp3(wma_file_path, new_path):
    wma_version = AudioSegment.from_file(wma_file_path)
    mp3_version = wma_version.export(new_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?', help='Path to directory with wma files.')
    args = parser.parse_args()
    path = args.path
    # TODO: verbosity argument.

    if path is None:
        print('No path specified. Exiting.')
        return

    wma_files = find_all_wmas(path)
    for wma_file in wma_files:
        try:
            convert_wma_to_mp3(wma_file, wma_file.replace('wma', 'mp3'))
            print(wma_file)
        except Exception as e:
            print('Error converting {}.'.format(wma_file))
            print(e)

        os.remove(wma_file)


if __name__ == '__main__':
    main()
