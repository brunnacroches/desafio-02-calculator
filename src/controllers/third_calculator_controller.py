# * Terceira Calculadora → N numeros são colocados como entrada.
# Caso sua soma forem maiores que sua multiplicação, 
# é apresentado um informação de sucesso ao usuario.
# Caso contrário, é apresentado uma informação de falha.


class ThirdCalculatorController:

    def third(self, numbers: any):
        lista_de_numeros = []
        somatorio = 0
        for numero_da_lista in lista_de_numeros:
            somatorio += numero_da_lista

        if somatorio > lista_de_numeros:
            print("Success")
        else:
             print("Error")

        return {"success": True, "value": number}


# usar o if else