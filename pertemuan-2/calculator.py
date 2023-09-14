PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVISION = "/"


def calculate(n1=0, operand=PLUS, n2=0):
    if (operand == PLUS):
        return n1 + n2
    if (operand == MINUS):
        return n1 - n2
    if (operand == TIMES):
        return n1 * n2
    if (operand == DIVISION):
        return n1 / n2
    return False


def perfom_calculation(list=[]):
    temp_list = []
    current_result = 0
    current_result_index = 0

    # print(list)

    # recursive control
    if (len(list) <= 2):
        return list[0]

    # looping to calculate Times (*) or Division (/) First
    index = 0
    while index < len(list):
        if (list[index] == TIMES or list[index] == DIVISION):
            operand = list[index]
            n1 = float(list[index - 1]) or 0
            n2 = float(list[index + 1]) or 0
            current_result = calculate(n1, operand, n2)
            current_result_index = index
            break
        index += 1

    if (current_result):
        index = 0
        while index < len(list):
            if (index == current_result_index - 1):
                temp_list.append(current_result)
            elif (index != current_result_index + 1 and index != current_result_index):
                temp_list.append(list[index])
            index += 1
        return perfom_calculation(temp_list)

    # looping to calculate Plus (+) or Minus (-)
    index = 0
    while index < len(list):
        if (list[index] == PLUS or list[index] == MINUS):
            operand = list[index]
            n1 = float(list[index - 1]) or 0
            n2 = float(list[index + 1]) or 0
            current_result = calculate(n1, operand, n2)
            current_result_index = index
            break
        index += 1

    if (current_result):
        index = 0
        while index < len(list):
            if (index == current_result_index - 1):
                temp_list.append(current_result)
            elif (index != current_result_index + 1 and index != current_result_index):
                temp_list.append(list[index])
            index += 1
        return perfom_calculation(temp_list)

    return 0


print("[]========| CALCULATOR |========[]")


list = []

index = 0
while True:
    if (index % 2 == 0):
        temp = float(input("Masukkan angka (1,2,3,...) : "))
        list.append(temp)
    else:
        temp = input("Masukkan operasi (+,-,*,/,=) : ")
        list.append(temp)
        if (temp != PLUS and temp != MINUS and temp != TIMES and temp != DIVISION and temp != "="):
            print("INVALID INPUT!")
            break
    if (list.count("=") > 0):
        break
    index += 1

print(perfom_calculation(list))
