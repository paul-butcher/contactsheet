import os
from PIL import ImageColor

import pytest
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from contactsheet.contactsheet import create_tiled_image


IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'features', 'images')

COLOURS = [
    "#000000",
    "#8a3ffc",
    "#ff7eb6",
    "#6fdc8c",
    "#d2a106",
    "#fa4d56",
    "#d4bbff",
    "#bae6ff"
]

scenarios('features')


@pytest.fixture(scope='function')
def context():
    return {}


@when(parsers.parse('a contactsheet with {image_count:d} images is requested'))
def a_contactsheet_with_4_images_is_requested(context, image_count):
    """a contactsheet with 4 images is requested."""
    context['image'] = create_tiled_image(
        [os.path.join(IMAGES_DIR, '{}.png'.format(ix)) for ix in range(image_count)]
    )


@then(parsers.parse('the images will be arranged thus\n{text}'))
def the_images_will_be_arranged(context, text):
    """the images will be arranged thus"""
    rows = text.split('\n')
    image = context['image']
    im_width, im_height = image.size
    tile_height = im_height / len(rows)
    image.save('test_out.png')
    for i, row in enumerate(rows):
        row_centre = (tile_height * i) + (tile_height/2)
        cells = row.strip('| ').split('|')
        tile_width = im_width / len(cells)
        for j, cell in enumerate(cells):
            expected_colour = ImageColor.getrgb(COLOURS[int(cell)])
            col_centre = (tile_width * j) + (tile_width / 2)
            assert expected_colour == image.getpixel((col_centre, row_centre))
