import os, re


def get_markdown_link(title, path, prefix=None):
    """Formats title and path as Markdown link."""
    if title.count("/") == 2:
        title_stem = title.split("/").pop()
    else:
        title_stem = re.sub(r"./|\.py$", "", title)

    # converts snake case to capitlized with spaces, e.g. linked_list -> Linked List
    formatted_title = " ".join(map(lambda x: x.capitalize(), title_stem.split("_")))

    return f"{prefix} [{formatted_title}]({path})\n"


def generate_directory():
    """Walks project directory and generates markdown links for each section."""

    EXCLUDED_PATHS = "__|.git|tests|scripts|pytest|solutions|utils"

    with open("DIRECTORY.md", "w") as file:
        for root, _, files in os.walk("."):
            if not re.search(EXCLUDED_PATHS, root) and root != ".":
                file.write(get_markdown_link(root, f"{root}/README.md", "##"))

                file.write("\n")

                for _file in files:
                    if not re.search("__init__.py|README.md", _file):
                        file.write(get_markdown_link(_file, f"{root}/{_file}", "-"))

                file.write("\n")

        file.close()


generate_directory()
