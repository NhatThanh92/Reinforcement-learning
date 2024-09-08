# Optimization of inputs for labor simulation

In this simulation, reinforcement learning (RL) optimizes input parameters to maximize uterine contraction strength by minimizing the distance between two reference points on the tissue.

**Reinforcement Learning Workflow:**

•	**Agent**: The agent, driven by a neural network or DDPG (Deep Deterministic Policy Gradient), acts as the decision-maker. It modifies simulation parameters or material properties (actions) within the range of 8 variables. The agent learns by interacting with the environment and receiving feedback.

•	**Environment**: FEBio, which simulates the labor process with active contraction using the Mooney-Rivlin model. It receives input actions from the agent and provides the current state and reward.

•	**State**: the current condition of the uterine model, such as its shape or tissue displacement. The agent uses this information to decide the next action.

•	**Action**: The modification of input parameters by the agent to optimize the simulation outcomes.

•	**Reward**: Defined as a function of the minimized displacement between two reference points, representing stronger uterine contractions. The closer the two points, the stronger the contraction, and thus, the higher the reward.

![image](https://github.com/user-attachments/assets/ebab7f89-8803-42b4-98c3-469ac28623ed)

**Fig 1. Reinforcement learning workflow.**

The RL process iterates continuously, with the agent refining its actions to achieve optimal outcomes.
