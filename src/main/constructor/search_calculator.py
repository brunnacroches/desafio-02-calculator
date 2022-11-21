from src.views.search_calculator_view import SearchCalculatorView
from src.controllers.search_calculator_controller import SearchCalculatorController


def search_calculator_process() -> None:
    search_calculator_view = SearchCalculatorView
    search_calculator_controller = SearchCalculatorController

    search_calculator_informations = search_calculator_view()
    response = search_calculator_controller.find(search_calculator_informations)

    if response["Success"]:
        search_calculator_view.search_calculator_success(response["registry"])
    else:
        search_calculator_view.search_calculator_fail(response["error"])
