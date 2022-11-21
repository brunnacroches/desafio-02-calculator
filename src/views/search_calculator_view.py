import os


class SearchCalculatorViews:
    def search_calculators_views(self) -> any:
        self.__clear

        print("Search Registry Calculator \n\n")
        calculators = input("Set the calculators of the counts to search: ")

        return calculators

    def search_calculators_success(self, registry_calculator: any) -> None:
        self.__clear()

        message = """
            Registration Calculator
            * Infos:
              ID Calculator: {}
              Name Calculator: {}
              Number Calculator: {}
              Counts Calculator: {}
          """.format(
            registry_calculator["id"],
            registry_calculator["number"],
            registry_calculator["counts"],
            registry_calculator["name"],
        )
        print(message)

    def search_calculators_fail(self, error: any) -> None:
        self.__clear()

        message = """
        There was an errpr fetching the song.
        {}
      """.format(
            error
        )
        print(message)

    def __clear(self):
        os.sytem("cls||clear")
