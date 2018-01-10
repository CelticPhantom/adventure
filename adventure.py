from data import locations, placeDescriptions, placeObjects

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)

swagBag = []

while True:
    location = locations[position]

    #first find the max values for X and Y
    maxX = 0
    maxY = 0
    for grid, place in locations.iteritems():
        y = grid[0]
        x = grid[1]

        if x > maxX:
            maxX = x

        if y > maxY:
            maxY = y

    #now create an empty gridMap (filled with zeros)
    gridMap = [[0 for x in range(maxX +1)] for y in range(maxY + 1)]

    #sort through the locations again placing them in the gridMap
    for grid, place in locations.iteritems():
        y = grid[0]
        x = grid[1]

        #location = locations[position]
        if location == place:
            placeInit = "*"
        else:
            placeInit = place[0].upper()

        gridMap[x][y] = placeInit

    #print map
    for row in gridMap:
        print(' '.join([str(elem) for elem in row]))

    description = placeDescriptions[location]
    print 'you are at %s ' % description
    print 'You have these items :  %s' % swagBag

    stealPrompt = 'Pick from this list of items you can steal :  %s' % placeObjects[location]
    swag = raw_input(stealPrompt)
    if swag in placeObjects[location]:
        swagBag.append(swag)
    else:
        print 'You cannot steal %s here' % swag

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)

        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go?\n')
    if direction in valid_directions:
        position = valid_directions[direction]
    else :
        print '%s is NOT a valid direction' % direction

    # Print map
    # if 'north' in valid_directions:
    #     print ' N'
    # if 'west' in valid_directions:
    #     print('W', end='')
    # print '*'
    # if 'east' in valid_directions:
    #     print 'E'
    # if 'south' in valid_directions:
    #     print ' S'

