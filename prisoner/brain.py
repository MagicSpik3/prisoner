import numpy as np
import random
import csv

class BeeBrain:
    """Simple feedforward NN for decision making."""
    def __init__(self, input_size=3, hidden_size=5, weights=None):
        if weights:
            self.w_input_hidden, self.w_hidden_output = weights
        else:
            self.w_input_hidden = np.random.randn(input_size, hidden_size)
            self.w_hidden_output = np.random.randn(hidden_size)

    def forward(self, x):
        h = np.tanh(np.dot(x, self.w_input_hidden))
        out = np.tanh(np.dot(h, self.w_hidden_output))
        return out

    def mutate(self, mutation_rate=0.05):
        if random.random() < mutation_rate:
            self.w_input_hidden += np.random.randn(*self.w_input_hidden.shape) * 0.1
            self.w_hidden_output += np.random.randn(*self.w_hidden_output.shape) * 0.1

    def get_weights(self):
        return (self.w_input_hidden.copy(), self.w_hidden_output.copy())

def map_output_to_action(output):
    """Map continuous NN output to discrete actions."""
    if output < -0.33:
        return "Ignore"
    elif output < 0.33:
        return "Decline"
    else:
        return "Groom"

class Bee:
    """Agent in the simulation."""
    def __init__(self, gender=None, brain=None):
        self.gender = gender if gender is not None else random.choice([0,1])
        self.energy = 10
        self.brain = brain if brain else BeeBrain()
        self.last_move = "Groom"  # default starting move
        self.reputation = 0.5

    def get_inputs(self):
        return np.array([self.energy/20, {"Groom":1,"Ignore":-1,"Decline":0}[self.last_move], self.reputation])

    def decide(self):
        output = self.brain.forward(self.get_inputs())
        action = map_output_to_action(output)
        self.last_move = action
        return action

def reproduce(parent_bee, mutation_rate=0.05):
    """Create an offspring with mutated weights."""
    new_brain = BeeBrain(weights=parent_bee.brain.get_weights())
    new_brain.mutate(mutation_rate)
    return Bee(gender=random.choice([0,1]), brain=new_brain)

class Simulation:
    def __init__(self, population_size=100):
        self.population = [Bee() for _ in range(population_size)]
        self.tick = 0
        self.logfile = "bee_sim_log.csv"
        with open(self.logfile, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["tick","total_bees","male_bees","female_bees","avg_energy"])

    def run_tick(self):
        self.tick += 1
        # Each bee decides
        for bee in self.population:
            bee.decide()
            # Adjust energy for demonstration
            bee.energy -= 1
        # Remove dead bees
        self.population = [b for b in self.population if b.energy > 0]
        # Reproduction to maintain population
        while len(self.population) < 100:
            parent = random.choice(self.population)
            self.population.append(reproduce(parent))
        self.log_stats()

    def log_stats(self):
        male_count = sum(b.gender==0 for b in self.population)
        female_count = sum(b.gender==1 for b in self.population)
        avg_energy = np.mean([b.energy for b in self.population])
        with open(self.logfile, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.tick,len(self.population),male_count,female_count,avg_energy])
