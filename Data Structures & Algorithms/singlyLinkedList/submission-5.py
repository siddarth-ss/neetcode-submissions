class Node:
    def __init__(self,val,nextnode=None):
        self.val= val
        self.next=nextnode

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail= self.head

    def get(self, index: int) -> int:
        curr= self.head.next
        i=0
        while curr:
            if i==index:
                return curr.val 
               
            else:
                i+=1
                curr=curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        newnode= Node(val)
        newnode.next=self.head.next
        self.head.next=newnode

        if not newnode.next:
            self.tail = newnode


    def insertTail(self, val: int) -> None:
        newnode = Node(val)
        self.tail.next=newnode
        self.tail = self.tail.next
      
        
    def remove(self, index: int) -> bool:
        curr= self.head
        i=0
        while curr and i < index:
            i+=1
            curr=curr.next
        if curr and curr.next:
            if  curr.next == self.tail:
                self.tail= curr
            curr.next=curr.next.next
            return True
        return False
      
    def getValues(self) -> List[int]:
        curr=self.head.next
        output=[]
        while curr:
            output.append(curr.val)
            curr=curr.next
        return output
       
