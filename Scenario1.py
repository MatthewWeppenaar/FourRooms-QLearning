from FourRooms import FourRooms
import numpy as np
import random


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    #hyper-parameters
    learning_rate = 0.1
    discount_factor = 0.6
    exploration = 0.01# very low exploration rate
    epochs = 10000

    #creating a q-table, given set of states and set of actions
    q_table = np.zeros([12*12, 4])


    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

    for trip in range(epochs):
         #reset environemt
         fourRoomsObj.newEpoch()
         #set initial terminal state to false
         isTerminal = False
         
         while not isTerminal:
            #getting a random value to decide between exploration or exploitation
            random_value = random.uniform(0,1)
            #exploration
            if (random_value < exploration):
                action = random.randint(0,3)# Explore a random action
            #exploitation
            else:
                #getting 'reward' from q-table
                one_dim = fourRoomsObj.getPosition()[0]*12+fourRoomsObj.getPosition()[1]
                action = np.argmax(q_table[one_dim])

            #creating a tempory variable to old the current state
            current_position = fourRoomsObj.getPosition()[0]*12+fourRoomsObj.getPosition()[1]
            
            #getting a new position
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(action)

            #added reward function
            reward = 0
            #if the package is collected we reward agent with 100
            if packagesRemaining == 0:
                reward = 100
            #else we penalize for each extra step
            else:
                reward -=10
            #updating q-table
            prev_q = q_table[current_position, action]
            next_max_q = np.max(q_table[newPos[0]*12+newPos[1]])
            new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
            q_table[current_position, action] = new_q
    #showing the final path
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()