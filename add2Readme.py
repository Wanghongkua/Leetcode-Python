import sys
import subprocess
import argparse
from termcolor import colored


def generateURL(problem_name: str, concatenating_char: str) -> str:
    """ Generate URL for question, answer and code.  """
    URL = "https://leetcode.com/problems/"
    git_link = ""
    git_link = problem_name.replace(concatenating_char, "-").lower()
    git_link = URL + git_link + "/"
    return git_link


def computeFolderName(arg: str, concatenating_char: str) -> str:
    """ Compute folder name """
    args = arg.split(" ")
    args = [arg.capitalize() for arg in args]
    return concatenating_char.join(args)


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


def add2Readme(tag: str, difficulty: str, number: str, problem_name: str):
    """ Add problem to readme

    : tag          : The category of the problem
    : difficulty   : The difficulty of the problem
    : number       : The index of the problem
    : problem_name : The name of the problem

    """
    concatenating_char = "_"

    tag_folder = computeFolderName(tag, concatenating_char)
    diff_folder = difficulty.capitalize()

    current_folder = tag_folder + "/" + diff_folder + "/"

    git_link = generateURL(problem_name, concatenating_char)

    #  current_folder = computeFolderName(tag, concatenating_char)

    file_path = "readme.md"
    last_empty_line = 0
    answer = number + "_a"
    code = number + "_c"

    list_line = "|" + number + \
        "|" + "[" + " ".join(sys.argv[2:]) + "][" + number + "]" + \
        "|" + "[Answer][" + answer + "]" + \
        "|" + "[Python][" + code + "]||" + "\n"
    url_line = "[" + number + "]: " + git_link + "\n"
    answer_line = "[" + answer + "]: " + current_folder + problem_name + "/" \
        + "\n"
    code_line = "[" + code + "]: " + current_folder + problem_name + "/" + \
        problem_name + ".py\n"

    print("Opening \"readme.md\"")
    with open(file_path, "r+") as f:
        contents = f.readlines()
        for index, line in enumerate(contents):
            if line == "\n":
                last_empty_line = index
        print("Writing links for readme")
        contents.insert(last_empty_line, list_line)
        contents.append(url_line)
        contents.append(answer_line)
        contents.append(code_line)
        f.seek(0)
        f.writelines(contents)
        print("Closing \"readme.md\"")

    print("start creating files for current question")
    bash_script = ["./add_new.sh"]
    val = subprocess.run(bash_script + sys.argv[2:], cwd=current_folder)
    print("The bash script result is:", val)


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

    number = args.number

    add2Readme(tag, difficulty, number, problem_name)


#  current_folder = "Array_Easy/"
#  url = "https://leetcode.com/problems/"
#  git_link = ""
#  problem_name = ""

#  number = sys.argv[1].replace(".", "")

#  problem_name = concatenating_char.join(sys.argv[2:])

#  git_link = problem_name.replace(concatenating_char, "-").lower()
#  url = url + git_link + "/"
