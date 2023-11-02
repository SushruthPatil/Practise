class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insertAtBegin(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insertAtEnd(self,data):
        if not self.head:
            return self.insertAtBegin(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def insertAt(self,data,index):
        current = self.head
        new_node = Node(data)
        for i in range(index-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def insert_values(self,data):
        if self.head == None:
            for values in data:
                self.insertAtEnd(values)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            for values in data:
                self.insertAtEnd(values)
            
    
    def print(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        
        current = self.head
        Llist = ''
        while (current is not None):
            Llist += str(current.data)+"-->"
            current = current.next
        print(Llist)
        

#------------------------------------------------------------------------------------------------
#driver code:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtEnd(10)
    ll.insertAtBegin(5)
    
    ll.insertAt(6,1)

    ll.insert_values([7,8,9])
    
    ll.print()




        






    