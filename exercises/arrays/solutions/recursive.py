def two_number_sum(arr, target):
  # retrieves first item from list
  el = arr.pop(0)
  comp = target - el
  arr_length = len(arr)

  if comp in arr:
    return [el, comp]

  elif arr_length > 1:
    return two_number_sum(arr, target)

  return []