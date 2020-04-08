class Stack:
    def __init__(self):
        self.stack = []
        self.max_length = 0
        self.visited = []

    def push(self, element):
        self.stack.append(element)
        if len(self.stack) > self.max_length:
            self.max_length = len(self.stack)

    def pop(self):
        self.visited.append(self.stack.pop(0))

    def sort(self, key=lambda point: 255 - point.r):
        """
        En düşük maliyetliden yükseğe doğru sıralanıyor.
        """
        # NOTE: built-in sort yerine insert yapacak bir fonksiyon
        # yazılabilir. Sonuçta dizi sürekli sıralı olacak, sadece yeni
        # eklenen elemanlar aralara yerleşecek.
        self.stack.sort(key=key)

    def print(self):
        print(*self.stack, sep="\n")
