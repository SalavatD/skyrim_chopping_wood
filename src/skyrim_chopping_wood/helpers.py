import argparse

DELAY = 10
WAIT = 35
MOVE = 700


def parse_args():
    parser = argparse.ArgumentParser(
        prog='skyrim_chopping_wood',
        description='Script for chopping wood in Skyrim.',
        epilog='This script must be run with administrator rights. Usage example: python -m skyrim_chopping_wood'
    )
    parser.add_argument(
        '-d',
        '--delay',
        default=DELAY,
        metavar='SEC',
        type=int,
        help=f'delay time in seconds before running the script, default value: {DELAY}',
    )
    parser.add_argument(
        '-w',
        '--wait',
        default=WAIT,
        metavar='SEC',
        type=int,
        help=f'waiting time in seconds before next wood chopping, default value: {WAIT}',
    )
    parser.add_argument(
        '-m',
        '--move',
        default=MOVE,
        metavar='PX',
        type=int,
        help=f'distance in pixels to move camera down, default value: {MOVE}',
    )
    args = parser.parse_args()
    return {
        'delay': args.delay,
        'wait': args.wait,
        'move': args.move
    }
