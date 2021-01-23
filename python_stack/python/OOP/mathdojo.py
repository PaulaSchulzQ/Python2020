class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        return self

md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
md4 = MathDojo()

x1 = md1.add(2).add(2, 5, 1).subtract(3, 2).result
print(x1)
x2 = md2.add(12).subtract(30,65).add(90).subtract(120).result
print(x2)
x3 = md3.add(200).subtract(100, 100).result
print(x3)
x4 = md4.add(100,300,100).subtract(100,100).result
print(x4)



