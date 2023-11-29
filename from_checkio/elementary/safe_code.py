import operator


ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


def parsr(equation):
    leftpart = equation.split("=")[0]
    result = equation.split("=")[1]
    for x in range(1, len(leftpart)):  # range(1, ...) - to ignore cases with the "-" in the beginning
        if leftpart[x] in "+-*":
            opidx = x
            break
    firstnum = leftpart[0:opidx]
    oper = leftpart[opidx]
    secondnum = leftpart[opidx+1:]
    return {"first": firstnum, "op": oper, "second": secondnum, "res": result}


def dgt_or_rep(string, n):
    newstring = ''
    for char in string:
        if char == "-":
            newstring = "-"
            continue
        try:
            digit = int(char)
        except:
            digit = int(n)
        newstring += str(digit)
    return int(newstring)


def safe_code(equation):
    eq = parsr(equation)  # {"first": firstnum, "op": oper, "second": secondnum, "res": result}
    for n in range(10):
        if str(n) in equation:
            continue
        if n == 0 and eq["res"][0] == "#":
            continue
        if n == 0 and len(eq["first"]) > 1 and eq["first"][0] == "#":
            continue
        if n == 0 and len(eq["second"]) > 1 and eq["second"][0] == "#":
            continue
        if ops[eq["op"]](dgt_or_rep(eq["first"], n), dgt_or_rep(eq["second"], n)) == dgt_or_rep(eq["res"], n):
            return n
        elif "#" not in eq["first"][1:] + eq["second"][1:] + eq["res"][1:] and \
                ops[eq["op"]](dgt_or_rep(eq["first"], -n), dgt_or_rep(eq["second"], -n)) == dgt_or_rep(eq["res"], -n):
            return -n
    return -1


if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1