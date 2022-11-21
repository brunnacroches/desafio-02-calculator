class __CalculatorEnrollment:
    def __init__(self) -> None:
        self.calculators = []
        self.first_calculator = []
        self.second_calculator = []
        self.third_calculator = []
        self.search_calculator = []

        def count_first_calculator(self) -> int:
            return len(self.first_calculator)

        def count_second_calculator(self) -> int:
            return len(self.second_calculator)

        def count_third_calculator(self) -> int:
            return len(self.third_calculator)

        def count_search_calculator(self) -> int:
            return len(self.search_calculator)

        def registry_first_calculator(self, first_calculator: any) -> None:
            self.first_calculator.append(first_calculator)

        def registry_second_calculator(self, second_calculator: any) -> None:
            self.second_calculator.append(second_calculator)

        def registry_third_calculator(self, third_calculator: any) -> None:
            self.third_calculator.append(third_calculator)

        def registry_search_calculator(self, search_calculator: any) -> None:
            self.search_calculator.append(search_calculator)

        def get_first_calculator(self, first_calculator_id: any) -> any:
            for registry in self.first_calculator:
                if registry.calculator == first_calculator_id:
                    return registry

            return None

        def get_second_calculator(self, second_calculator_id: any) -> any:
            for registry in self.second_calculator:
                if registry.calculator == second_calculator_id:
                    return registry

            return None

        def get_third_calculator(self, third_calculator_id: any) -> any:
            for registry in self.third_calculator:
                if registry.calculator == third_calculator_id:
                    return registry

            return None

        def get_search_calculator(self, search_calculator_id: any) -> any:
            for registry in self.search_calculator:
                if registry.calculator == search_calculator_id:
                    return registry

            return None

        def get_calculators_by_id(self, calculators_id: any):
            calculators = []
            for registry in self.calculators:
                if registry.calculators.id == calculators_id:
                    calculators.append(registry)

            return calculators


calculator_enrollemnt = __CalculatorEnrollment
