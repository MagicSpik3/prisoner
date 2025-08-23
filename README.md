# Prisoner's Dilemma: An Evolutionary Simulation

This project is an experiment to simulate the evolution of cooperation, inspired by Robert Axelrod's famous Prisoner's Dilemma tournaments. It uses a population of agents, each equipped with a simple neural network, to see if cooperative strategies can emerge from an initially random state.

---

## Project Plan (Minimum Viable Product Stages)

This project is being developed in four distinct stages, starting with the simplest possible version and gradually adding complexity.

### Stage 1: The Core Mechanics (Current Stage ✅)

**Goal:** To build and test the absolute basic mechanics of the simulation. This stage focuses on the environment, not the agents' strategies.

* **Features:**
    * An `Agent` class with basic attributes (`id`, `energy`).
    * Agents make **completely random choices** (50/50 Groom vs. Ignore).
    * A working payoff matrix that correctly modifies agent energy.
    * A "metabolism" and "death" mechanic to remove unsuccessful agents.
* **Status:** **IN PROGRESS**

---

### Stage 2: Simple Strategies and Evolution

**Goal:** To implement a basic evolutionary loop using simple, hardcoded strategies to prove that the selection and reproduction mechanics work.

* **Features:**
    * Agents will have predefined strategies (`Always_Groom`, `Always_Ignore`, `Tit_for_Tat`).
    * A reproduction system where successful agents pass on their strategy to offspring.
    * A mutation system to allow for new strategies to emerge.
* **Status:** Not Started

---

### Stage 3: The Neural Network Brain

**Goal:** To replace the hardcoded strategies with an evolving neural network, allowing agents to learn from their direct experiences.

* **Features:**
    * Each agent will have a neural network "brain" whose weights act as its "genes."
    * Agents will have a `memory` of past interactions with specific opponents.
    * Reproduction will involve crossover and mutation of the neural network weights.
* **Status:** Not Started

---

### Stage 4: Reputation and Partner Choice

**Goal:** To create a full, complex social simulation where reputation matters and agents can choose who they interact with.

* **Features:**
    * Agents will have a public `reputation` score based on their past actions.
    * The interaction loop will be replaced with a "partner selection" phase.
    * The neural network will be updated to use social cues (like reputation) to make decisions.
* **Status:** Not Started


# Prisoner's Dilemma: An Evolutionary Simulation

This project is an experiment to simulate the evolution of cooperation, inspired by Robert Axelrod's famous Prisoner's Dilemma tournaments. It uses a population of agents to see if cooperative strategies can emerge from an initially random state.

---

## Project Plan (Minimum Viable Product Stages)

This project is being developed in distinct stages, starting with the simplest possible version and gradually adding complexity.

### Stage 1: The Core Mechanics

**Goal:** To build and test the absolute basic mechanics of the simulation.
* **Features:** `Agent` class, random choices, working payoff matrix, metabolism and death mechanic.
* **Status:** **COMPLETE** ✅

---

### Stage 2: Simple Strategies and Evolution (Current Stage ⚙️)

**Goal:** To implement a basic evolutionary loop using simple, hardcoded strategies to prove that the selection and reproduction mechanics work.
* **Features:** Predefined strategies (`Always_Groom`, `Always_Ignore`, `Tit_for_Tat`), reproduction of the fittest, mutation system.
* **Status:** **IN PROGRESS**

---

### Stage 3: The Neural Network Brain

**Goal:** To replace the hardcoded strategies with an evolving neural network, allowing agents to learn from their direct experiences.
* **Features:** NN "brain" with weights as "genes," a `memory` of past interactions, reproduction via crossover and mutation of NN weights.
* **Status:** Not Started

---

## Long-Term Roadmap (Future Development Ideas)

Once the core MVP stages are complete, the simulation can be extended with more complex and realistic social dynamics.

### Social Negotiation and Avoidance

* **Goal:** Introduce more nuanced social interactions beyond simple cooperation or defection.
* **Features:**
    * Add a third action: **"Decline,"** allowing agents to politely refuse an interaction at no cost.
    * Introduce an **"Always_Decline"** strategy to test the viability of pure isolationism.

### Reputation and Partner Choice

* **Goal:** Create a system where an agent's past behaviour influences future interactions.
* **Features:**
    * Implement a **reputation score** based on an agent's history of cooperation and defection.
    * Modify the interaction loop to allow agents to **choose their partners**, preferentially selecting those with a good reputation.
    * Explore a "gossip" mechanic where agents can learn about others through their social network ("friend of a friend").

### Advanced Social Pressures

* **Goal:** Introduce a "need for cooperation" that goes beyond simple energy gain.
* **Features:**
    * A **"Cleanliness"** score that decays over time and is only replenished by being groomed.
    * A **"Partnership Hierarchy"** where "unclean" agents are shunned by the elite but are forced to interact with each other out of necessity.