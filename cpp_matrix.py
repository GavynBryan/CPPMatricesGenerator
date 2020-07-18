print("Generate a C++ matrix of zeroes!\n"
      "Enter the rows and columns, separated by a comma. 'rows, columns'")
finished = False

while not finished:
    print("Terminate with 'quit'.")
    command = input()
    if ',' in command:
        command.replace(" ", "")
        dimensions = command.split(',')

        x = int(dimensions[0])
        y = int(dimensions[1])

        res = "int matrix[{0}][{1}] = \n{{".format(x, y)
        row = "{"
        for i in range(0, y):
            row += "0"
            if i < y - 1:
                row += ","
        row += "}"

        for i in range(0, x):
            res += row
            if i < x - 1:
                res += ","
            res += "\n"

        res += "};"
        print(res)
    else:
        if command == "quit":
            finished = True


print("Thank you for your interest in creating C++ matrices. :)")