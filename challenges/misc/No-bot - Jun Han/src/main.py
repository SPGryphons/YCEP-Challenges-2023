import sys
import readline
import functools
from app.quiz import *
from app.challenge import *
from time import perf_counter
from core.banner import *
from core.status import Status
from core.custom_exception import *

CMD = ['start', 'help']

def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                output_values = func(*args, **kwargs)
                break
            except IndexError:
                print("Oops guess thats wrong.")
            except (KeyboardInterrupt, ExitProgram):
                print("\nBye Bye :)")
                sys.exit()
            except ValueError:
                print('Oops guess your input is wrong. oh well')
                sys.exit()
            except:
                print("Welp guess you typo'd, can't help with that")
                continue
        return output_values
    return wrapper

def input_handler(type=None):
    '''
    Handles user's inputs within this terminal
    '''
    exit_commands = ['q', 'quit', 'exit']
    user_input = input("\n\033[94mNo-bot > \x1b[0m")
    
    if user_input.lower() in exit_commands:
        raise ExitProgram
    
    if type == 'hash':
        return user_input

    return int(user_input)

@error_handler
def main():
    print(welcome)
    print(begin)

    q_list = questions()
    for i, element in enumerate(q_list):
        if i % 100 == 0:
            print("CAPCHA Challenge (provide last 8 hash values): ")
            c = challenge()
            answer = input_handler('hash')            
            if answer != c:
                print("Congratulations on your failure")
                raise ExitProgram

        print(element[0])
        answer = input_handler()
        if answer != element[1]:
            print("Congratulations on your failure")
            raise ExitProgram
    
    if True:
        win()

if __name__ == "__main__":
    main()