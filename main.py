def isRound(i):
    return round(i) == i


def go(i1) -> int: 
    v:int = 0
    for i in range(1,10001):
        if isRound(int(i1[0]) / i) and isRound(int(i1[1]) / i):
            v = i
            pass
        else:
            pass
    return v


def calculate(i1,i2) -> str:
    m1 = go(i1)
    m2 = go(i2)
    i2[0],i2[1] = i2[1],i2[0]
    si1:list[int] = [1,1]
    si2:list[int] = [1,1]
    si1[0] = int(i1[0]) / m1
    si1[1] = int(i1[1]) / m1
    si2[0] = int(i2[0]) / m2
    si2[1] = int(i2[1]) / m2
    out:list[int] = [1,1]
    out[0] = si1[0] * si2[0]
    out[1] = si1[1] * si2[1]
    Mout = go(out)

    return f"{int(si1[0])}/{int(si1[1])} * {int(si2[0])}/{int(si2[1])} = {int(out[0] / Mout)}/{int(out[1] / Mout)}"

def catchErr(i:list[str]) -> str:
    if i[1] == '':
        i[1] = "1"
        pass
    if "+" in i[0]:
        s = i[0].split("+")
        i[0] = str((int(s[0])*int(i[1])) + int(s[1]) )
        pass
    return i

def run():
    # i1 = input("Bruch 1 seperate numbers with / :>").split("/")
    # i2 = input("Bruch 2 seperate numbers with / :>").split("/")
    i1:list[str] = [1,1]
    i2:list[str] = [1,1]
    i1[0] = input("Bruch 1 number 1 :>")
    i1[1] = input("Bruch 1 number 2 :>")
    i2[0] = input("Bruch 2 number 1 :>")
    i2[1] = input("Bruch 2 number 2 :>")

    i1 = catchErr(i1)
    i2 = catchErr(i2)

    

    print(calculate(i1,i2))

def main():
    while True:
        run()


if __name__ == '__main__':
    main()