def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.
    :param array: исходный список.
    :param index: индекс извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """

    if index < 0: #проверка на отрицательный индекс
        return default

    if 0 <= index < len(array): 
        return array[index]

    return default


def my_slice(coll, start=None, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """

    length = len(coll)

    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    elif start < 0:
       normalized_start = max(0, length + start) 
    else:
        normalized_start = min(length, start) #без выхода за пределы Макс и Мин

##########

    if end is None:
        normalized_end = length
    elif end < 0:
       normalized_end = min(length, end)  
    else:
        normalized_end = min(length, end) #без того, что бы был выход их Мин



    if normalized_start >= normalized_end:
        return []

    return coll[normalized_start:normalized_end]
