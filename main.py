from collections import UserDict


class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)

    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)


if __name__ == "__main__":
    d1 = MyDict({1: "a", 2: "b"})
    d2 = MyDict({3: "c", 4: "d"})

    d3 = d1 + d2
    print(d3)

    d4 = d3 - d2
    print(d4)


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Сума: {num1 + num2}")
    print(f"Різниця: {num1 - num2}")
    print(f"Добуток: {num1 * num2}")


from collections import UserList


class MulArray(UserList):
    def __init__(self, *args):
        self.data = list(args)

    def __mul__(self, other):
        return self.__scalar_mul(other)

    def __rmul__(self, other):
        return self.__scalar_mul(other)

    def __scalar_mul(self, other):
        result = 0
        for i in range(min(len(self.data), len(other))):
            result += self.data[i] * other[i]
        return result


if __name__ == "__main__":
    vec1 = MulArray(1, 2, 3)
    vec2 = MulArray(3, 4, 5)

    print(vec1 * vec2)
    print(vec1 * [1, 2, 3])
    print([1, 1, 1] * vec2)
