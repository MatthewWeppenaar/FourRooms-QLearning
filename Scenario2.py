from FourRooms import FourRooms
import numpy as np
import random

def convertTo1D(n):
    #takes in a tuple(x,y) and it converts it into a 1d index for the Q-table
    postion = n[0]*12+n[1]
    return postion



def main():

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    # Create FourRooms Object
    fourRoomsObj = FourRooms('multi')

    #hyper-parameters
    learning_rate = 0.1
    discount_factor = 0.8
    exploration_max = 1.0  # Initial exploration rate
    exploration_min = 0.01  # Final exploration rate
    exploration_decay = 0.001  # Rate of exploration dec
    epochs = 10000
    #creating a q-table, given set of states and set of actions
    q_table = np.zeros([4,144, 4])
    print(q_table[0][1])

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

    
    for trip in range(epochs):
    
         
         
         print(trip)
         print(fourRoomsObj.getPackagesRemaining())
         print(q_table[fourRoomsObj.getPackagesRemaining()])
         #reset environemt
         fourRoomsObj.newEpoch()
         #set initial terminal state to false
         isTerminal = False
         state = fourRoomsObj.getPosition()
         subgoals = 3
         
         
         
         while not isTerminal:
            #getting a random value to decide between exploration or exploitation
            random_value = random.uniform(0,1)
            #exploration
            if (random_value < exploration):
                action = random.randint(0,3)# Explore a random action
            #exploitation
            else:
                #getting 'reward' from q-table
                action = np.argmax(q_table[fourRoomsObj.getPackagesRemaining(),convertTo1D(state)])

            #creating a tempory variable to old the current state
            current_position = convertTo1D(state)
            
            #getting a new position
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(action)

            #added reward function

            
            reward = 0
            #if the package is collected we reward agent with 100

            if packagesRemaining<subgoals:
                reward+=10
            
            reward-=0.1
            #if packagesRemaining == 0:
               # reward += 5

            #elif packagesRemaining==1:
                #reward += 2

            #elif packagesRemaining == 2:
                #reward +=1
            
            
            #reward -= 0.01
            #reward += 0.5*(3-packagesRemaining)

            prev_q = q_table[packagesRemaining,current_position, action]
            next_max_q = np.max(q_table[packagesRemaining,convertTo1D(newPos)])
            new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
            q_table[packagesRemaining,current_position, action] = new_q

            state = newPos

         if packagesRemaining == 0:
            subgoals -= 1
        
         exploration *= exploration_decay
         exploration = max(exploration,exploration_min)
        
            #print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[action], newPos, gTypes[gridType]))
    #showing the final path
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()