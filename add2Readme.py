import argparse
import json
import os
import subprocess
from sys import exit
from typing import Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import requests
#  from bs4 import BeautifulSoup
from termcolor import colored


def generateURL(problem_name: str) -> str:
    """ Generate URL for question, answer and code.  """
    URL = "https://leetcode.com/problems/"
    git_link = ""
    git_link = problem_name.replace(" ", "-").lower()
    git_link = URL + git_link + "/"
    return git_link


def capitalizeArg(arg: str) -> str:
    """ capitalize argument """
    arg_list = arg.split(" ")
    arg_list = [arg.capitalize() for arg in arg_list]
    return " ".join(arg_list)


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

    title_line = "|#|Title|Explanation|Code|Basic Ideas|\n"
    table_line = "|-|-----|-----------|----|-----------|\n"
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


def getCurrentFolder(tag: str, difficulty: str) -> str:
    """Get current working directory"""
    tag_folder = tag.replace(" ", "_")
    diff_folder = difficulty.capitalize()
    return tag_folder + "/" + diff_folder + "/"


def add2Readme(tag: str, difficulty: str, number: str, problem_name: str):
    """ Add problem to readme

    :tag:          The category of the problem
    :difficulty:   The difficulty of the problem
    :number:       The index of the problem
    :problem_name: The name of the problem

    """
    #  Format inputs
    tag = capitalizeArg(tag)

    current_folder = getCurrentFolder(tag, difficulty)

    git_link = generateURL(problem_name)

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


def createFile(current_folder: str, problem_name: str):
    """Create Problem Folder"""
    print("Do you want to create file for " + colored(problem_name, "red") +
          " within folder " + colored(current_folder, "red"))
    create_file = input("Y for yes, N for no: ")
    if create_file == "Y" or create_file == "y":
        pass
    else:
        return
    if not os.path.isdir(current_folder):
        print("start creating " + current_folder + " for current question")
        subprocess.run(["mkdir", "-p", current_folder])
        print("Done")

    print("start creating files for current question")
    bash_script = ["../../add_new.sh"]
    val = subprocess.run(bash_script + problem_name.split(" "),
                         cwd=current_folder)
    print("The bash script result is:", val)


def existInReadme(number: int) -> int:
    """ Find existence of current question in readme.md """
    file_path = "readme.md"
    with open(file_path, "r") as f:
        contents = f.readlines()
        index = len(contents) - 1
        line = contents[index]
        while line != "\n":
            if "_" not in line:
                line_number = int(line[1:line.find("]")])
                if line_number == number:
                    return 1
            index -= 1
            line = contents[index]
    return 0


def existInFile(current_folder: str, problem_name: str) -> int:
    """Test existence of problem folder"""
    problem_folder = current_folder + "/" + problem_name.replace(" ", "_")
    if os.path.isdir(problem_folder):
        return 1
    return 0


def getQuestionDescription(problem_name: str) -> Dict[str, str]:
    """Get the question description and write to readme file

    :problem_name: the name of the problem
    :return:       both the description and examples of the question

    """
    question = {"description": "", "examples": ""}
    return question


def write2Readme(question: Dict[str, str],
                 current_folder: str, problem_name: str):
    """Write problem description to readme.md file

    :question: description of the question
    :current_folder: current working folder
    :problem_name: name of the question

    """
    pass


def findOnline(problem_name: str, number: str):
    """ Find problem by it's number on LeetCode

    :problem_name: name of the problem
    :number:       index of the problem
    :returns:      The question info for correct, False for incorrect

    """
    # LeetCode API URL to get json of problems on algorithms categories
    ALGORITHMS_ENDPOINT_URL = "https://leetcode.com/api/problems/algorithms/"

    # Load JSON from API
    algorithms_problems_json = requests.get(ALGORITHMS_ENDPOINT_URL).content
    algorithms_problems_json = json.loads(algorithms_problems_json)

    # List to store question_title_slug
    for child in algorithms_problems_json["stat_status_pairs"]:
        # Only process free problems
        if not child["paid_only"]:
            question_id = child["stat"]["frontend_question_id"]
            question_title = child["stat"]["question__title"]
            if str(question_id) == number:
                if question_title != problem_name:
                    print("Question name is incorrect")
                    return False
                return child
    print("ID not found, please check if ", colored(number, "red"),
          " is the desired index")
    return False


def belong2tag(number: str, tag: str) -> bool:
    """verify which problem is belong to the category provided

    :number: The index of the problem
    :tag: The category of the problem
    :returns: Whether problem belong to the category

    """
    CATEGORY_BASE_URL = "https://leetcode.com/tag/"

    # Find problem on leetcode webpage
    url = CATEGORY_BASE_URL + tag.replace(" ", "-").lower()

    driver = webdriver.Chrome()
    driver.get(url)
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "reactable-data"))
        )
        questions = table.find_elements_by_tag_name("tr")
        for question in questions:
            question_id = question.find_elements_by_tag_name("td")[1]
            if question_id.text == number:
                driver.quit()
                return True
        print("The tag: ", colored(tag, "red"), " provided doesn't match")
        driver.quit()
    except Exception:
        print("The tag: ", colored(tag, "red"), " provided doesn't exist")
        driver.quit()
        return False
    return False


if __name__ == "__main__":
    diffValues = ["easy", "medium", "hard"]

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tag", help="The category of the problem")
    parser.add_argument("-i", "--index", type=int,
                        help="The index of the problem")
    parser.add_argument("-n", "--name", help="Name of the problem")
    args = parser.parse_args()

    # Get the category of the problem
    tag = args.tag
    if tag is None:
        tag = getArg("category")

    problem_name = args.name

    number = str(args.index)

    # Validate the problem's name and difficulty by its number
    result = findOnline(problem_name, number)
    if not result:
        exit()

    # Validate tag based on info provided
    while not belong2tag(number, tag):
        tag = getArg("tag")

    # Get difficulty
    difficulty = diffValues[result["difficulty"]["level"] - 1]

    if not existInReadme(int(number)):
        add2Readme(tag, difficulty, number, problem_name)
    tag = capitalizeArg(tag)
    current_folder = getCurrentFolder(tag, difficulty)
    if not existInFile(current_folder, problem_name):
        createFile(current_folder, problem_name)
    question = getQuestionDescription(problem_name)
    write2Readme(question, current_folder, problem_name)
