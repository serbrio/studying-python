def stones(pile, moves):
    #replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(stones(17, [1, 3, 4]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stones(17, [1, 3, 4]) == 2
    assert stones(17, [1, 3, 4, 6, 9]) == 1
    assert stones(99, [1]) == 2
