from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], 0, "test") == "test"
    # 1. Индекс в середине массива
    assert arrs.get([10, 20, 30, 40], 1, "default") == 20  # или 30? зависит от индексации
    
    # 2. Индекс в конце массива
    assert arrs.get([1, 2, 3], 2, "default") == 3   # последний элемент
    
    # 3. Индекс за пределами (больше длины)
    assert arrs.get([1, 2, 3], 10, "not found") == "not found"
    
    # 4. Отрицательный индекс (должен возвращать default, если индексация с 1)
    assert arrs.get([1, 2, 3], -1, "negative") == "negative"
    
    # 5. Индекс 0 (если индексация с 1, то такого индекса нет)
    #assert arrs.get([0, 1, 2, 3], 1, "zero index") == "zero index"
    


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

    # 1. Пустой массив
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([]) == []
    
    # 2. Только start (без end)
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    
    # 3. start = 0 (с начала)
    assert arrs.my_slice([1, 2, 3], 0) == [1, 2, 3]
    
    # 4. end больше длины массива
    assert arrs.my_slice([1, 2, 3], 1, 10) == [2, 3]
    
    # 5. Отрицательный start (если поддерживается)
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]  # последние два элемента
    
    # 6. Отрицательный end
    #assert arrs.my_slice([1, 2, 3, 4, 5], 1, -1) == [2, 3, 4]  # с 1 до предпоследнего
    
    # 7. start >= end (должен вернуть пустой список)
    assert arrs.my_slice([1, 2, 3], 3, 1) == []
    assert arrs.my_slice([1, 2, 3], 2, 2) == []
    
    # 8. start и end оба отрицательные
    #assert arrs.my_slice([1, 2, 3, 4, 5], -4, -1) == [2, 3, 4]
    
    # 9. Без аргументов (вернуть копию всего массива)
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
