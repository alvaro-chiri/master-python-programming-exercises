# class IterateClass:
#     def __init__(self, n):
#         self.n = n

#     def divisible_by_seven(self):
#         for number in range(self.n + 1):
#             if number % 7 == 0:
#                 yield number

# n = 100
# generator_seven = IterateClass(n).divisible_by_seven()

# for num in generator_seven:
#     print(num)

#---------------------------------------------------------------

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for number in range(self.n + 1):
            if number % 7 == 0:
                yield number

# Example usage:
n = 50
divisible_by_seven_generator = DivisibleBySeven(n).generate_divisible_by_seven()

for num in divisible_by_seven_generator:
    print(num)
