from FourRooms import FourRooms
import numpy as np
import random


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    #hyper-parameters
    learning_rate = 0.1
    discount_factor = 0.6
    exploration = 0.1
    epochs = 1000

    #creating a q-table, given set of states and set of actions
    q_table = np.zeros([12*12, 4])


    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

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
                reward -=1 


    for act in actSeq:
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)

        print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))

        if isTerminal:
            break

    # Don't forget to call newEpoch when you start a new simulation run

    # Show Path
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()