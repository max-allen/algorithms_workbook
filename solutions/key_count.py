# Given an object and target key, return all instances of the target present on
# the object.

# {
#   foo: {
#     bar: {}
#   },
#   baz: {
#     quux: {
#       corge: {
#       }
#     },
#   },
#   quux: {}
# }


def key_count(obj, target, count=0):
    """
    time: O(n), where n is the number keys present on the object
    space: O(n), where n is the number of non empty keys on the object
    """
    for key in obj:
        if key == target:
            count += 1

        val = obj[key]

        if len(val) > 0:
            count = key_count(val, target, count)

    return count
