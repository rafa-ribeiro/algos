from typing import List


class Node:

    def __init__(self, name):
        self.name = name
        self.childs: List[Node] = list()
        self.parent = None

    def append(self, node: 'Node') -> None:
        node.parent = self
        self.childs.append(node)

    def pwd(self) -> str:
        path = f'/{self.name}'
        parent = self.parent
        while parent:
            path = f"/{parent.name}{path}"
            parent = parent.parent

        return path
