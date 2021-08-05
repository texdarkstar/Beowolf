import random

STARPORTS = {
    2: 'X',
    3: 'E',
    4: 'E',
    5: 'D',
    6: 'D',
    7: 'C',
    8: 'C',
    9: 'B',
    10: 'B',
    11: 'A',
    12: 'A',
}

def _2d6(mod=0):
    return random.randint(1, 6) + random.randint(1, 6) + mod

def get_uwp():
    starport = STARPORTS[_2d6()]

    size = _2d6(-2)

    atmosphere = _2d6(-7 + size)
    if atmosphere < 0:
        atmosphere = 0

    hydrosphere = _2d6(-7 + size)
    if (atmosphere <= 1) or ((atmosphere >= 10) and atmosphere <= 13):
        hydrosphere -= 4
    if (hydrosphere < 0) or (size <= 1):
        hydrosphere = 0

    population = _2d6(-2)
    if population <= 0:
        population = 0

    government = 0
    government = _2d6(-7 + population)
    if government <= 0:
        government = 0

    law_level = _2d6(-7 + government)
    if law_level <= 0:
        law_level = 0
        
    tech_level = random.randint(1, 6)
    if starport == "A":
        tech_level += 6
    if starport == "B":
        tech_level += 4
    if starport == "C":
        tech_level += 2
    if starport == "X":
        tech_level -= 4

    if size <= 1:
        tech_level += 2
    if (size <= 4) and (size >= 2):
        tech_level += 1

    if (atmosphere >= 3 and atmosphere <= 0) or (atmosphere >= 10 and atmosphere <= 15):
        tech_level += 1

    if (hydrosphere == 0) or (hydrosphere == 9):
        tech_level += 1
    if hydrosphere == 10:
        tech_level += 2

    if ((population >= 1) and (population <= 5)) or (population == 9):
        tech_level += 1
    if population == 10:
        tech_level += 2
    if population == 11:
        tech_level += 3
    if population == 12:
        tech_level += 4

    if (government == 0) or (government == 5):
        tech_level += 1
    if government == 7:
        tech_level += 2
    if (government >= 13) and (government <= 14):
        tech_level -= 2

    if tech_level < 0:
        tech_level = 0

    _uwp = [starport, size, atmosphere, hydrosphere, population, government, law_level, tech_level]
    u = list()
    for i in _uwp:
        n = i
        if n == 10:
            n = "A"
        elif n == 11:
            n = "B"
        elif n == 12:
            n = "C"
        elif n == 13:
            n = "D"
        elif n == 14:
            n = "E"
        elif n == 15:
            n = "F"
        elif n == 16:
            n = "G"
        elif n == 17:
            n = "H"
        elif n == 18:
            n = "I"
        elif n == 19:
            n = "J"


        u.append(str(n))

    return "".join(u)
