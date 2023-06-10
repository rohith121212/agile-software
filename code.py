class Node():
    def __init__(self,value,next):
        self.value = value
        self.next = next
        
s = Node(1,None)
print(s.value, s.next)

s2 = Node(2,None)
print(s2.value,s2.next)

s.next = s2
print("After connection")
print(s.value,s.next)
print(s2.value,s2.next)

print(s.next.value)
print(s.next.next)

s3 = Node(3,None)
print(s3.value,s.next)

s.next.next = s3
print(s.next.next.value)
print(s.next.next.next)
