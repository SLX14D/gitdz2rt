import logging
import doctest

logging.basicConfig(
    filename='cube.log',
    level=logging.INFO,
    filemode='a',  #дооавлять,перезаписывать
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cube(n):
    """
    Возвращает куб числа n.

    >>> cube(2)
    8
    >>> cube(-3)
    -27
    """
    result = n ** 3
    logging.info(f"Вызов cube({n}) = {result}")
    return result


if __name__ == "__main__":
    doctest.testmod()
    print(cube(5))
    print(cube(-2))
