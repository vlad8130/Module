
class EnemyDown(Exception):
    pass


class GameOver(Exception):

    def __init__(self, player):
        super(GameOver, self).__init__()
        self.player = player
        self.scores = Score(player, 'scores.txt')

    def add_new_score(self):

        self.scores.scores_list.append([self.player.name, self.player.score])
        self.scores.scores_list.sort(key=lambda i: i[1], reverse=True)

        if len(self.scores.scores_list) > 10:
            self.scores.scores_list.pop()

        with open('scores.txt', 'w') as file:
            index = 1
            for score in self.scores.scores_list:
                file.write(f'{index}. Player name: {score[0]} | Score: {score[1]}\n')
                index += 1


class Score:

    def __init__(self, player, score_file):
        self.player = player
        self.scores_list = []
        with open(score_file, 'r') as file:
            for line in file.readlines():
                self.scores_list.append([line.split(' ')[3], int(line.split(' ')[-1].rstrip('\n'))])
