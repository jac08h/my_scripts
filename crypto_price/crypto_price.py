#!/usr/bin/env python

import requests
import argparse


def get_price(from_symbol, to_symbol):
    url = 'https://min-api.cryptocompare.com/data/price'
    params = {'fsym': from_symbol, 'tsyms':to_symbol}
    r = requests.get(url, params=params)

    output = '{}/{}: {}'.format(from_symbol, to_symbol, r.json()[to_symbol])
    return output


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('from_symbols', type=str, help='Separate symbols by coma if you want to use more than one.')
    parser.add_argument('to_symbols', type=str, help='Separate symbols by coma if you want to use more than one.')
    return parser.parse_args()


def main():
    args = get_args()

    to_symbols = args.to_symbols.split(',')
    from_symbols = args.from_symbols.split(',')

    for fs in from_symbols:
        print('*'*20)
        for ts in to_symbols:
            price = get_price(fs.upper(), ts.upper())
            print(price)

if __name__ == '__main__':
    main()
