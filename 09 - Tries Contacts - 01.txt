class trie:
    def __init__(self):
        self.frequency = 0
        self.children = {}
    def add(self, name):
        self.frequency += 1
        if (len(name) != 0):
            self.children.setdefault(name[0], trie())
            self.children[name[0]].add(name[1:])
    def find(self, partial):
        if (len(partial) > 0):
            if (self.children.has_key(partial[0])):
                return(self.children[partial[0]].find(partial[1:]))
            else:
                return(0)
        return(self.frequency)

names = trie()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if (op == 'add'):
        names.add(contact)
    elif (op == 'find'):
        print(names.find(contact))

