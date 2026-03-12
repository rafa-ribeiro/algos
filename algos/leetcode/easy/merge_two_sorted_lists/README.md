# 21. Merge Two Sorted Lists

Reference: [LeetCode - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints**:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

### Algoritmo explicado

Uma lista ligada é dada pela seguinte estrutura:

```python
class ListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next = None
```

- Cada nó da lista tem um valor e um ponteiro para o próximo nó.
- Como ambas as listas estão ordenadas, podemos comparar os valores de cada nó inicial de ambas as listas e decidir qual nó
deve ser o próximo nó da lista mesclada.
- Continuamos comparando os nós seguintes de ambas as listas e adicionando o nó com o menor valor à lista mesclada.
- Se uma das listas chegar ao fim, adicionamos o nó da lista restante no final da lista mesclada, pois ela já está ordenada.

#### Passo a passo:

1. Se uma das listas estiver vazia, retornamos a outra lista como resultado pois ela já está ordenada, logo sabemos de cara qual o primeiro nó da lista mesclada.

Esse trecho abaixo faz isso:

```python
    if not list1:
        return list2

    if not list2:
        return list1
```

2. A partir de agora, sabemos que ambas as listas têm pelo menos um nó. Comparamos então os valores de cada nó e o menor valor será o primeiro nó da lista mesclada.

```python
    if list1.value <= list2.value:
        merged_list = list1
        list1 = list1.next # Se nó 1 for menor, avançamos para o próximo nó da lista 1.
    else:
        merged_list = list2
        list2 = list2.next # Se nó 2 for menor, avançamos para o próximo nó da lista 2.
```

    **Obs1:** Importante prestar atenção nesse ponto que devemos atualizar o ponteiro da lista que teve seu nó adicionado à lista mesclada, para o próximo nó, pois na próxima comparação devemos comparar os próximos nós de cada lista.

    **Obs2:** Importante frisar aqui também que o nosso algoritmo deve retornar o nó inicial da lista mesclada, e nesse momento já sabemos qual é o nó inicial e podemos apenas guardá-lo e retorná-lo no final do algoritmo.

3. Agora estamos numa parte bacana do algoritmo porque como estamos trabalhando com listas ligadas e elas são ordenadas, 
podemos usar dessa característica para comparar os nós seguintes apenas se ambas as listas ainda tiverem nós. Se uma das listas chegar ao fim, a outra lista já estará ordenada e podemos simplesmente adicionar o nó restante no final da lista mesclada.

```python
    curr_node = merged_list
    while list1 and list2:
        if list1.value <= list2.value:
            curr_node.next = list1
            list1 = list1.next
        else:
            curr_node.next = list2
            list2 = list2.next

        curr_node = curr_node.next
```

    **Obs:** Note que o ponteiro `curr_node` é atualizado a cada iteração do loop, para apontar para o último nó adicionado à lista mesclada. Isso é importante para garantir que os nós sejam adicionados na ordem correta.

4. E para finalizar, se uma das listas chegar ao fim, a execução do while será interrompida, então precisamos saber qual das listas chegou ao fim para adicionar o restante da outra lista no final da lista mesclada.

```python
    if list1 is None: # Se a lista 1 chegou ao fim, adicionamos o restante da lista 2 no final da lista mesclada.
        curr_node.next = list2
    else: # Se a lista 2 chegou ao fim, adicionamos o restante da lista 1
        curr_node.next = list1
```

#### Resultado final:

```python
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.value <= list2.value:
        merged_list = list1
        list1 = list1.next
    else:
        merged_list = list2
        list2 = list2.next

    curr_node = merged_list
    while list1 and list2:
        if list1.value <= list2.value:
            curr_node.next = list1
            list1 = list1.next
        else:
            curr_node.next = list2
            list2 = list2.next

        curr_node = curr_node.next

    if list1 is None:
        curr_node.next = list2
    else:
        curr_node.next = list1

    return merged_list
```

