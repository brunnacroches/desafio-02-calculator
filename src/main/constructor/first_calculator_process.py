from src.views.first_calculator_view import FirstCalculatorView
from src.controllers.first_calculator_controller import FirstCalculatorController


def first_calculator_process() -> None:
    first_calculator_view = FirstCalculatorView
    first_calculator_controller = FirstCalculatorController

    first_calculator_informations = first_calculator_view()
    response = first_calculator_controller.first(first_calculator_informations)

    if response["Success"]:
        first_calculator_view.first_calculator_success(response["value"])
    else:
        first_calculator_view.first_calculator_fail(response["error"])
