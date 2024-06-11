'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for elem in nodes:
                node.next=Node(data=elem)
                node=node.next
    def __iter__(self):
        node=self.head
        nodes=[]
        while node is not None:
            node.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)
        

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    def swap_elements(self):
        node=self.head
        while node and node.next:
            node.data,node.next.data=node.next.data,node.data
            node=node.next.next
            
    
llist = LinkedList()
first_node=Node("Srishanka")
llist.head=first_node
second_node=Node("sri")
third_node=Node("sai")
first_node.next=second_node
second_node.next=third_node
fourth_node=Node("samantha")
fifth_node=Node("sree")
third_node.next=fourth_node
fourth_node.next=fifth_node
llist = LinkedList(['12','76','43','8','56','3','9','88'])
print(llist)'''
 
#linkedlist implementation
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

    def _repr_(self):
        return self.data

class LinkedList:
    def _init_(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head=node
            for ele in nodes:
                node.next = Node(data=ele)
                node=node.next
    def _iter_(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def _repr_(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def swap(self):
        node=self.head
        while node and node.next:
            node.data,node.next.data=node.next.data,node.data
            node=node.next.next
            
llist = LinkedList()
first_node = Node("a")
llist.head = first_node
second_node = Node("b")
third_node = Node("c")
fourth_node = Node("d")
fifth_node = Node("e")
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
llist.add_last(fifth_node)
LList=LinkedList(['12','76','43','8','56','3','9','88'])
LList.swap()
print(llist)
print(LList)