def freeweight(weight, measures):
    freew = (weight*1000) - (measures['amount']*measures['weight'])
    if freew >= 0:
        return freew/1000, measures
    if freew < 0:
        measures_dim = measures
        measures_dim['amount'] = measures['amount'] - 1
        return None, measures_dim


def treasures(info, limit):
    unused = limit
    res = {'golden coin': 0, 'silver coin': 0, 'ruby': 0}
    so = [(k, info[k], (info[k]['price']/info[k]['weight'])) for k in info]
    so = sorted(so, key=lambda k: k[2], reverse=True)
    for item in so:
        w, newinfo = freeweight(unused, item[1])
        while w is None:
            w, newinfo = freeweight(unused, newinfo)
        unused, amount = w, newinfo['amount']
        treasure = item[0]
        if amount:
            res[item[0]] = (treasure + ": " + str(amount))
        if unused == 0:
            return [res[k] for k in res if res[k]]
        else:
            continue
    return [res[k] for k in res if res[k]]


if __name__ == '__main__':
    print("Example:")
    print(treasures({'golden coin':
                        {'price': 100, 'weight': 50, 'amount': 200},
                     'silver coin':
                        {'price': 10, 'weight': 20, 'amount': 1000},
                     'ruby':
                        {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 200},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 1000},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5) == [
                          'golden coin: 92', 'ruby: 2']
    assert treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 100},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 100},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5) == [
                          'golden coin: 100', 'silver coin: 100', 'ruby: 1']