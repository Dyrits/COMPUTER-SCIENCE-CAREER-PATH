from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap():
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]
        
    def hash_index(self, key):
        return sum(key.encode()) % self.array_size
    
    def assign(self, key, value):
        list_at_array = self.array[self.hash_index(key)]
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        list_at_array.insert(Node([key, value]))
        
    def retrieve(self, key):
        for item in self.array[self.hash_index(key)]:
            if item[0] == key:
                return item[1]
        
blossom = HashMap(len(flower_definitions))
[blossom.assign(flower[0], flower[1]) for flower in flower_definitions]

print(blossom.retrieve('daisy'))
print(blossom.retrieve('magnolia'))
