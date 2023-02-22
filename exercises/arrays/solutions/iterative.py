# given a non-empty list of distinct integers and an integer representing
# a target sum, return an list containing the two numbers that total the sum.
# if no two numbers exist within the list, return an empty list.

# [3, 5, -4, 8, 11, 1, -1, 6], 10 -> [-1 ,11]

# [4], 5 -> []

def two_number_sum(arr, target):
  """
  time: O(N) | space: O(N)
  """
  no_match = []

  if len(arr) < 2:
    return no_match

  visited = {}

  for el in arr:
    comp = target - el

    if comp in visited:
      return [el, comp]

    else:
      visited[el] = None

  return no_match