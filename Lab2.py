def task1():
    try:
        word1 = input("Введите первое слово: ")
        if not word1.isalpha():
            raise ValueError("Некорректный ввод. Пожалуйста, введите только буквы.")

        word2 = input("Введите второе слово: ")
        if not word2.isalpha():
            raise ValueError("Некорректный ввод. Пожалуйста, введите только буквы.")

        word1_sorted = ''.join(sorted(word1.replace(" ", "")))
        word2_sorted = ''.join(sorted(word2.replace(" ", "")))

        if word1_sorted == word2_sorted:
            print("Слова являются анаграммами.")
        else:
            print("Слова не являются анаграммами.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Эта функции отработала")

def task2(param):
    if type(param) == list:
        index = len(param)-1
        while param[index] <= 0 <= index:
            index -= 1

        if index < 0:
            raise IndexError("No positive elements")
        sum = 0
        index += 1
        while index < len(param):
            sum+=param[index]
            index+=1

        print("Sum =", sum)
        param = [i for i in param if i!=0]

        print("Result =", param)


    elif type(param) == dict:

        items = list(param.items())

        min = items[0]

        for i in items:

            if i[1] < min[1]:
                min = i

        print("Min =", min)

    elif type(param) == int:
        s = str(param)[::-1]

        print("Result =", s)

    elif type(param) == str:
        words = param.split()
        #words = [i for i in words if len(i) > 0]
        print("Count of words =", len(words))

    else:
        raise TypeError("Unknown type")

try:
    task2(-123124)
except TypeError:
    print("Unknown type")
except IndexError:
    print("No positive elements")
finally:
    print("Function done")


def task3():
    try:
        rows = int(input("Введите количество строк матрицы: "))
        if rows <= 0:
            raise ValueError("Количество строк должно быть больше нуля.")

        cols = int(input("Введите количество столбцов матрицы: "))
        if cols <= 0:
            raise ValueError("Количество столбцов должно быть больше нуля.")

        matrix = []

        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"Введите элемент [{i + 1}][{j + 1}]: "))
                row.append(element)
            matrix.append(row)

        positive = all(any(element > 0 for element in row) for row in matrix)

        if positive:
            for i in range(rows):
                for j in range(cols):
                    matrix[i][j] = -matrix[i][j]

            print("Все строки содержат хотя бы один положительный элемент.")
            print("Знаки всех элементов матрицы изменены на обратные.")
            print("Новая измененная матрица:")
            for row in matrix:
                print(row)
        else:
            print("Не все строки содержат хотя бы один положительный элемент.")

    except ValueError as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Функция отработала.")


def task4():
    try:
        num1 = int(input("Введите 1 число: "))
        num2 = int(input("Введите 2 число: "))
        result = num1 / num2
        print("Результат: ", result)

    except ZeroDivisionError:
        print("Делить на 0 нельзя")

    except ValueError:
        print("Некорректный ввод")

    finally:
        print("Функция отработала")

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def inputInt(description):
    str = input(description)
    while not isInt(str):
        print("Некорректный ввод, введите только числа из диапазона")
        str = input()
    return int(str)

def inputIntList(description):
    print(description)
    l=[]
    s=""
    while s != "*":
        s=input()
        while not isInt(s) and s != "*":
            print("Некорректный ввод, введите только числа из диапазона")
            s = input()
        if s != "*":
            l.append(int(s))
            print(l)
        else:
            break
    return l
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def inputFloat(description):
    str = input(description)
    while not isfloat(str):
        print("Некорректный ввод, введите только числа из диапазона")
        str = input()
    return float(str)
def main():
    isWork = True

    while isWork:
        print("1. 1 задание, анаграммы")
        print("2. 2 задание,  разные типы")
        print("3. 3 задание, матрица")
        print("4. 4 задание, try/except/finally")
        print("5. Выход")

        match (inputInt("Выберите вариант: ")):
            case 1:
                task1()
            case 2:
                v=inputInt("Введите вариант\n1.int\n2.str\n3.list\n4.dict\n5.float")
                try:
                    match v:
                        case 1:
                            p = inputInt("Введите число")
                            task2(p)
                        case 2:
                            p = input("Введите строку")
                            task2(p)
                        case 3:
                            p = inputIntList("Введите числo или * для окончания ввода")
                            task2(p)
                        case 4:
                            p = dict()
                            print("Введите пару (строка, число) или * для окончания ввода")
                            val = 0
                            s = ""
                            while s != "*":
                                s = input()
                                if s != "*":
                                    val = inputInt("")
                                    p.update({s: val})
                            task2(p)
                        case 5:
                            p = inputFloat("Введите дробное число")
                            task2(p)
                        case _:
                            print("Некорректный ввод")
                except TypeError:
                    print("Unknown type")
                except IndexError:
                    print("No positive elements")
                finally:
                    print("Function done")

            case 3:
                task3()
            case 4:
                task4()
            case 5:
                isWork = False
            case _:
                print("Некорректный ввод")

main()