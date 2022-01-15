
""" DATA STRUCTURE: LINKED LIST """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'The data is {self.data}, and ' \
               f'next is {self.next}.'


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        # print(new_node)
        cur = self.head
        # print('Before: ', cur)
        # print('Before: ', cur.next)
        while cur.next is not None:
            cur = cur.next
            # print('##')
        cur.next = new_node
        self.size += 1
        # print('After: ', self.head)
        # print('After: ', cur.next)

    def get_size(self):
        return self.size

    def display(self):
        element = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            element.append(cur.data)
        return element

    def get(self, index):
        if index >= self.get_size():
            return 'Index not in Linked List'
        return self.display()[index]

    def get_index(self, index):
        if index >= self.get_size():
            return 'Index not in Linked List'
        cur_idx = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.get_size():
            return 'Index not in Linked List'
        cur_idx = 0
        cur_node = self.head
        while cur_node.next is not None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                self.size -= 1
                return
            cur_idx += 1

    def get_index_node(self, index):
        if index >= self.get_size():
            return 'Index not in Linked List'
        cur_idx = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node
            cur_idx += 1

    def middleNode(self):
        if self.get_size() % 2 == 0:
            ans = self.get_size()/2
            return self.get_index_node(ans)
        ans = (self.get_size()//2)
        return self.get_index_node(ans)


thelist = LinkedList()
print(type(thelist))
thelist.append(1)
thelist.append(2)
thelist.append(3)
thelist.append(4)
thelist.append(5)
thelist.append(5)
thelist.append(5)
thelist.append(9)
print(thelist.display())
print(thelist.get_size())
print(thelist.get(3))
print(thelist.get_index())
thelist.erase(1)
print(thelist.display())
print(thelist.middleNode())
