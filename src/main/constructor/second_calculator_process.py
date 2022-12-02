from src.views.second_calculator_view import SecondCalculatorView
from src.controllers.calculators.second_calculator import SecondCalculatorController


def second_calculator_process() -> None:
    second_calculator_view = SecondCalculatorView
    second_calculator_controller = SecondCalculatorController

    second_calculator_informations = second_calculator_view()
    response = second_calculator_controller.find(second_calculator_informations)

    if response["Success"]:
        second_calculator_view.second_calculator_success(response["registry"])
    else:
        second_calculator_view.second_calculator_fail(response["error"])
