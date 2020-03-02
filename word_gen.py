"""
word_gen.py
McKade Sorensen
03/02/2020

This built off of Matt Perry's word_gen.py script
"""

import random
from argparse import ArgumentParser


def create_file(write_file: str) -> None:
    count = 1000*1000
    word_file = "/usr/share/dict/words"

    words = open(word_file).read().splitlines()
    words_length = len(words)

    all_the_words = []
    for size in range(count):
        all_the_words.append(words[random.randint(0, words_length-1)])

    sortedWords = sorted(all_the_words, key=str.lower)

    with open(write_file, "w") as file:
        for word in sortedWords:
            file.write("%s\n" % word)


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, help="Name of file with extension")

    argument_parser.set_defaults(func=create_file)

    # Parse and execute selected function
    args = argument_parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args.file)
    else:
        argument_parser.print_help()