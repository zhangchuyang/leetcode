# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x1 = ""
        x2 = ""
        while l1:
            x1 += str(l1.val)
            l1 = l1.next
        while l2:
            x2 += str(l2.val)
            l2 = l2.next
        x3 = str(int(x1[::-1]) + int(x2[::-1]))[::-1]
        head = ListNode(x3[0])
        answer = head
        for i in range(1, len(x3)):
            node = ListNode(x3[i])
            head.next = node
            head = head.next
        return answer
