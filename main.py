# main.py
from collections import Counter

import matplotlib.pyplot as plt

from prisoner.simulation import Simulation


def main():
    """The main entry point for the simulation."""
    print("--- Starting Prisoner's Dilemma Simulation (MVP 2) ---")
    
    sim = Simulation(start_population=100)
    
    # Data tracking
    history = []

    num_generations = 100
    for i in range(num_generations):
        sim.run_generation()
        
        # Track the count of each strategy
        strategy_counts = Counter(agent.strategy for agent in sim.population)
        history.append(strategy_counts)
        
        print(f"Generation {i+1}: Population = {len(sim.population)} | "
              f"Strategies = {dict(strategy_counts)}")
        
        if not sim.population:
            print("--- Population has died out. ---")
            break

    print("--- Simulation Finished ---")
    
    # Plotting the results
    if history:
        strategies = sorted(history[0].keys())
        plt.figure(figsize=(12, 8))
        
        # Create a list for each strategy's count over time
        strategy_data = {strategy: [gen.get(strategy, 0) for gen in history] for strategy in strategies}
        
        plt.stackplot(range(num_generations), strategy_data.values(), labels=strategy_data.keys())
        
        plt.title("Evolution of Strategies Over Time")
        plt.xlabel("Generation")
        plt.ylabel("Number of Agents")
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    main()