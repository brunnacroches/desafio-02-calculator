from .constructor.introduction_process import introduction_process
from .constructor.first_calculator_process import first_calculator_process
from .constructor.second_calculator_process import second_calculator_process
from .constructor.third_calculator_process import third_calculator_process


def start() -> None:
    while True:
        command = introduction_process()
        if command == "1":
            first_calculator_process()
        elif command == "2":
            second_calculator_process()
        elif command == "3":
            third_calculator_process()
        elif command == "4":
            exit()
        else:
            print("\nCommand not found! Try again!\n\n")
