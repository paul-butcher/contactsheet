"""
Utility script to create single-colour images for testing.
"""
from PIL import Image

colours = [
    "#8a3ffc",
    "#ff7eb6",
    "#6fdc8c",
    "#d2a106",
    "#fa4d56",
    "#d4bbff",
    "#bae6ff"
]

for i, colour in enumerate(colours):
    img = Image.new("RGB", (20, 10), colour)
    img.save('{}.png'.format(i))
