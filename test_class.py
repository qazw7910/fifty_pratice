class Scorelist:

    def __init__(self, scores):
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


class_scores = Scorelist([85, 95, 70 , 90, 64])

print(f'平均分數: {class_scores.average()}')
