from .constructor.introduction_process import introduction_process
from .constructor.first_calculator import first_calculator
from .constructor.second_calculator import second_calculator
from .constructor.third_calculator import third_calculator
from .constructor.search_calculator import search_calculator


def start() -> None:
    while True:
        command = introduction_process()
        if command == "1":
            first_calculator()
        elif command == "2":
            second_calculator()
        elif command == "3":
            third_calculator()
        elif command == "4":
            search_calculator()
        elif command == "5":
            exit()
        else:
            print("\nCommand not found! Try again!\n\n")
