Feature: Generating contactsheet images

Scenario: Squares
When a contactsheet with 4 images is requested
Then the images will be arranged thus
  """
  |1|2|
  |3|4|
  """

Scenario: Perfect rectangles
When a contactsheet with 6 images is requested
Then the images will be arranged thus
  """
  |1|2|3|
  |4|5|6|
  """

Scenario: Imperfect rectangles
    0 represents a blank filler tile
When a contactsheet with 7 images is requested
Then the images will be arranged thus
  """
  |1|2|3|
  |4|5|6|
  |7|0|0|
  """
