import random

class Hat:
    def __init__(self, **kwargs):
        # Define a list called "contents" which will include all arguments included when calling the Hat object (color and number)
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    #Define the draw method, including the number of balls to take as a variable
    def draw(self, num_balls):
        # Draw balls randomly from the hat without replacement
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        # Remove the drawn balls from contents list (simulating non-replacement). The list will include only the balls that initially belonged to self.contents and are not included in our random sampling from drawn_balls list.
        self.contents = [ball for ball in self.contents if ball not in drawn_balls]
        return drawn_balls
        #Note: I've defined this method because the instruction requires it, but the experiment function will use random.sample() for the same purpose. I could not fin the way yo use this method in the experiment function without finding issues which I could not solve on my own.

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Count the number of successful experiments where expected balls are drawn
    num_successful_experiments = 0
    # Perform the specified number of experiments
    for _ in range(num_experiments):
        # Copy the hat contents for each experiment to avoid modification. This is the only place where the hat oject is useful in my code.
        hat_copy = hat.contents.copy()
        # Draw balls randomly from the hat without replacement
        drawn_balls = random.sample(hat_copy, min(num_balls_drawn, len(hat_copy)))
        # Check if the drawn balls match or exceed the expected balls
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            num_successful_experiments += 1
    # Calculate the probability
    probability = num_successful_experiments / num_experiments
    return probability

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
