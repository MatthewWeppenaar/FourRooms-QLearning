from FourRooms import FourRooms


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    #hyper-parameters
    learning_rate = 0.1
    discount_factor = 0.6
    exploration = 0.1
    epochs = 1000

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

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