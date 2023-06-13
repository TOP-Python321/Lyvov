from collections.abc import Iterable


def tree_leaves(data: Iterable) -> int:
    """
    Считает количество листьев на дереве.
    
    :param data: Итерируемый объект.
    
    :return: Возвращает объект int
    """
    count = 0
    
    for elem in data:
        if isinstance(elem, list):
            count += tree_leaves(elem)
        else:
            count += 1
            
    return count
    
    
# tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# print(tree_leaves(tree))
# 38