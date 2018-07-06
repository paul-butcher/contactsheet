# -*- coding: utf-8 -*-

"""Console script for contactsheet."""
import sys
import click
from contactsheet import create_tiled_image

@click.command()
@click.option('--out-file', help='Path to file where the contactsheet should be saved', default='contactsheet.jpg')
def main(out_file):
    """Console script for contactsheet.

    Reads a list of paths to image files from STDIN, and
    compiles them into a contact sheet image
    """
    img = create_tiled_image([line.rstrip() for line in list(click.get_text_stream('stdin'))])
    img.convert('RGB').save(out_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
