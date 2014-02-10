"Calculate distribution using D'Hondt"


def dhondt(votes_cast, total_seats):
    seats_per_party = dict.fromkeys(votes_cast.keys(), 0)
    quotients = [(votes, 0, party) for party, votes in votes_cast.iteritems()]
    for seat in range(total_seats):
        print("%s %s" % (seat, quotients))
        round_winner = max(quotients)
        idx = quotients.index(round_winner)
        max_quotient, inv_seats, party = round_winner
        seats_per_party[party] += 1
        quotients[idx] = votes_cast[party] / (seats_per_party[party] + 1), inv_seats-1, party
    return seats_per_party


def test():
    partidos = ('A', 'B', 'C', 'D', 'E',)

    votos = (340000, 280000, 160000, 60000, 15000,)
    escanos = (3, 3, 1, 0, 0)

    data = dict(zip(partidos, votos))

    assert dhondt(dict(a=1), 1) == dict(a=1)
    assert dhondt(dict(a=2, b=1), 1) == dict(a=1, b=0)
    assert dhondt(dict(a=3, b=2, c=1), 2) == dict(a=1, b=1, c=0)
    assert dhondt(dict(a=10, b=4, c=1), 3) == dict(a=2, b=1, c=0)
    assert dhondt(data, 7) == dict(zip(partidos, escanos))


def test_cordoba():
    from collections import OrderedDict
    partidos = 'PSOE', 'PP', 'IU'
    votos = 246324, 166665, 47908
    escanos = 4, 3, 0

    data = OrderedDict(zip(partidos, votos))
    resultado = OrderedDict(zip(partidos, escanos))

    assert dhondt(data, 7) == resultado


def test_cordoba_dos():
    partidos = 'PSOE', 'PP', 'IU'
    votos = 246324-7647, 166665, 47908+7647
    escanos = 4, 2, 1

    data = dict(zip(partidos, votos))
    resultado = dict(zip(partidos, escanos))


    assert dhondt(data, 7) == resultado
