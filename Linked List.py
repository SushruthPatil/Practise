class Node: #Creating Node
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

#insertion-----------------------------------------------------------------------
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
#deletion----------------------------------------------------------------------------------------            
    def removeAtBegin(self):
        if self.head is None:
            print("Linked List is empty")
        self.head = self.head.next

    def removeAtEnd(self):
        if self.head is None:
            print("Linked list is empty")
        current = self.head
        while current.next.next != None:
            current = current.next
        current.next = None    

    def removeAt(self,index):
        if not self.head:
            return
        current = self.head
        for i in range(index-1):
            current = current.next
        current.next = current.next.next
#search-----------------------------------------------------------------------------
    def find(self,x):
        current = self.head
        count = 0
        while current!=None:
            if current.data == x:
                print(count)
                return
            current = current.next
            count+=1
        print("Not Found")
#size----------------------------------------------------------------------------------    
    def size(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        print(count)

    
    def print(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        
        current = self.head
        Llist = ''
        while (current is not None):
            Llist += str(current.data)+"-->"
            current = current.next
        print(Llist+"None")
        

#------------------------------------------------------------------------------------------------
#driver code:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtEnd(10)
    ll.insertAtBegin(5)
    
    ll.insertAt(6,1)
    
    
    ll.insert_values([7,8,9])
    # ll.removeAtBegin()
    # ll.removeAtEnd()
    
    ll.print()
    ll.size()
    ll.find(9)