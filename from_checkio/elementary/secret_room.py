def int2alpha(i):
    units = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    dozens29 = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    dozens19 = {0: "ten", 1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen",
                7:"seventeen", 8:"eighteen", 9:"nineteen"}

    hundred = lambda x: units[int(str(x)[-3])] + " hundred"
    dozen29 = lambda x: dozens29[int(str(x)[-2])]
    dozen19 = lambda x: dozens19[int(str(x)[-1])]
    unit19 = lambda x: units[int(str(x)[-1])]

    alpha = ""
    if len(str(i)) == 4:
        alpha = "one thousand"
    elif len(str(i)) == 3:
        alpha = hundred(i)
        if str(i)[-2] == "1":
            alpha = alpha + " " + dozen19(i)
        elif str(i)[-2] == "0" and str(i)[-1] != "0":
            alpha = alpha + " " + unit19(i)
        elif str(i)[-2] == "0" and str(i)[-1] == "0":
            pass
        else:
            if str(i)[-1] == "0":
                alpha = alpha + " " + dozen29(i)
            else:
                alpha = alpha + " " + dozen29(i) + " " + unit19(i)
    elif len(str(i)) == 2:
        if str(i)[-2] == "1":
            alpha = dozen19(i)
        else:
            if str(i)[-1] == "0":
                alpha = dozen29(i)
            else:
                alpha = dozen29(i) + " " + unit19(i)
    elif len(str(i)) == 1:
        alpha = unit19(i)
    return alpha


def secret_room(number):
    di = {}
    for n in range(number):
        di[n+1] = int2alpha(n+1)
    ordered = sorted(di, key=lambda x: di[x])
    pos = ordered.index(number) + 1
    return pos


if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    assert secret_room(100) == 51

    print("Coding complete? Click 'Check' to earn cool rewards!")
