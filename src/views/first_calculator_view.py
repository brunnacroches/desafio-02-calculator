import os


class RegistryFirstCalculatorViews:
    def registry_first_calculator_page(self) -> None:
        self.__clear()

        print("Registry the results calculator \n\n")
        number = input("Add the results calculator")

        return number

    def registry_first_calculator_success(self, calculator_number: any) -> None:
        self.__clear()

        message = """
          Calculators results successfully registered!
          * Infos:
            Calculator ID: {}
            Resultus Calculator: {}
        """.format(
            calculator_number.id, calculator_number.calculators
        )
        print(message)

    def registry_first_calculator_fail(self) -> None:
        self.__clear()

        message = """
          There was an error when show the number the calculator, check the numbers or de counts 
        """
        print(message)

    def __clear(self):
        os.system("cls|clear")
