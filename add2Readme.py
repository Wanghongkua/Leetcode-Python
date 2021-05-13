import sys
import subprocess
import argparse
from termcolor import colored


def generateURL(problem_name: str, concatenatingChar: str) -> str:
    """ Generate URL for question, answer and code.  """
    URL = "https://leetcode.com/problems/"
    gitLink = ""
    gitLink = problem_name.replace(concatenatingChar, "-").lower()
    gitLink = URL + gitLink + "/"
    return gitLink


def getArg(argName: str) -> str:
    """ Get the argument by it's name from input """
    arg = None
    while True:
        end = False
        output_string = "Please specify " + argName + " of the problem: "
        arg = input(output_string)
        print("The inputed", argName, "is:", colored(arg, "red"))
        print("Are you sure?", end=" ")
        end = input("Y for yes, N for no: ")
        if end == "Y" or end == "y":
            break
    return arg


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tag", help="The category of the problem")
parser.add_argument("-d", "--difficulty", choices=["easy", "medium", "hard"],
                    help="The difficulty level of the problem")
parser.add_argument("-i", "--index", type=int, help="The index of the problem")
parser.add_argument("-n", "--name", help="Name of the problem")
args = parser.parse_args()

tag = args.tag
if tag is None:
    tag = getArg("category")

difficulty = args.difficulty
if difficulty is None:
    difficulty = getArg("difficulty")

print(tag, difficulty)

sys.exit()

concatenatingChar = "_"

#  current_folder = computeFolderName(args.tags, args.difficulty,
#                                     concatenatingChar)

problem_name = args.name

number = args.number

gitLink = generateURL(problem_name, concatenatingChar)

file_path = "readme.md"
last_empty_line = 0
answer = number + "_a"
code = number + "_c"

list_line = "|" + number + \
    "|" + "[" + " ".join(sys.argv[2:]) + "][" + number + "]" + \
    "|" + "[Answer][" + answer + "]" + \
    "|" + "[Python][" + code + "]||" + "\n"
url_line = "[" + number + "]: " + gitLink + "\n"
answer_line = "[" + answer + "]: " + current_folder + problem_name + "/" + "\n"
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

print("start bash script")
bash_script = ["./add_new.sh"]
val = subprocess.run(bash_script + sys.argv[2:], cwd=current_folder)
print("The bash_script result is:", val)

#  current_folder = "Array_Easy/"
#  url = "https://leetcode.com/problems/"
#  gitLink = ""
#  problem_name = ""

#  number = sys.argv[1].replace(".", "")

#  problem_name = concatenatingChar.join(sys.argv[2:])

#  gitLink = problem_name.replace(concatenatingChar, "-").lower()
#  url = url + gitLink + "/"
