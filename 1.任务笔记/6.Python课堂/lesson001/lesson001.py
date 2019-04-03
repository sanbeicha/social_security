class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(self.name)
        print(self.age)

if __name__ == '__main__':
    aaa = People("Tom", 33)
    aaa.call()
