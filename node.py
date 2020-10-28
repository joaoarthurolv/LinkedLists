# Definição da classe Nó
class Node:
    # A classe Nó contém o dado e a posição do próximo nó
    def __init__(self, data) -> None:
        self.data = data
        self.next = None