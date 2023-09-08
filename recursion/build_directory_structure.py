# Given a string of space separated filesystem paths, return the corresponding directory
# struture as a hash.

# account/settings
# account/settings/activity/client/home
# profile/activity/team/client
# account/notifications
# about/contact/address
# about
# home
# about/team
# about/address

# NOTE: Only worry about merging at file system root. No deep merging necessary.


def build_hash_from_path(path):
    curr = path.pop(0)

    if len(path):
        return {curr: build_hash_from_path(path)}
    else:
        return {curr: {}}


def build_directory_structure(paths):
    result = {}
    paths_list = paths.split("\n")

    for path in paths_list:
        path_elements = path.split("/")
        dir_hash = build_hash_from_path(path_elements.copy())

        path_root = path_elements[0]

        if path_root not in result:
            result[path_root] = dir_hash[path_root]
        else:
            result[path_root].update(dir_hash[path_root])
    return result
