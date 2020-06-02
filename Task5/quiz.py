from contextlib import contextmanager
import os, sys
from timer import Timer
from user_session import User

@contextmanager
def open_file(filename: str, mode: str):
    """File content generator with context manager protocol"""
    content = open(filename, mode)
    try:
        yield content
    finally:
        content.close()

def validate_quiz(quiz_path: str):
    """This function is used to validate the content of the given directory before we run the quiz"""
    try:
        if (len(os.listdir(quiz_path)) == 0):
            print("Directory is empty")
            return False
        elif not any([True for file in os.scandir(quiz_path) if file.name.endswith(".txt")]):
            print("Couldn't find text files in given directory!")
            return False
        else:
            return True
    except OSError:
        print("Error occured while attempting to open files in given directory!")
        return False

def main():
    user = User()
    with Timer('Quiz', user.timer_file_name):
        for file in os.scandir(quiz_path):
            if (file.name.endswith( ".txt" ) \
                and not file.name.endswith("_answers.txt") \
                    and not file.name.endswith("_timer.txt")):
                        with open_file(file, 'r') as questions, Timer(file.name, user.timer_file_name):
                            for line in questions:
                                user.quiz_answers['%s' %line.strip()] = input(f"{line}Answer: ")

    with open_file(user.answers_file_name, 'a+') as answer_file:
        for key, value in user.quiz_answers.items():
            answer_file.write(f'{key}: {value}\n')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("It looks like you didn't provide the quiz system path as command line parameter..")
        print('Program needs a directory with question files to run the quiz!')
        answer = input('Do you want to enter the system path to the quiz directory? (Yes/No): ')
        if answer == 'Yes':
            quiz_path = input('Please enter the full system path to quiz directory:\nPath: ')
        else:
            sys.exit(0)
    else:
        quiz_path = sys.argv[1]
    
    flag = True
    while flag:
        if validate_quiz(quiz_path):
            flag = False
        else:
            answer = input('Do you want to enter another system path to the quiz directory? (Yes/No): ')
            if answer == 'Yes':
                quiz_path = input('Please enter the full system path to quiz directory:\nPath: ')
            else:
                sys.exit(0)
    main()



            
            



     