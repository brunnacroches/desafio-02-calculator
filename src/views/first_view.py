def introduction_page():
    message = """
    Calculator System

    * First Calculator - 1
    * Second Calculator - 2
    * Third Calculator - 3
    * Search Calculator - 4
    * Exit - 5
  """
    print(message)
    command = input("Command: ")

    return command
