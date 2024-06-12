import argparse
from polars_nightly import git

def main():
    parser = argparse.ArgumentParser(description="Polars nightly build installer")
    subparser = parser.add_subparsers(dest='command')
    parser_install = subparser.add_parser('install', help="Greet someone")

    # Add arguments
    parser_install.add_argument('-v', '--version', type=str, required=False, help="Installed version")

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'version':
        greet(args.version)

    # Print a greeting message
    print(f"Hello, {args.version}!")

if __name__ == "__main__":
    main()
