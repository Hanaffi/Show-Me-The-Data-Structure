import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data


def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


# blocks
block_zero = Block(get_timestamp(), "Information A", 0)
block_one = Block(get_timestamp(), "Information B", block_zero)
block_two = Block(get_timestamp(), "Information C", block_one)

# linked list
linked_list = LinkedList()
linked_list.append(get_timestamp(), "Information X")
linked_list.append(get_timestamp(), "Information Y")

# tests
print("Block Zero data : ", block_zero.data)
print("Block Zero hash : ", block_zero.hash)
print("Block Zero timestamp : ", block_zero.timestamp)
print("Block one's previous block's data : ", block_one.previous_hash.data)
print("Linked list last data : ", linked_list.last.data)
print("Linked list last's previous hash data : ", linked_list.last.previous_hash.data)






# TEST 2
block_zero = Block(get_timestamp(), "Information A", 0)
block_one = Block(get_timestamp(), "Information B", block_zero)
block_two = Block(get_timestamp(), "Information C", block_one)
block_three = Block(get_timestamp(), "Information C", block_two)
linked_list1 = LinkedList()
linked_list1.append(get_timestamp(), "Information X")
linked_list1.append(get_timestamp(), "Information Y")
linked_list1.append(get_timestamp(), "Information Z")

print("Block Zero data : ", block_zero.data)
print("Linked list last's previous hash data : ", linked_list1.last.previous_hash.data)

# TEST 3

block_zero = Block(get_timestamp(), "Information A", 0)
block_one = Block(get_timestamp(), "Information B", block_zero)
block_two = Block(get_timestamp(), "Information C", block_one)
block_three = Block(get_timestamp(), "Information D", block_two)
block_four = Block(get_timestamp(), "Information D", block_two)


linked_list2 = LinkedList()
linked_list2.append(get_timestamp(), "Information X")
linked_list2.append(get_timestamp(), "Information Y")
linked_list2.append(get_timestamp(), "Information Z")
linked_list2.append(get_timestamp(), "Information T")

print("Block Zero data : ", block_zero.data)
print("Linked list last's previous hash data : ", linked_list2.last.previous_hash.data)






