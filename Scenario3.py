from FourRooms import FourRooms
import numpy as np
import random
import time
import sys

def convertTo1D(n):
    # takes in a tuple (x, y) and converts it into a 1D index for the Q-table
    position = n[0] * 12 + n[1]
    return position

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-stochastic":
            fourRoomsObj = FourRooms('rgb',stochastic="True")
    else:
        fourRoomsObj = FourRooms('rgb')
    # Hyperparameters
    learning_rate = 0.3
    discount_factor = 0.95
    exploration_max = 1  # Initial exploration rate
    exploration_min = 0.01  # Final exploration rate
    exploration_decay = 0.01 # Rate of exploration decay
    epochs = 2000
    order = [1, 2, 3] #expexted order of collection
    
    # Creating a Q-table, given the set of states and set of actions
    q_table = np.zeros([12 * 12, 4])

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))
    start_time = time.time()
   
    for trip in range(epochs):
        fourRoomsObj.newEpoch()
        state = fourRoomsObj.getPosition()
        # Reset environment
        expected_package = 1 # starts off expexting red package i.e package 1
        # Set initial terminal state to False
        isTerminal = False
        #adding exploration decay
        exploration = exploration_min + (exploration_max - exploration_min) * np.exp(-exploration_decay * trip)

        while not isTerminal:
            # Getting a random value to decide between exploration or exploitation
            random_value = random.uniform(0, 1)
            # Exploration
            if random_value < exploration:
                action = random.randint(0, 3)  # Explore a random action
            # Exploitation
            else:
                # Getting 'reward' from q-table
                action = np.argmax(q_table[convertTo1D(state)])

            # Creating a temporary variable to hold the current state
            current_position = convertTo1D(state)

            # Getting a new position
            gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(action)
           
                
            reward = 0

            # Added reward function
            if packagesRemaining == 3 - expected_package:
                expected_color = order[expected_package-1]  # Get the color of the expected package
                if gridType == expected_color:
                    reward += 50
                    expected_package += 1
                else:
                    reward -= 1
                
            reward -= 1
            
            
            prev_q = q_table[current_position, action]
            next_max_q = np.max(q_table[convertTo1D(newPos)])
            new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
            q_table[current_position, action] = new_q

            state = newPos

            
    # Showing the final path
    print("Time taken to run {0} Epochs".format(epochs))
    print("--- %s seconds ---" % (time.time() - start_time))
    if len(sys.argv) == 2:
        if sys.argv[1] == "-stochastic":
            fourRoomsObj.showPath(-1,"Scenario_3(stochastic).png")
    else:
        fourRoomsObj.showPath(-1,"Scenario_3.png")

if __name__ == "__main__":
    main()
