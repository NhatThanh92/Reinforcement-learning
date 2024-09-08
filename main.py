import numpy as np
import gym
from gym.envs.registration import register
from stable_baselines3 import DDPG
from stable_baselines3.common.env_util import make_vec_env

import argparse

import environments
#from ActEnv_baselines3 import ActEnv


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_parser(parser=None):
    parser = parser or argparse.ArgumentParser(description='RL')
    parser.conflict_handler = 'resolve'
    parser.add_argument('--env', default='childBirthEnv-v0',
                        help='environment to train on')
    parser.add_argument('--reset_step', type=int, default=300, help='Reset envs every n iters.')
    parser.add_argument('--test', type=str2bool, default=False, help='Evaluate a trained model.')
    parser.add_argument('--alg', default='DDPG',
                        help='algorithm to use: A2C | DDPG | PPO | SAC | TD3')
    
    return parser

def save_action_to_file(action, filename):
    # Flatten the array to 1D if it's multi-dimensional
    #action_flat = action.Flatten()
    
    # Convert the array to strings
    action_strings = [str(value) for value in action]
    
    # Join the strings with spaces to create a single line
    action_line = ' '.join(action_strings)
    
    with open(filename, 'w') as file:
        file.write(action_line)


#args = get_parser().parse_args()
# Instantiate the env
env = gym.make('childBirthEnv-v0')
vec_env = make_vec_env(lambda: env, n_envs=1, seed=None)

# Train the agent

model = DDPG("MlpPolicy", vec_env, verbose=1, learning_starts=200) # F 

model.learn(total_timesteps=500, log_interval=10)

model.save("DDPG_8vars_Y_element_3483")


## Save each 50 episodes ##

for idx in range(10):
    model = DDPG("MlpPolicy", vec_env, verbose=1, learning_starts=200) # F 
    model.learn(total_timesteps=50, log_interval=10)
    model.save("DDPG_alg_" + str(idx))


## Test ##

model = DDPG.load("DDPG_8vars_Y_element", env=env)

obs = env.reset()
action, _states = model.predict(obs) # obs -> pridict new action,state 
save_action_to_file(action, 'pcesamples_opt.txt')

obs, rewards, dones, info = env.step(action)
print(rewards)
