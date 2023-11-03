# -*- coding: UTF-8 -*-
# ToolName   : DirMaze
# Author     : Omar Menshawy
# Version    : 1.0
# Github     : https://github.com/OmarMenshawy/DirMaze
# Contact    : omar-menshawy@proton.me
# Description: A tool that can make a maze of folders in Python to store sensitive files
# 1st Commit : 26/09/2023
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit

from random import randint
from os import mkdir, chdir, listdir
from pathlib import Path


# words lists
words_a = open(Path("words_list", "words_list_A.txt")).readlines()
words_b = open(Path("words_list", "words_list_B.txt")).readlines()
words_c = open(Path("words_list", "words_list_C.txt")).readlines()
words_d = open(Path("words_list", "words_list_D.txt")).readlines()
words_e = open(Path("words_list", "words_list_E.txt")).readlines()
words_list = {"A": words_a, "B": words_b, "C": words_c, "D": words_d, "E": words_e}


# shuffle lists
def shuffle(your_list):
    list_type = type(your_list)
    return list_type(set(your_list))


words_a = shuffle(words_a)
words_b = shuffle(words_b)
words_c = shuffle(words_c)
words_d = shuffle(words_d)
words_e = shuffle(words_e)


maze_path = ""
# where files are located
maze_code = 0


def create_parent_dir():
    maze_path = input("Type maze path: ")
    try:
        mkdir(Path(maze_path, "maze"))
    except FileExistsError:
        print(
            f"{maze_path} is already has a folder named `maze`, delete it or move it to another folder"
        )
        exit()
    chdir(Path(maze_path, "maze"))


# variables for loading
ratio = 0
count = 0


def create_maze():
    for letter, words in words_list.items():
        mkdir(words.pop(0).replace("\n", ""))
        global count
        count += 1
        if count == 970:
            global ratio
            ratio += 1
            count = 0
            print(f"Creating Maze... {ratio}%", end="\r")


def end():
    maze_code = str(randint(0, 5555555))
    numbers = {
        "0": "1st",
        "1": "1st",
        "2": "2nd",
        "3": "3rd",
        "4": "4th",
        "5": "5th",
    }
    print("maze created successfully!")
    files_path = ""
    for num in maze_code:
        try:
            files_path = files_path + numbers[num] + " "
        except KeyError:
            files_path = files_path + "1st" + " "
            maze_code = maze_code.replace(num, "1", 1)
    print(f"Your maze code is {maze_code}, save it or you'll never find your files!")
    print(f"put your sensitive files into the {files_path}directory")


def main():
    create_parent_dir()
    print(f"Creating Maze... 0%", end="\r")
    create_maze()
    for directory1 in listdir():
        # 1st dir
        chdir(directory1)
        create_maze()
        for directory2 in listdir():
            # 2nd dir
            chdir(directory2)
            create_maze()
            for directory3 in listdir():
                # 3rd dir
                chdir(directory3)
                create_maze()
                for directory4 in listdir():
                    # 4th dir
                    chdir(directory4)
                    create_maze()
                    for directory5 in listdir():
                        # 5th dir
                        chdir(directory5)
                        create_maze()
                        for directory6 in listdir():
                            # 6th dir
                            chdir(directory6)
                            create_maze()
                            chdir("..")
                        chdir("..")
                    chdir("..")
                chdir("..")
            chdir("..")
        chdir("..")
    chdir("..")
    end()


if __name__ == "__main__":
    main()
