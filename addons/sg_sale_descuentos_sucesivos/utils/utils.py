
from functools import reduce


def descuento_sucesivos(descuentos):
    return reduce(lambda x, y: x * (1 - y / 100), descuentos, 100)
    """
    producto_descuentos = 1
    cantidad_descuentos = len(descuentos)
    for dsct in descuentos:
        producto_descuentos*=(100-dsct)

    return 100-(producto_descuentos/100**(cantidad_descuentos-1))
    """