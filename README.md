# Optimization of inputs for labor simulation

In this simulation, reinforcement learning (RL) optimizes input parameters to maximize uterine contraction strength by minimizing the distance between two reference points on the tissue. A smaller distance indicates stronger contractions.

![noba](https://github.com/user-attachments/assets/f30ed19a-5bea-4c72-9cfe-04cc00be3825)

**Fig 1.  Two reference points in uterine contraction simulation.**


## Reinforcement Learning Workflow:

•	**Agent**: The agent, driven by a neural network or DDPG (Deep Deterministic Policy Gradient), acts as the decision-maker. It modifies simulation parameters or material properties (actions) within the range of 8 variables (Table 1). The agent learns by interacting with the environment and receiving feedback.

•	**Environment**: FEBio, which simulates the labor process with active contraction using the Mooney-Rivlin model. It receives input actions from the agent and provides the current state and reward.

•	**State**: the current condition of the uterine model, such as its shape or tissue displacement. The agent uses this information to decide the next action.

•	**Action**: The modification of input parameters by the agent to optimize the simulation outcomes.

•	**Reward**: Defined as a function of the minimized displacement between two reference points, representing stronger uterine contractions. The closer the two points, the stronger the contraction, and thus, the higher the reward.

![image](https://github.com/user-attachments/assets/ebab7f89-8803-42b4-98c3-469ac28623ed)

**Fig 2. Reinforcement learning workflow.**

The RL process iterates continuously, with the agent refining its actions to achieve optimal outcomes.

## Simulation oucomes:
• **Episodes**: are trials where the RL agent interacts with the environment (FEBio Studio) by adjusting 8 variables, receiving feedback as a reward after each action.
• **Fluctuations**: (episodes 0 to ~180) show the agent is exploring and learning, testing various parameter combinations, which leads to varying reward levels.
• **Stability**: Around episode 200, rewards stabilize, indicating the agent has learned optimal parameters.
• **Success Indicator**: Stable, higher rewards (-41) demonstrate effective learning and optimal uterine contraction.

![image](https://github.com/user-attachments/assets/60c98c8e-1870-40e3-ba24-b10824b4bdfd)

**Fig 3. Reward Progression Across Episodes in RL Optimization.**

![image](https://github.com/user-attachments/assets/3636f62f-b920-46cb-9622-a280fc69105a)

**Table 1. Parameters for training from literature review and optimal parameters from Reinforcement learning.** 
