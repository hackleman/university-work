class Log:
    def __init__(self, num):
        self.log = [0] * num
        self.num = num
        self.iter = 0

    def record(self, order_id):

        if self.iter < self.num:
            self.log[self.iter] = order_id
            self.iter += 1
        elif self.iter == self.num:
            self.iter = 0
            self.log[self.iter] = order_id
            self.iter += 1

    def get_last(self, i):
       
        if self.iter > i-1:
            return self.log[self.iter-i:self.iter]
        else:
            return self.log[self.iter-i:] + self.log[:self.iter]
    def display(self):
        return self.log

tweetlog = Log(5)

for i in range(24):
    tweetlog.record(i)

print(tweetlog.get_last(1))
print(tweetlog.get_last(2))
print(tweetlog.get_last(3))
print(tweetlog.get_last(4))
print(tweetlog.get_last(5))
print(tweetlog.display())
