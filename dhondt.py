"Calculate distribution using D'Hondt"


def dhondt(votes_cast, total_seats):
    seats_per_party = [0] * len(votes_cast)
    quotients = zip(votes_cast, seats_per_party)
    for seat in range(total_seats):
        print("%s -> %s" % (seat, quotients))
        round_winner = max(quotients, key=lambda x: (x[0], -x[1]))
        idx = quotients.index(round_winner)
        seats_per_party[idx] += 1
        quotients[idx] = votes_cast[idx] / (seats_per_party[idx] + 1), seats_per_party[idx]
    return tuple(seats_per_party)


def test_basic():
    assert dhondt((1, ), 1) == (1, )
    assert dhondt((2, 1), 1) == (1, 0)
    assert dhondt((3, 2, 1), 2) == (1, 1, 0)
    assert dhondt((10, 4, 1), 3) == (2, 1, 0)


def test_wikipedia():
    votos = (340000, 280000, 160000, 60000, 15000,)
    escanos = (3, 3, 1, 0, 0)

    assert dhondt(votos, 7) == escanos


def test_cordoba():
    votos = 246324, 166665, 47908
    escanos = 4, 3, 0

    assert dhondt(votos, 7) == escanos


def test_cordoba_dos():
    votos = 246324-7647, 166665, 47908+7647
    escanos = 4, 2, 1

    assert dhondt(votos, 7) == escanos
