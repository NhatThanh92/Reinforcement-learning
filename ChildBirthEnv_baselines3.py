import os
import gym
from gym import spaces
import numpy as np

import torch
import time
import math
import shutil
'''
CODE check out.txt vs out_temp.txt
'''

class childBirth_Env(gym.Env):
    def __init__(self):
        super().__init__()
        
        self.action_size = 8
        self.observation_size = 2
        self.episode_counter = 0
        action_low = np.array([0.01, 0, 0.1, 17.2, 0.85, 1.02, 0.4, 1])
        action_high = np.array([1, 0.45, 2.9, 108.3, 1.58, 1.12, 1, 10])

        #self.action_space = spaces.Discrete(1) # [0,1,10] action
        self.action_space = spaces.Box(low = action_low, high = action_high, shape =(self.action_size, ), dtype=np.float32) # action ??
        #Identical bound for each dimension
        self.observation_space = spaces.Box(low=-100, high= 260, shape=(self.observation_size,), dtype=np.float32)
        
        self.rewards = []
        #self.reset_step = int(reset_step)
        #Independent bound for each dimension
        #self.observation_space = spaces.Box(low=np.array([-1.0, -2.0]), high=np.array([2.0, 4.0]), dtype=np.float32)
        print('Finishing Initialize Environment!!!')
        
        

    def step(self, action): 
        
        self.episode_counter += 1
        #  insert "action" into  "pcesamples.txt"
        self.save_action_to_file(action, 'pcesamples.txt')
        
        
            
        # run FEbio with action, pceresult.txt (position of baby)
        cmd = 'python febio_UQ.py nobaby_1st_scale1.feb control.json'
        try:
            
            os.system(cmd)
             # read state from open pceresults.txt file
            state = self.read_state_from_file('out.txt')
            reward, done, info = self.calc_reward(state)
            
            if os.path.exists("out.txt"):
                os.remove("out.txt")
            
        except Exception as e:
            print("An error occurred:", str(e))
            reward =-46.67846
            done = False
            state = np.array([-8.54826, 38.1302])
            info = {}
                                       
        
        if self.episode_counter >= 300:
            done = True
            
        if self.episode_counter == 1:
            self.rewards = [[self.episode_counter, reward]]
        else:
            self.rewards = np.append(self.rewards, [[self.episode_counter, reward]], axis = 0)
        
        '##### REWARD.NPY #####'
        
        np.save('reward_8vars_Y_element_optimal.npy', self.rewards)
        print("episodes: {},rewards: {}, dones: {}".format(self.episode_counter, reward, done))
        #done = self._is_done()
        #info = {}
        
        return state, reward, done, info


    def calc_reward(self, state):
        
        # Calculate Euclidean distance
        info = {}
        done = False
        reward = -(state[1] - state[0])
        #if reward == -35:######################
            #done = True#######################
        return reward, done, info


    def reset(self):
    
        initial_observation = np.array([-8.54826, 38.1302], dtype=np.float32)## initial Node 614, 503
        
        return initial_observation
    
    def read_state_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        state_read = []
        for line in lines:
            # Remove leading/trailing whitespaces and split into individual values
            values = line.strip().split()
            
            # convert the values to float
            state_read.extend([float(value) for value in values])
        
        # create a numpy array from the list
        state_read = np.array(state_read)
        
        return state_read
    
    def save_action_to_file(self, action, filename):
        # Flatten the array to 1D if it's multi-dimensional
        #action_flat = action.Flatten()
        # action_size = 8: 
        action_temp = []
        for idx in range(5):
            action_temp = np.concatenate((action_temp, action))
            
            # Convert the array to strings
        action_strings = [str(value) for value in action_temp]
                
            # Join the strings with spaces to create a single line
        action_line = ' '.join(action_strings)
            
        '''
        
        # Convert the array to strings
        action_strings = [str(value) for value in action]
        
        # Join the strings with spaces to create a single line
        action_line = ' '.join(action_strings)
        '''
        with open(filename, 'w') as file:
            file.write(action_line)
    
    def _is_done(n_episodes):
        if n_episodes == 200:
            done = True
        else:
             done = False
        
        return done
