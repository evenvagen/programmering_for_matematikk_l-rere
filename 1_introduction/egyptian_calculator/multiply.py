class Multiply:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def closest_number(self, x):

        for i in range(10):
            power_of_two = 2 ** i
            if power_of_two <= x:
                c = power_of_two
        return c

    def calculate(self):
        x = self.closest_number(self.num_b)

        while x < self.num_b:
            n = self.num_b - x
            m = self.closest_number(n)
            x += m

        return x * self.num_a

    def cal(self):
        x = self.closest_number(self.num_b)
        list_a = [x]
        while x < self.num_b:
            n = self.num_b - x
            m = self.closest_number(n)
            x += m
            list_a.append(m)

        return list_a
















