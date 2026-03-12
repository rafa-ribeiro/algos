from typing import List


def quicksort(items: List, start=0, end=None) -> List:
    if len(items) <= 1:
        return items

    end = end if end is not None else len(items)
    if start < end:
        pp = partition(items, start, end)
        quicksort(items, start, pp)
        quicksort(items, pp + 1, end)

    return items


def partition(items, start, end) -> int:
    pivot = items[end - 1]  # seleciona o pivo, nesse caso o último elemento da lista
    for i in range(start, end):
        if items[i] <= pivot:
            items[i], items[start] = items[start], items[i]
            start += 1
            # Ponteiro start só vai andar se o item corrente é MENOR que o pivo;
            # sempre que MAIOR, o start não anda, ou seja, ele guarda o primeiro elemento encontrado maior que o pivot,
            # assim quando encontrar o próximo menor que o pivot, já sabemos que podemos trocar esse
            # menor pelo primeiro maior que o pivot.

    return start - 1
