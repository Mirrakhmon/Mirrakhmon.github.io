class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Строим список 10 → 20 → 30 вручную
c = ListNode(30)
b = ListNode(20, c)
a = ListNode(10, b)

def to_python_list(head):
    curr=head
    dummy=[]
    while curr:
        dummy.append(int(curr.val))
        curr=curr.next
    return dummy

    # цикл по узлам (как в print_all, только вместо print — append)
    # верните собранный список
    pass

print(to_python_list(a))   # ожидается: [10, 20, 30]

def sum_list(head):
    curr=head
    dummy=0
    while curr:
        dummy+=curr.val
        curr=curr.next
    return dummy


    # ваш код — верните СУММУ всех значений в списке

print(sum_list(a))   # ожидается: 60   (10+20+30)

def find_max(head):
    curr=head
    max_dummy=curr.val
    while curr:
        if max_dummy<curr.val:
            max_dummy=curr.val
        curr=curr.next

    # ваш код — верните МАКСИМАЛЬНОЕ значение в списке
    return max_dummy

print(find_max(a))   # ожидается: 30

def add_to_all(head, amount):
    curr=head
    while curr:
        curr.val=curr.val+amount
        curr=curr.next
    # пройдите по списку и увеличьте KAЖДОЕ значение на amount
    # НЕ создавайте новый список - изменяйте узлы "на месте"

add_to_all(a, 5)
print(to_python_list(a))   # ожидается: [15, 25, 35]

def remove_first(head):
    return head.next

new_head = remove_first(a)
print(to_python_list(new_head))    # без первого элемента
print(to_python_list(a))            # а этот список остался полным!