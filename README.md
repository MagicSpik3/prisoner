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

### Stage 4: Reputation and Partner Choice

**Goal:** To create a full, complex social simulation where reputation matters and agents can choose who they interact with.

* **Features:**
    * Agents will have a public `reputation` score based on their past actions.
    * The interaction loop will be replaced with a "partner selection" phase.
    * The neural network will be updated to use social cues (like reputation) to make decisions.
* **Status:** Not Started


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