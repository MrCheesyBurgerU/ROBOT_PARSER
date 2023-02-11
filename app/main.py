
import parsero as prs
import sys
import os

sys.setrecursionlimit(100000*10)

def main():

    print()
    print("Note: If your file contains procedures without parameters, please add a space between the parameter bars (| |),")
    print("otherwise the program will fail")
    print()
    print("Please put the files to check in the test folder")
    print()
    
    user_input = input("Enter the relative path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens = prs.load_code(user_input)
    prs.parse(tokens)

main()
