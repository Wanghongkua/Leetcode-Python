import sys
import subprocess


current_folder = "Array_Easy/"
concatenatingChar = "_"
url = "https://leetcode.com/problems/"
gitLink = ""
folder_name = ""

number = sys.argv[1].replace(".", "")

folder_name = concatenatingChar.join(sys.argv[2:])

gitLink = folder_name.replace(concatenatingChar, "-").lower()
url = url + gitLink + "/"

file_path = "readme.md"
last_empty_line = 0
answer = number + "_a"
code = number + "_c"

list_line = "|" + number + \
    "|" + "[" + " ".join(sys.argv[2:]) + "][" + number + "]" + \
    "|" + "[Answer][" + answer + "]" + \
    "|" + "[Python][" + code + "]||" + "\n"
url_line = "[" + number + "]: " + url + "\n"
answer_line = "[" + answer + "]: " + current_folder + folder_name + "/" + "\n"
code_line = "[" + code + "]: " + current_folder + folder_name + "/" + folder_name + ".py\n"

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
