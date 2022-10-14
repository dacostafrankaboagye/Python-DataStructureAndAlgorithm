class Node:
  def __init__(self, item):
    self.item = item
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    
  def insertFirst(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
      
  def printOut(self):
    temp  =self.head
    while(temp):
      print(temp.item, end="-->")
      temp = temp.next
    print("null")

  def insertAfterNode(self, prevNode, data):
    if (prevNode is None):
      return
    newNode = Node(data)
    newNode.next = prevNode.next
    prevNode.next = newNode
    
  def insertLast(self, data):
    newNode = Node(data)
    if(self.head == None):
      self.head = newNode
      return
    temp = self.head
    while(temp.next != None):
      temp = temp.next
    temp.next = newNode
    newNode.next = None

  def deleteFirst(self):
    if self.head == None:
      print('Nothing to delete')
      return
    temp = self.head.next
    self.head = None
    self.head = temp

  def deleteNode(self, position):
    if position == 0: 
      deleteFirst()
      return
    current = self.head
    
    for i in range(0,position-1):
      previous = current
      current = current.next
    previous.next = current.next
    

    
        

LL = LinkedList()
LL.insertFirst(20)
LL.insertFirst(30)
LL.insertFirst(40)
LL.insertFirst(50)
LL.printOut()
fouth = Node(40)
LL.insertAfterNode(LL.head.next,99)
LL.printOut()
LL.insertLast(1)
LL.printOut()
LL.deleteFirst()
LL.printOut()
LL.deleteNode(3)
LL.printOut()
LL.deleteNode(3)
LL.printOut()



















