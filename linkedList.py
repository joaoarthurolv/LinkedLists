from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # Inserção ao final da lista
    def append(self, element):
        if self.head:
            # Inserção quando a lista já possui elementos
            aux_pointer = self.head

            while(aux_pointer.next):
                aux_pointer = aux_pointer.next
            
            aux_pointer.next = Node(element)
        else:
            # Primeira inserção
            self.head = Node(element)

        self._size = self._size + 1
    
    # Inserção no início da lista
    def insert_at_beginning(self, element):
        if(self.head):
            # Inserção quando a lista já possui elementos
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
        else:
            # Primeira inserção
            self.head = Node(element)
        
        self._size = self._size + 1
    # Retorna o tamanho da lista
    def __len__(self):
        return self._size

    def get(self, index):
        # a = lista.get(6)
        pass

    def set(self, index, element):
        # lista.set(5, 9)
        pass
    
    # Recuperação de item utilizando sobrecarga de operadores
    def __getitem__(self, index):
        # a = lista[5]
        aux_pointer = self.head
        
        for i in range(index):
            if aux_pointer:
                aux_pointer = aux_pointer.next
            else:
                raise IndexError("list index out of range")
        
        if aux_pointer:
            return aux_pointer.data
        raise IndexError("list index out of range")
    
    # Definição de item utilizando sobrecarga de operadores
    def __setitem__(self, index, element):
        # lista[5] = 9
        aux_pointer = self.head
        
        for i in range(index):
            if aux_pointer:
                aux_pointer = aux_pointer.next
            else:
                raise IndexError("list index out of range")
        
        if aux_pointer:
            aux_pointer.data = element
        else:
            raise IndexError("list index out of range")
        
    # Retorna o índice do elemento da lista
    def index(self, element):
        aux_pointer = self.head
        i = 0

        while(aux_pointer):
            if aux_pointer.data == element:
                return i
            else:
                aux_pointer = aux_pointer.next
                i = i + 1
        raise ValueError("{} is not in the list".format(element))

lista = LinkedList()

print(len(lista))

lista.append(7)

print(len(lista))

lista.append(80)

print(len(lista))

lista.insert_at_beginning(1)

print(lista.__getitem__(0))