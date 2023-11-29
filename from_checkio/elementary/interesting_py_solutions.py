#################################################
# Interesting python solutions from checkio.org #
#################################################


###################
###     str     ###
###################


def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
    # or pythonic:  return text[0].upper() + text[1:] + "."*(text[-1] != ".")


def checkio(words: str) -> bool:
    """
    return True, if the string contains three words (words contain letters only)
    in succession (== one after another);
    else False
    """
    import itertools
    wl = words.split()
    for k, i in itertools.groupby(wl, key=lambda s: s.isalpha()):
        if k == True and len(list(i)) >= 3:
            return True
    return False


def checkio_alt1(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False

# another alternative for checkio()
checkio_alt2 = lambda x:"www" in "".join('w' if w.isalpha() else 'd' for w in x.split())
# and the same shorter:
checkio_alt3 = lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())

# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False


###################
###  different  ###
###################


def is_even(num: int) -> bool:
    # r = lambda n: False if n % 2 else True
    # return r(num)
    return False if num % 2 else True


def nearest_value(values: set, one: int) -> int:
    """
    Find and return the nearest (and smallest, if two) int
    in values (set of integers) to the given one (int).
    """
    return min(values, key=lambda n: (abs(one - n), n))


###############################
###  dicts, lists, sorting  ###
###############################


def two_teams(sailors):
    """
    Create two different lists on base of a given dictionary
    """
    first_team = [key for key, value in sailors.items() if value < 20 or value > 40]
    second_team = [key for key, value in sailors.items() if value >= 20 and value <= 40]
    first_team.sort()
    second_team.sort()
    return [first_team, second_team]


def two_teams_alt(sailors):
    young_and_old = {x for x,y in sailors.items() if y<20 or y>40}
    others = sailors.keys() ^ young_and_old
    return [sorted(young_and_old), sorted(others)]


