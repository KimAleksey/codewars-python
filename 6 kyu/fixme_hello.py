"""
https://www.codewars.com/kata/5b0a80ce84a30f4762000069/train/python
"""

class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self.order = {"name": None, "sex": None, "age": None}

    def setOrder(self, attribute):
        if self.order[attribute] is None:
            max_order = 0
            for value in self.order.values():
                if value is not None and value > max_order:
                    max_order = value
            self.order[attribute] = max_order + 1

    def setAge(self, age):
        self.age = age
        self.setOrder("age")
        return self

    def setSex(self, sex):
        self.sex = sex
        self.setOrder("sex")
        return self

    def setName(self, name):
        self.name = name
        self.setOrder("name")
        return self

    def hello(self):
        res = ["Hello."]
        order_tmp = {key: value for key, value in self.order.items() if value is not None}
        order_tmp = dict(sorted(order_tmp.items(), key=lambda x: x[1]))
        for key, value in order_tmp.items():
            if value is not None:
                if key == "name":
                    res.append(f"My name is {self.name}.")
                elif key == "age":
                    res.append(f"I am {self.age}.")
                else:
                    res.append(f"I am {'male' if self.sex=='M' else 'female'}.")
        return " ".join(res)


dm = Dinglemouse().setName("Batman")
print(dm.hello())