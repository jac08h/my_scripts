#!/usr/bin/env python

import requests
import argparse


def get_price(from_symbol, to_symbol):
    url = 'https://min-api.cryptocompare.com/data/price'
    params = {'fsym': from_symbol, 'tsyms':to_symbol}
    r = requests.get(url, params=params)
    # TODO: error handling

    return r.json()[to_symbol]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('from_symbols', type=str, help='Separate symbols by comma if you want to use more than one.')
    parser.add_argument('to_symbols', type=str, help='Separate symbols by comma if you want to use more than one.')
    return parser.parse_args()


def format_output(from_symbol, to_symbol, price):
    output = '{}/{}: {}'.format(from_symbol, to_symbol, price)
    return output


def main():
    args = get_args()

    to_symbols = [s.upper() for s in args.to_symbols.split(',')]
    from_symbols = [s.upper() for s in args.from_symbols.split(',')]

    for fs in from_symbols:
        for ts in to_symbols:
            price = get_price(fs.upper(), ts.upper())
            output = format_output(fs, ts, price)
            print(output)

if __name__ == '__main__':
    main()
