def crop(lst):
    """As input takes a list of split lines.
    Crops the zero-lines and -columns on the edges of the grid."""
    newgrid = []
    if "#" not in lst[0]:
        newgrid = lst[1:]
    if newgrid:
        if "#" not in newgrid[-1]:
            newgrid = newgrid[:-1]
    else:
        if '#' not in lst[-1]:
            newgrid = lst[:-1]

    if newgrid:
        return crop(newgrid)
    else:
        return lst


def rotate(lst):
    """Rotates the grid 90 grad counter clockwise."""
    newlst = []
    for x in range(len(lst[0])):
        nl = ''
        for line in lst:
            nl = nl + line[len(line)-x-1]
        newlst.append(nl)
    return newlst


def keys_and_locks(lock, some_key):
    lock_list = crop(lock.split())
    lock_list = crop(rotate(lock_list))
    key_list = crop(some_key.split())
    key_list = crop(rotate(key_list))
    if (lock_list == key_list or
            rotate(lock_list) == key_list or
            rotate(rotate(lock_list)) == key_list or
            rotate(rotate(rotate(lock_list))) == key_list):
        return True
    else:
        return False


def keys_and_locks_alt(lock, key):
    """Alternate solution from other student."""
    def turn90(key):
        return [''.join([line[::-1][i] for line in key]) for i in range(len(key[0]))] if key else []

    def trim(key):
        for n in range(4):
            while key and not '#' in key[0]:
                key = key[1:]
            key = turn90(key)
        return key

    def keys_and_locks(lock, key):
        lock, key = trim(lock.split()), trim(key.split())
        for n in range(4):
            if lock == key:
                break
            key = turn90(key)
        return lock == key

    return keys_and_locks(lock, key)


if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False