def equilateral(sides):
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0:
            return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b == c:
        return True
    else:
        return False


def isosceles(sides):
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0:
            return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    if a == b or b == c or a == c:
        return True
    else:
        return False


def scalene(sides):
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0:
            return False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    if a != b and b != c and a != c:
        return True
    else:
        return False