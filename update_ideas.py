import re
from os import listdir
from os.path import isfile, join


def findCommentLine(contents):
    """
    find the lines that are comments
    """
    comments = ""
    isComment = 0
    count = 1
    for _, line in enumerate(contents):
        result = re.match("^ *\"\"\"\n$", line)
        if result and not isComment:
            isComment = 1
        elif isComment == 1:
            if count > 1:
                comments = comments + "<br>" + str(count) + ". "
            else:
                comments += "1. "
            count += 1
            comments += re.search(r'^ *([^ ]+.*)\n', line).group(1)
            isComment = 2
        elif isComment == 2:
            isComment = 0
    return comments


def findPosition(line):
    """
    find the second of the last "|"
    """
    result = re.search(r"\|[^\|]*\|\n", line).start()
    return result


#  update basic idea
current_folder = "Array_Easy/"
onlyFolders = [
    f for f in listdir(current_folder) if not isfile(join(current_folder, f))
]

with open("readme.md", "r+") as index_file:
    index_contents = index_file.readlines()
    for folder_name in onlyFolders:
        file_path = join(current_folder, folder_name, folder_name + ".py")
        comments = ""
        with open(file_path, "r") as f:
            contents = f.readlines()
            comments = findCommentLine(contents)
        for index, line in enumerate(index_contents):
            if folder_name.replace("_", " ") in line and "|" in line:
                position = findPosition(line)
                line = line[:position + 1] + comments + "|\n"
                index_contents[index] = line
    index_file.seek(0)
    index_file.truncate()
    index_file.writelines(index_contents)
