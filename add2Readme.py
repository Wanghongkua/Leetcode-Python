import sys
import subprocess
import argparse
from termcolor import colored


def generateURL(problem_name: str, concatenating_char: str) -> str:
    """ Generate URL for question, answer and code.  """
    URL = "https://leetcode.com/problems/"
    git_link = ""
    git_link = problem_name.replace(" ", "-").lower()
    git_link = URL + git_link + "/"
    return git_link


def capitalizeArg(arg: str) -> str:
    """ capitalize argument """
    args = arg.split(" ")
    args = [arg.capitalize() for arg in args]
    return " ".join(args)


def getArg(argName: str) -> str:
    """ Get the argument by it's name from input """
    arg = None
    while True:
        end = False
        output_string = "Please specify " + colored(argName, "yellow") \
            + " of the problem: "
        arg = input(output_string)
        print("The inputed", colored(argName, "yellow"), "is:",
              colored(arg, "red"))
        print("Are you sure?", end=" ")
        end = input("Y for yes, N for no: ")
        if end == "Y" or end == "y":
            break
    return arg


def findInsertPosition(contents, tag_line, diff_line):
    """Find the index of tag_line"""
    last_empty_line = 0
    found_tag = False
    found_diff = False
    repeat = False
    for index, content in enumerate(contents):
        if content == "\n":
            last_empty_line = index
            # Insert before this line
            if found_diff:
                if not repeat:
                    repeat = True
                else:
                    break

        if not found_tag:
            if content == tag_line:
                found_tag = True
        else:
            if content == diff_line:
                found_diff = True
            # Found tag but not diff
            elif content[:4] == "### ":
                break

    title_line = "|#|Title|Explanation|Code|BasicIdeas|\n"
    table_line = "|-|-----|-----------|----|----------|\n"
    # Tag not found
    if not found_tag:
        new_content = ["\n", tag_line, "\n", diff_line, "\n",
                       title_line, table_line]
        contents = contents[:last_empty_line] + new_content + \
            contents[last_empty_line:]
        return contents, last_empty_line + 7
    # tag exist, but difficulty doesn't
    elif not found_diff:
        new_content = ["\n", diff_line, "\n", title_line, table_line]
        contents = contents[:last_empty_line] + new_content + \
            contents[last_empty_line:]
        return contents, last_empty_line + 5
    # Both exist
    else:
        return contents, last_empty_line


def sortFunc(line: str):
    """Sorting function for links"""
    if "_" in line:
        return int(line[1:line.find("_")])
    else:
        return int(line[1:line.find("]")])


def add2Readme(tag: str, difficulty: str, number: str, problem_name: str):
    """ Add problem to readme

    : tag          : The category of the problem
    : difficulty   : The difficulty of the problem
    : number       : The index of the problem
    : problem_name : The name of the problem

    """
    #  Format inputs
    tag = capitalizeArg(tag)
    #  problem_name = capitalizeArg(problem_name)

    # Construct links
    concatenating_char = "_"

    tag_folder = tag.replace(" ", "_")
    diff_folder = difficulty.capitalize()
    current_folder = tag_folder + "/" + diff_folder + "/"

    git_link = generateURL(problem_name, concatenating_char)

    answer = number + "_a"
    code = number + "_c"

    list_line = "|" + number + \
        "|" + "[" + problem_name + "][" + number + "]" + \
        "|" + "[Answer][" + answer + "]" + \
        "|" + "[Python][" + code + "]||" + "\n"
    url_line = "[" + number + "]: " + git_link + "\n"
    answer_line = "[" + answer + "]: " + current_folder + \
        problem_name.replace(" ", "_") + "/" \
        + "\n"
    code_line = "[" + code + "]: " + current_folder + \
        problem_name.replace(" ", "_") + "/" + \
        problem_name.replace(" ", "_") + ".py\n"

    # Write new file into "readme.md"
    tag_line = "### " + tag + "\n"
    diff_line = "#### " + difficulty.capitalize() + "\n"
    file_path = "readme.md"

    print("Opening \"readme.md\"")
    with open(file_path, "r+") as f:
        contents = f.readlines()
        contents, insert_position = findInsertPosition(
            contents, tag_line, diff_line)

        print("Writing links for readme")
        contents.insert(insert_position, list_line)
        contents.append(url_line)
        contents.append(answer_line)
        contents.append(code_line)
        last_empty_index = len(contents) - 1
        while last_empty_index >= 0:
            if contents[last_empty_index] == "\n":
                contents[last_empty_index + 1:] = sorted(contents[
                    last_empty_index + 1:], key=sortFunc)
                break
            last_empty_index -= 1
        f.seek(0)
        f.writelines(contents)
        print("Closing \"readme.md\"")

    #  print("start creating files for current question")
    #  bash_script = ["./add_new.sh"]
    #  val = subprocess.run(bash_script + sys.argv[2:], cwd=current_folder)
    #  print("The bash script result is:", val)


if __name__ == "__main__":
    diffValues = ["easy", "medium", "hard"]

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tag", help="The category of the problem")
    parser.add_argument("-d", "--difficulty", choices=diffValues,
                        help="The difficulty level of the problem")
    parser.add_argument("-i", "--index", type=int,
                        help="The index of the problem")
    parser.add_argument("-n", "--name", help="Name of the problem")
    args = parser.parse_args()

    tag = args.tag
    if tag is None:
        tag = getArg("category")

    difficulty = args.difficulty
    while difficulty is None:
        difficulty = getArg("difficulty")
        if difficulty not in diffValues:
            difficulty = None
            print("Please select difficulty from these values: " +
                  colored(" ".join(diffValues), "blue") + ".")

    problem_name = args.name

    number = str(args.index)

    add2Readme(tag, difficulty, number, problem_name)
