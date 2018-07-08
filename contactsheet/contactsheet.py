# -*- coding: utf-8 -*-
"""
Functions for creating contactsheet images.
"""
import math

from PIL import Image, ImageOps


def create_tiled_image(image_paths):
    image_count = len(image_paths)
    if image_count == 0:
        return Image.new("RGBA", (1, 1), "black")
    grid_size = get_grid_size(image_count)
    tile_size, output_size = get_tiled_image_dimensions(grid_size, Image.open(image_paths[0]).size)
    final_image = Image.new("RGBA", output_size, "black")

    for i, image_path in enumerate(image_paths):
        insert_image_into_grid(final_image, tile_size, image_path, get_location_in_grid(grid_size, i))

    return final_image


def insert_image_into_grid(final_image, tile_size, image_path, location):
    input_image = Image.open(image_path)
    input_image.thumbnail(tile_size)
    final_image.paste(input_image, (tile_size[0] * location[0], tile_size[1] * location[1]))
    return final_image


def get_location_in_grid(grid, index):
    """
    Given an index position into a flat list, and a grid (cols, rows).  Return the
    col, row position of that index, assuming a horizontal-first view.

    e.g.
    +---+---+---+
    | 0 | 1 | 2 |
    +---+---+---+
    | 3 | 4 | 5 |
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+

    >>> get_location_in_grid((3, 3), 4)
    (1, 1)

    >>> get_location_in_grid((4, 3), 6)
    (2, 1)

    >>> get_location_in_grid((3, 4), 4)
    (1, 1)
    """

    return index % grid[0], int(math.floor(index / grid[0]))


def get_tiled_image_dimensions(grid_size, image_size):
    """

    An image consisting of tiles of itself (or same-sized) images
    will be as close to the same dimensions as the original.

    This returns two tuples - the size of the final output image, and the size of the
    tiles that it will consist of.

    :param grid_size: A 2-tuple (width, height) defining the shape of the grid (in number of images)
    :param image_size: A 2-tuple (width, height) defining the shape of the final image (in pixels)
    :return: two 2-tuples, the size of each tile and the size of the final output image/
    """
    tile_width = image_size[0] / grid_size[0]
    # preserve aspect ratio by dividing consistently. grid cols is always >= rows
    tile_height = image_size[1] / grid_size[0]

    # find the final height by multiplying up the tile size by the number of rows.
    final_height = tile_height * grid_size[1]

    return (tile_width, tile_height), (image_size[0], final_height)


def get_grid_size(cell_count):
    """
    Determines the best grid shape for a given cell count.

    The best grid shape is the one closest to square that minimises the number of blank cells
    e.g. for a square number, it is the corresponding square.
    >>> get_grid_size(25)
    (5, 5)

    It will otherwise be a rectangle, with the one value matching the square root
    >>> get_grid_size(20)
    (5, 4)

    If the number does not fit perfectly into such a rectangle, then it will be a rectangle the
    next size up.
    >>> get_grid_size(15)
    (4, 4)
    """
    sqrt = math.sqrt(cell_count)
    sqrt_floor = int(math.floor(sqrt))
    if sqrt == sqrt_floor:
        # perfect square
        cols = sqrt_floor
        rows = sqrt_floor
    else:
        # Otherwise, this is a rectangle.
        cols = sqrt_floor + 1  # Expand cols to accommodate
        rows = sqrt_floor + (1 if cell_count > sqrt_floor * cols else 0)  # Expand rows if needed

    return cols, rows  # PIL image sizes are width x height - analogous with cols x rows
