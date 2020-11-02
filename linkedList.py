from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    # Inserção no fim da lista
    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    # Retorna no tamanho da lista
    def __len__(self):
        return self._size

    # Retorna o nó em índicie especificado
    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range") #return None
        return pointer

    def set(self, index, elem):
        # lista.set(5, 9)
        pass

    def __getitem__(self, index):
        # a = lista[6]
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[5] = 9
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    # Retorna o índice do elemento especificado
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))
    
    # Inserção no meio da lista
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
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
    
    # Remoção de elemento
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(elem))
    
    # Print da lista
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r
    
    # def destroy(self):
    #     self.head = None


lista = LinkedList()

# print(len(lista))

# lista.append(7)
# lista.append(80)

# print(len(lista))

# print("Posição 0:", lista[0])
# print("Posição 1:", lista[1])

# lista.insert_at_beginning(85)

# print("---------------")

# print("Posição 0:", lista[0])
# print("Posição 1:", lista[1])
# print("Posição 2:", lista[2])

# lista.insert(1, 25)

# print("---------------")

# print("Posição 0:", lista[0])
# print("Posição 1:", lista[1])
# print("Posição 2:", lista[2])
# print("Posição 3:", lista[3])

# lista.insert(3, 90)

# print("---------------")

# print("Posição 0:", lista[0])
# print("Posição 1:", lista[1])
# print("Posição 2:", lista[2])
# print("Posição 3:", lista[3])
# print("Posição 4:", lista[4])
