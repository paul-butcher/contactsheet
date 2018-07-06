#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `contactsheet` package."""

import pytest

from click.testing import CliRunner

from contactsheet import contactsheet
from contactsheet import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output


@pytest.mark.parametrize(
    "cell_count",
    xrange(1, 145)
)
def test_get_grid_size(cell_count):
    """
    Grid size is intended to find the squarest arrangement that will fit
    the given number of cells.

    This means that two criteria should be met
    - It should fit all the cells,
    - The two values should be as close as possible
    """
    x, y = contactsheet.get_grid_size(cell_count)
    assert x * y >= cell_count
    assert abs(x - y) <= 1
