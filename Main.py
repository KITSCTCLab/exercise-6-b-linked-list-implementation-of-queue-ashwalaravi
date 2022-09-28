class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.last is None:
      self.head = Node(data)
      self.last = self.head
    else:
      temp = self.last
      temp.next = Node(data)
      temp = temp.next 
      
    

  def dequeue(self) -> None:
    # Write your code here
    if self.head is None:
      return None
    else:
      val_returned  = self.head.data
      self.head = self.head.next 
      

    
  def status(self) -> None:
    # Write your code here
    currentnode = self.head
    queu=[]
    while(currentnode):
      queu.append(currentnode.data)
      currentnode = currentnode.next
    for i in queu:
      print(i,end="=>")
    print(None)

# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
