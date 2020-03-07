"""
words_frequency.py
McKade Sorensen
CS321 Homework 2

Checks for the frequency of words and then assigns them to a low, high, medium score.
"""
import random
import math
import operator
import time
import concurrent.futures

from argparse import ArgumentParser
from typing import List, Dict, Tuple


def open_file(file: str) -> str:
    with open(file) as f:
        words = f.read()
    return words


def break_up_words(string_of_words: str) -> List[str]:
    words = string_of_words.split("\n")
    return words


def get_word_frequency(words: List[str]) -> Dict[str, int]:
    words_stats = {}
    for word in words:
        if words_stats.get(word.lower()):
            words_stats[word.lower()] += 1
            continue

        words_stats.update({word.lower(): 1})

    return words_stats


# noinspection PyTypeChecker
def count_of_highest_used_word(words: Dict[str, int]) -> Tuple[str, int]:
    return max(words.items(), key=operator.itemgetter(1))


# noinspection PyTypeChecker
def count_of_lowest_used_word(words: Dict[str, int]) -> Tuple[str, int]:
    return min(words.items(), key=operator.itemgetter(1))


def find_high_low_values(words: Dict[str, int]) -> Dict[str, int]:
    lowest_used = count_of_lowest_used_word(words)
    highest_used = count_of_highest_used_word(words)

    return {
        "lowest": lowest_used[1],
        "highest": highest_used[1]
    }


def set_frequency_levels(high_low_values: Dict[str, int]) -> Dict[str, Dict[str, int]]:
    one_third = math.floor((1/3) * high_low_values["highest"])
    two_third = math.floor((2/3) * high_low_values["highest"])

    return {
        "low":    {
            "low_bound":  high_low_values["lowest"],
            "high_bound": one_third
        },
        "medium": {
            "low_bound":  one_third + 1,
            "high_bound": two_third
        },
        "high":   {
            "low_bound":  two_third + 1,
            "high_bound": high_low_values["highest"]
        }
    }


def get_random_words(words: Dict[str, int]) -> Dict[str, int]:
    random_words = {}
    for count in range(0, 50):
        random_word = random.choice(list(words.keys()))
        random_words.update({random_word: words[random_word]})
    return random_words


def print_frequency_level(words: Dict[str, int], high_low_values) -> None:
    frequency_levels = set_frequency_levels(high_low_values)
    for word in words:
        if frequency_levels["low"]["low_bound"] <= words[word] <= frequency_levels["low"]["high_bound"]:
            print(f"Word: {word}, Count: {words[word]}, frequency: Low")
        if frequency_levels["medium"]["low_bound"] <= words[word] <= frequency_levels["medium"]["high_bound"]:
            print(f"Word: {word}, Count: {words[word]}, frequency: Medium")
        if frequency_levels["high"]["low_bound"] <= words[word] <= frequency_levels["high"]["high_bound"]:
            print(f"Word: {word}, Count: {words[word]}, frequency: High")


def break_up_list(words: List[str]) -> Tuple[List[str], List[str], List[str]]:
    one_third = math.floor((1/3) * len(words))
    two_third = math.floor((2/3) * len(words))
    return words[0:one_third], words[one_third:two_third], words[two_third:len(words)]


def run_get_word_frequency_with_threads(words: list, threads) -> Dict[str, int]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future = executor.submit(get_word_frequency, words)
        return future.result()


def display_frequency_data(file: str, thread=1) -> float:
    start_time = time.time()
    string_of_words = open_file(file)
    words = break_up_words(string_of_words)

    words_stats = run_get_word_frequency_with_threads(words, thread)

    high_low_values = find_high_low_values(words_stats)
    random_words = get_random_words(words_stats)
    print_frequency_level(random_words, high_low_values)

    end_time = time.time()
    print(end_time - start_time)
    return end_time - start_time


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, help="Path to file containing words")

    argument_parser.set_defaults(func=display_frequency_data)

    # Parse and execute selected function
    args = argument_parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args.file)
    else:
        argument_parser.print_help()