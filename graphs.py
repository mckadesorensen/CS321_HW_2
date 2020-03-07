from typing import List, Tuple

from matplotlib import pyplot as plt
from argparse import ArgumentParser

from word_frequency import display_frequency_data


def plot_stats(file: str):
    stats, threads = get_stats(file)
    plt.plot(stats, threads)
    plt.ylabel("Threads")
    plt.xlabel("Time")
    plt.show()


def get_stats(file: str) -> Tuple[List[int], List[int]]:
    threads = []
    for index in range(4):
        threads.append(2 ** index)

    stats = []
    for thread in threads:
        stats.append(display_frequency_data(file, thread))
    return stats, threads


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, help="Path to file containing words")

    argument_parser.set_defaults(func=plot_stats)

    # Parse and execute selected function
    args = argument_parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args.file)
    else:
        argument_parser.print_help()