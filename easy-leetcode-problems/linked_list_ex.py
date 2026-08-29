class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Строим список 1 → 2 → 3 вручную
node3 = ListNode(3)              # последний, next=None по умолчанию
node2 = ListNode(2, node3)        # указывает на node3
node1 = ListNode(1, node2)        # указывает на node2 — это ГОЛОВА списка

current = node1
while current:
    print(current.val)
    current = current.next