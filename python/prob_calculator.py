import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ball, num in kwargs.items():
            self.contents.extend([ball for _ in range(num)])

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            all_balls, self.contents = self.contents, []
            return all_balls

        random_balls = random.sample(self.contents, num_balls)
        for ball in random_balls:
            self.contents.remove(ball)

        return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    run_counter, hits = 0, 0
    while run_counter < num_experiments:
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)

        is_hit = True
        for ball, num in expected_balls.items():
            if balls_drawn.count(ball) < num:
                is_hit = False
                break

        if is_hit:
            hits += 1

        run_counter += 1

    return hits / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=10,
)
