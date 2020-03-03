import time
from argparse import ArgumentParser

from status import Status


def get_call_to_memory_time(word: str) -> float:
    start = time.time()
    print(f"{word}", end="\n\n")
    end = time.time()

    return end - start


def per_access_time(file: str) -> None:
    words_list = [line.rstrip('\n') for line in open(file)]
    status = Status()

    for word in words_list:
        _time = get_call_to_memory_time(word)
        status.update_status(_time)

    status.print_stats()


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, help="Name of file with extension")

    argument_parser.set_defaults(func=per_access_time)

    # Parse and execute selected function
    args = argument_parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args.file)
    else:
        argument_parser.print_help()