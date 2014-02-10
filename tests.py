from dhondt import dhondt


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
