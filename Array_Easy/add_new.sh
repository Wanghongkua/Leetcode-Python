#!/bin/sh

file=""
python_file=".py"
readme_file="readme.md"
gitignore=".gitignore"
gitignore_content=".gitignore\ntags"
concatenatingChar="_"
i=0
for Token in "$@" ; do
    if [[ "$i" -eq "0" ]]; then
        file="$Token"
        i=1
    else
        file="$file$concatenatingChar$Token"
    fi
done
python_file="$file/$file$python_file"
readme_file="$file/$readme_file"
gitignore="$file/$gitignore"


if [[ -d $file ]]; then
    echo "Directory already exists, please check to avoid replace."
else
    mkdir $file
    touch "$python_file"
    touch "$readme_file"
    touch "$gitignore"
    echo "$gitignore_content" > "$gitignore"
fi
