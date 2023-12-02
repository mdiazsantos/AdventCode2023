#################################################
# Solution for problem 2 of Advent of Code 2023 #
#################################################

#############
# Constants #
#############

cubes_bag = {
    "blue": 14,
    "red": 12,
    "green": 13
}


###########
# Classes #
###########

class CubeColor:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        return f"CubeColor(name={self.name}, count={self.count})"
    
class Result:
    def __init__(self, total_sum, total_power):
        self.total_sum = total_sum
        self.total_power = total_power


############# 
# Functions #
#############

# Retrieves a result with the total power for all games in a file and the total of games possible with our cube bag.
def getSumOfPossibleGamesAndTotalPowerForAllGames(file_name):
    total_sum = 0
    total_power = 0
    with open(file_name, 'r') as file:
        for line in file:
            line_split = line.split(':')
            game_id_number = extractGameNumber(''.join(line_split[0]))

            possible_game, total_power_per_game = processGame(''.join(line_split[1:]))
            total_power += total_power_per_game
            if possible_game:
                total_sum += game_id_number          

    return Result(total_sum, total_power)


# Checks if game is possible and retrieves the total power for all cube colors in game. 
# The power is the minimum number of cubes per color to make game possible.
def processGame(game_combination):
    # print('Game combination: ' + game_combination)
    cube_colors = []
    cube_colors_with_minimun_values = []        # Cube colors with minimum values for make possible the game
    number = ''
    color = ''
    combinations_are_possible = True
    for char in game_combination:
        if char == ';':
            # New set of cubes
            cube_colors = []

        if char.isdigit():
            number = number + char

        if char.isalpha():
            color = color + char
        
        if colorIsKey(color):
            cube_colors.append(CubeColor(name=color, count=int(number)))
            if not isPossibleCombination(cube_colors, cubes_bag):
                combinations_are_possible = False
            updateMinimums(cube_colors_with_minimun_values, cube_colors)
            number = ''
            color = ''

    # print('All combinations for game are possible? ' + str(combinations_are_possible))
    combine_power_for_game = extractPower(cube_colors_with_minimun_values)
    # print('Power for game is: ' + str(combine_power_for_game))
    # print('##################################\n')
    return combinations_are_possible, combine_power_for_game


# Update needed minimums for game to be possible.
def updateMinimums(cube_colors_with_minimun_values, cube_colors):
    for new_cube_color in cube_colors:
        cube_color_with_same_name = next((cube_color for cube_color in cube_colors_with_minimun_values if cube_color.name == new_cube_color.name), None)

        if cube_color_with_same_name is None:
            cube_colors_with_minimun_values.append(new_cube_color)
        else:
            if new_cube_color.count > cube_color_with_same_name.count:
                cube_color_with_same_name.count = new_cube_color.count


# Extract the power of cubes for a game.
def extractPower(cube_colors_with_minimun_values):
    power = 1
    for cube_color in cube_colors_with_minimun_values:
        power *= cube_color.count
    return power


# Checks if a color is an available key from colors in bag.
def colorIsKey(color):
    for key in cubes_bag.keys():
        if key == color:
            return True
    return False


# Extracts game ID from line.
def extractGameNumber(game_id):
    # print('\n##################################')
    # print('Game ID: ' + game_id)
    game_id_number = game_id.replace('Game ', '')
    return int(game_id_number)


# Checks if cube combination is possible by checking if there are enough cube colors in bag.
def isPossibleCombination(cube_colors, cubes_bag):
    for cube_color in cube_colors:
        if cubes_bag.get(cube_color.name) < cube_color.count:
            return False
    return True


###########
# Results #
###########
test_result = getSumOfPossibleGamesAndTotalPowerForAllGames('test1.txt')
print("(1) The total sum of possible game ids for test is: " + str(test_result.total_sum))
print("(2) The total power for games for test is: " + str(test_result.total_power))

problem_result = getSumOfPossibleGamesAndTotalPowerForAllGames('input.txt')
print("(1) The total sum of possible game ids is: " + str(problem_result.total_sum))
print("(2) The total power for games is: " + str(problem_result.total_power))