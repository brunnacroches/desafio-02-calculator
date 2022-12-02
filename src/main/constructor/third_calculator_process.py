from src.views.third_calculator_view import ThirdCalculatorView
from src.controllers.calculators.third_calculator import ThirdCalculatorController


def third_calculator_process() -> None:
    third_calculator_view = ThirdCalculatorView
    third_calculator_controller = ThirdCalculatorController

    third_calculator_informations = third_calculator_view()
    response = third_calculator_controller.find(third_calculator_informations)

    if response["Success"]:
        third_calculator_view.third_calculator_success(response["registry"])
    else:
        third_calculator_view.third_calculator_fail(response["error"])
