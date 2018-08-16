# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Node1=l1
        Node2=l2
        resultListNode=currNode=ListNode(0)
        carry=0
        while (Node1!=None or Node2!=None):
            if (Node1!=l1 and Node1!=None and Node1.next==None and Node1.val==0) or (Node2!=l2 and Node2!=None and Node2.next==None and Node2.val==0):
                raise ValueError("value iinput erro,the first number shouldn't be zero")
           
            if (Node1!=None):
                x=Node1.val
            else:
                x=0
            if (Node2!=None):
                y=Node2.val
            else:
                y=0

            num=(carry+x+y)%10
            carry=(carry+x+y)//10                #carry is a carry flag (进位标志)
            currNode.next=ListNode(num)
            currNode=currNode.next
            if Node1!=None:
                Node1=Node1.next 
            if Node2!=None:    
                Node2=Node2.next
        if carry!=0:
            currNode.next=ListNode(1)
        return resultListNode.next
    
    def printListNodes(self,l1):
        curr=l1
        strlist=""
        while curr!=None:
            strlist=strlist+str(curr.val)
            curr=curr.next
        strlist=strlist[::-1]
        print(strlist)
      


def main():
    currNode11=ListNode1=ListNode(1)
    currNode11.next=ListNode(2)
    currNode11=currNode11.next
    currNode11.next=ListNode(3)
    currNode22=ListNode2=ListNode(1)
    currNode22.next=ListNode(4)
    currNode22=currNode22.next
    currNode22.next=ListNode(9)
    sol1=Solution()
    result=sol1.addTwoNumbers(ListNode1,ListNode2)
    sol1.printListNodes(result)
if __name__ == '__main__':
    main()
