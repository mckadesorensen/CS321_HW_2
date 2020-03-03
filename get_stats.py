import time
from argparse import ArgumentParser

from status import Status


def main(file: str) -> None:

    words_list = [line.rstrip('\n') for line in open(file)]
    status = Status()
    for word in words_list:
        start = time.time()
        print(f"{word}", end="\n\n")
        end = time.time()

        if .00001 <= end - start < .0000999999:
            print(f"Time {end - start}")
            status.l2_cache += 1
        elif end - start < .0000099999:
            print(f"Time {end - start}")
            status.l1_cache += 1
        elif .00599999 > end - start >= .0001:
            print(f"Time {start - start}")
            status.ram += 1
        elif end - start >= .006:
            print(f"Time {end - start}")
            status.tbl_miss += 1

    status.print_stats()


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, help="Name of file with extension")

    argument_parser.set_defaults(func=main)

    # Parse and execute selected function
    args = argument_parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args.file)
    else:
        argument_parser.print_help()