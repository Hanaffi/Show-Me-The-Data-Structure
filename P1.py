class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def get_key(self):
        return self.data[0]

    def get_value(self):
        return self.data[1]
    

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_size = capacity
        self.size = 0
        self.dict = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            if  self.dict[key].next: # if item is not the most recently used alread (the head), then make it so 
                if self.dict[key].previous:
                    # if the item is not the tail then link the previous item to the next one
                    self.dict[key].previous.next = self.dict[key].next
                else:
                    self.tail = self.dict[key].next
                self.dict[key].next.previous = self.dict[key].previous
                self.dict[key].previous = self.head
                self.head.next = self.dict[key]
                self.head = self.dict[key]
            return self.dict[key].get_value()
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.max_size == 0:
            print("ERROR :: 0 capacity cache")
            return 
        
        if key in self.dict:
            temp =  self.dict[key]
            temp.data = (key, value)
            if temp.previous:
                temp.previous.next = temp.next
            if temp.next:
                temp.next.previous = temp.previous
            self.head.next = temp
            self.head = temp
            if self.tail == temp and temp.next:
                self.tail = temp.next
            temp.next = None
            return

        if self.size == self.max_size:
            del self.dict[self.tail.get_key()]
            self.tail = self.tail.next
            self.size -= 1
        
        temp = Node((key, value))
        if self.size == 0:
            self.head = self.tail = self.dict[key] = temp
            self.size += 1
            return
        temp.previous = self.head
        self.head.next = temp
        self.head = temp
        self.dict[key] = self.head
        self.size += 1


# Test1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
#print(our_cache.tail.data)   
#print(our_cache.head.data)   

print(our_cache.get(1))       
# expected output: 1
print(our_cache.get(2))    
# expected output: 2
print(our_cache.get(9))        
# expected output: -1 

#print(our_cache.tail.data)
#print(our_cache.head.data)
our_cache.set(5, 5) 
our_cache.set(6, 6)
#print(our_cache.tail.data)
#print(our_cache.head.data)

print(our_cache.get(3))    
# expected output: -1 
print(our_cache.get(6))    
# expected output: 6
print(our_cache.get(1))    
# expected output: 1

print('\n-----------------------------------\n')

#Test 2
our_cache = LRU_Cache(3)
our_cache.set(0, 0)
our_cache.set(1, 1)
our_cache.set(2, 2)

our_cache.set(1, 10)
our_cache.set(0, 5)
our_cache.set(2, 17)

print(our_cache.get(0))
# expected output: 5
print(our_cache.get(1))
# expected output: 10
print(our_cache.get(2))
# expected output: 17

print('\n-----------------------------------\n')

#Test 3
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# expected output: "Can't perform operations on 0 capacity cache"
print(our_cache.get(17))
# expected output: -1