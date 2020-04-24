class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    u_set = set()
    current_node = llist_1.head;
    while current_node:
        u_set.add(current_node.value)
        current_node=current_node.next
    current_node = llist_2.head;
    while current_node:
        u_set.add(current_node.value)
        current_node=current_node.next
    u_head = Node(None)
    u_current_node = u_head
    for element in u_set:
        u_current_node.next = Node(element)
        u_current_node = u_current_node.next
    u_head = u_head.next
    u_list = LinkedList()
    u_list.head = u_head
    return u_list
    pass


def intersection(llist_1, llist_2):
    l1 = set()
    current = llist_1.head
    while current:
        l1.add(current.value)
        current = current.next
    l2 = set()
    current = llist_2.head
    while current:
        l2.add(current.value)
        current = current.next

    l = l1.intersection(l2)
    result = LinkedList()
    for num in l:
        result.append(num)
    return result

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))



# Test case 3: empty link
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
print(union(linked_list_5, linked_list_6))#print empty list
print(intersection(linked_list_5, linked_list_6))#prints empty list

# Test case 4: one empty, and one non-empty linked lists
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
for i in [1,2,3,4,5,6,7]:
    linked_list_7.append(i)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))