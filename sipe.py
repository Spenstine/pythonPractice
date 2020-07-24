class Kangaroo():
    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        return f'Kangaroo object: pouch_contents:{self.pouch_contents}'

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
print(kanga)
print(roo)
kanga.put_in_pouch(roo)
print(kanga)