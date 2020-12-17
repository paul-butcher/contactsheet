=====
Usage
=====

To use contactsheet in a project::

    import contactsheet
    img = create_tiled_image(['1.jpg', '2.jpg', '3.jpg', '4.jpg'])


`img`, above will be a PIL image consisting of the given files,
tiled thus:

+-------+-------+
| 1.jpg | 2.jpg |
+-------+-------+
| 3.jpg | 4.jpg |
+-------+-------+

To use from the command line, see the readme.

