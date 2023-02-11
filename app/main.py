
import parsero as prs
import sys
import os

sys.setrecursionlimit(100000*10)

def main():

    print()
    
    user_input = input("Please enter the relative path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens = prs.load_code(user_input)
    prs.parse(tokens)

main()
