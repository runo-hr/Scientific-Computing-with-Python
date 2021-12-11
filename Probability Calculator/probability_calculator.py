import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        self.copy = copy.deepcopy(self.contents)

    def draw(self, n):
        self.contents = copy.copy(self.copy)
        if n > len(self.contents):
            return self.contents
        draws = []
        for i in range(n):
            draw = random.choice(self.contents)
            draws.append(draw)
            self.contents.remove(draw)
        return draws

    def __str__(self):
        return str(self.contents)

def experiment(hat , expected_balls , num_balls_drawn, num_experiments ):
    M = 0
    for i in range(num_experiments):
        draws = hat.draw(num_balls_drawn)
        x = 0
        for k,v in expected_balls.items():
            if draws.count(k) >= v:
                x += 1
        if x == len(expected_balls):
            M += 1
    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)