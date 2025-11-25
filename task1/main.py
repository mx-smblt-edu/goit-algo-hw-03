import argparse
from dataclasses import dataclass
from pathlib import Path
from shutil import copyfile


@dataclass
class Context:
    """
    Represents a context containing the configuration for an operation.
    """
    destination: Path


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"File or directory '{args[1]}' is not found.")
        except PermissionError as e:
            print(f"Permission denied for '{args[1]}': {e}")
        except Exception as e:
            print(f"Error processing: {e}")

    return wrapper


@handle_exceptions
def read(context: Context, source: Path) -> None:
    for element in source.iterdir():
        if element.is_dir():
            read(context, element)
        else:
            copy_file(context, element)


@handle_exceptions
def copy_file(context: Context, file: Path) -> None:
    ext = file.suffix.strip('.').lower()
    new_path = Path(context.destination) / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


@handle_exceptions
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", "-s", required=True, help="Source folder")
    parser.add_argument("--destination", "-d", default="dist", help="Destination folder")
    args = vars(parser.parse_args())

    source = Path(args.get("source"))
    if not source.exists():
        print(f"Source '{source}' does not exist.")
        return
    if not source.is_dir():
        print("Source must be a directory.")
        return

    destination = Path(args.get("destination"))
    context = Context(destination=destination)
    read(context, source)


if __name__ == "__main__":
    main()
