class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')

    def __stack__(self):
        cur = self.head.next
        out = ""
        sep = '->'
        while cur:
            out += f'{cur.value}{sep}'
            cur = cur.next
        out = out[:-2]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        tmp = self.head.next.value
        self.head.next = self.head.next.next
        return tmp


class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        super().__init__()

    def backup(self):
        self.backups.append(self.__stack__())

    def get_backup(self, i):
        return self.backups[i]

    def push(self, value):
        self.backup()
        super().push(value)



    def pop(self):
        self.backup()
        super().pop()


R = -1  # number of operations, e.g. .pop() or .push(), gotta add '1' before each operation
s = PersistentStack()
print(f"Backups:")
for i in range(5):
    R += 1
    s.push(i)
    print(s.get_backup(R))


print(f'Stack: {s.__stack__()}')
R += 1
s.pop()
print(f'New stack (after pop): {s.__stack__()}')
print(f'Before "pop" version: {s.get_backup(R)}')
print(f'All previous versions: {"; ".join(s.backups[1:])}')

