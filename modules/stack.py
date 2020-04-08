class Stack:
    def __init__(self):
        self.stack = []
        self.max_length = 0
        self.visited = []
        self.last_pop = None
        self.total_pop = 0

    def push(self, element):
        if not self.contains(element):
            self.stack.append(element)
            if len(self.stack) > self.max_length:
                self.max_length = len(self.stack)

    def pop(self):
        self.last_pop = self.stack.pop(0)
        self.visited.append(self.last_pop)
        self.total_pop += 1
        return self.last_pop

    def distance_sort(self, end_point):
        self.stack.sort(key=lambda point: point.distance(end_point))

    def red_sort(self, end_point):
        """
        En düşük maliyetliden yükseğe doğru sıralanıyor.
        """
        # NOTE: built-in sort yerine insert yapacak bir fonksiyon
        # yazılabilir. Sonuçta dizi sürekli sıralı olacak, sadece yeni
        # eklenen elemanlar aralara yerleşecek.
        self.stack.sort(key=lambda point: point.total_red + point.distance(end_point))

    def print(self):
        print(*self.stack, sep="\n")

    def length(self):
        return len(self.stack)

    def contains(self, element):
        for point in self.stack:
            if point == element:
                return True
        for point in self.visited:
            if point == element:
                return True
        return False
