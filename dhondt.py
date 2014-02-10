"Calculate distribution using D'Hondt"


def dhondt(data, num_escanos):
    escanos = dict.fromkeys(data.keys(), 0)
    partidos = data.keys()
    votos = data.values()
    for escano in range(num_escanos):
        print("%s %s" % (escano, votos))
        max_votos = max(votos)
        ganador = votos.index(max_votos)
        partido_ganador = partidos[ganador]
        escanos[partido_ganador] += 1
        votos[ganador] = data[partido_ganador] / (escanos[partido_ganador] + 1)
    return escanos


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
    from collections import OrderedDict
    partidos = 'PSOE', 'PP', 'IU'
    votos = 246324-7647, 166665, 47908+7647
    escanos = 4, 2, 1

    data = OrderedDict(zip(partidos, votos))
    resultado = OrderedDict(zip(partidos, escanos))


    assert dhondt(data, 7) == resultado
