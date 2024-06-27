#!/usr/bin/python3
"""This module calculates the perimeter of an island represented by a grid.

The island is assumed to have no lakes (connected water within its landmass).
Each cell in the grid is either 0 (water) or 1 (land).
"""


def island_perimeter(grid):
  """Calculates the total length of the island's outer boundary.

  Args:
      grid: A 2D list representing the island grid. Zeros represent water, ones represent land.

  Returns:
      The total perimeter of the island (sum of all its outer edges).

  Raises:
      TypeError: If the input grid is not a list.
  """

  if type(grid) != list:
    return 0

  # Get the number of rows and columns in the grid
  num_rows = len(grid)
  num_cols = len(grid[0])

  perimeter = 0

  # Loop through each cell in the grid
  for row_index, row in enumerate(grid):
    for col_index, cell in enumerate(row):
      # If the current cell is water, skip to the next cell
      if cell == 0:
        continue

      # Check if the current cell is on an edge (has water as a neighbor)
      is_top_edge = row_index == 0 or (len(grid[row_index - 1]) > col_index and grid[row_index - 1][col_index] == 0)
      is_right_edge = col_index == num_cols - 1 or (num_cols > col_index + 1 and row[col_index + 1] == 0)
      is_bottom_edge = row_index == num_rows - 1 or (len(grid[row_index + 1]) > col_index and grid[row_index + 1][col_index] == 0)
      is_left_edge = col_index == 0 or row[col_index - 1] == 0

      # Count the number of edges (water neighbors) of the current cell
      num_edges = sum([is_top_edge, is_right_edge, is_bottom_edge, is_left_edge])

      # Add the number of edges (water neighbors) to the total perimeter
      perimeter += num_edges

  return perimeter

