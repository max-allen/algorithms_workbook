import os, sys

METADATA = {
    "river_sizes": {
        "prompt": [
            "# Given a two dimensional array of 0 and 1s, return an array of the sizes of all",
            "# rivers contained within the input matrix.",
            "# A river consists of any number of 1s either horizontally or vertically adjacent.",
            "# The number of adjacent 1s forming a river determine its size.",
        ],
        "signature": "def river_sizes(matrix):",
    }
}


def reset_exercise(filename):
    # TODO: move to constants file after removing relative module name '.scripts'
    EXCLUDED_PATHS = "__|.git|tests|scripts|pytest|utils"

    name_with_ext = f"{filename}.py"
    for dirpath, dirnames, filenames in os.walk("."):
        if name_with_ext in filenames:
            filepath = f"{dirpath}/{filename}.py"
            # NOTE: contents of existing file are erased when opening new file with
            # same name. See: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
            with open(filepath, "w") as f:
                metadata = METADATA[filename]
                lines = [f"{line}\n" for line in metadata["prompt"]]
                f.writelines([*lines, *["\n", "\n", metadata["signature"]]])


reset_exercise(sys.argv[1])
