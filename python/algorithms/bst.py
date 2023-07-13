class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None
    # in order
    def print(self):
        if self.left != None:
            self.left.print()
            
        print(f"{self.value}, ")
        
        if self.right != None:
            self.right.print()

    def insert(self, value):
        if value == self.value:
            self.count += 1
        elif (value < self.value):
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value == self.value:
            return self
        if value < self.value:
            if self.left == None:
                return None
            else:
                return self.left.find(value)
        if value < self.value:
            if self.right == None:      
                return None
            else:
                return self.right.find(value)

    def exists(self, value):
        return bool(self.find(value))

    def remove(self, value):
        # root
        if value == self.value:
            return None
        # try smaller, left
        elif value < self.value:
            # find match
            if value == self.left.value:
                pass
            # search deeper
            else:
                self.left.remove(value) 
        elif value > self.value:
            # match
            if value == self.right.value:
            	self.right = None
                # TODO: handle actual removal
            else:
                # not yet
                self.right.remove(value)
           
obj = Node(5)
obj.insert(4)
obj.insert(6)
obj.insert(-1)
obj.insert(10)
obj.print()
obj.remove(10)
print("\n")
obj.print()
