def replaceWithNumbers(char):
    char = char.lower()
    match char:
        case "a":
            return 10
        case "b":
            return 11
        case "c":
            return 12
        case "d":
            return 13
        case "e":
            return 14
        case "f":
            return 15
        case _:
            return int(char)

def replaceWithLetters(num):
    match num:
        case 10:
            return "a"
        case 11:
            return "b"
        case 12:
            return "c"
        case 13:
            return "d"
        case 14:
            return "e"
        case 15:
            return "f"
        case _:
            return str(num)

def isCorrectSystemFor(sys, num):
    num = list(map(replaceWithNumbers, num))
    rangeOfSys = list(range(sys))
    #print(set(rangeOfSys), set(num))
    return True if list(set(rangeOfSys)|set(num)) == rangeOfSys else False

def toDEC(sys, num):
    calculation = ""
    num = list(map(replaceWithNumbers, list(num[::-1])))
    for d in enumerate(num):
        calculation += f"{d[1]}*{sys}**{d[0]}{'+' if int(d[0])+1 != len(num) else ''}"
    return eval(calculation)

def decTo(sys, num):
    x, ra = None, []
    while sys<=num:
        x = num%sys
        num = num//sys
        ra.append(x)
    else:
        ra.append(num)
    return ''.join(list(map(replaceWithLetters, list(reversed(ra)))))


# Testing
s, n = 16, "c9"
x = toDEC(s, n) if isCorrectSystemFor(s, n) else f"You entered incorrect number system for \"{n}\""
y = decTo(s, x)
print(y)
