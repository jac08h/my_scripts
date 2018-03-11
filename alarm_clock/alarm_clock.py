#!/usr/bin/env python

import argparse
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--seconds', type=int, default=0)
parser.add_argument('-m', '--minutes', type=int, default=0)

args = parser.parse_args()
args.seconds += args.minutes * 60

sleep(args.seconds)
song = AudioSegment.from_wav('sound.wav')
play(song)
