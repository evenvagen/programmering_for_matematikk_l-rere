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

    def beta_calculator(self):
        x = self.closest_number(self.num_b)

        while x < self.num_b:
            n = self.num_b - x
            m = self.closest_number(n)
            x += m

        return x * self.num_a

    def egypt_calculator(self):
        x = self.closest_number(self.num_b)
        h = x * self.num_a
        list_b = [h]
        while x < self.num_b:
            n = self.num_b - x
            m = self.closest_number(n)
            x += m
            k = m * self.num_a
            list_b.append(k)

        return list_b
















