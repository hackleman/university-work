class maxStack(object):

    def __init__(self):
        self.vals = []
        self.maxs = []

    def push(self, val):
        self.vals.append(val)
        if self.maxs:
            if val > self.max():
                self.maxs.append(val)
            else:
                self.maxs.append(self.max())
        else:
            self.maxs.append(val)

    def pop(self):
        self.maxs.pop()
        return self.vals.pop()

    def max(self):
        return self.maxs[-1]

driver = maxStack()

driver.push(2)
print(driver.max())
driver.push(5)
driver.push(3)
driver.push(4)
print(driver.max())
driver.push(10)
driver.push(9)
print(driver.max())
driver.pop()
driver.pop()
print(driver.max())