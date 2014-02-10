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
