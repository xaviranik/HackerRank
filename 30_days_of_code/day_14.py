class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximum = 0

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                abs_num = abs(self.__elements[i] - self.__elements[j])
                if abs_num > maximum:
                    maximum = abs_num
        self.maximumDifference = maximum


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)