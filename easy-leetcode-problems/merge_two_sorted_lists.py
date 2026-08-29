from datetime import datetime

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        current=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next = list1 if list1 else list2
        return dummy.next



def build_list(arr):
    dummy = ListNode()
    current = dummy
    for x in arr:
        current.next = ListNode(x)
        current = current.next
    return dummy.next

def list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
sol = Solution()
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
print(list_to_array(sol.mergeTwoLists(l1, l2)))    # [1, 1, 2, 3, 4, 4]