#################################################
# Solution for problem 1 of Advent of Code 2023 #
#################################################

numbers_in_str_format = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def getTotalCalibration(file_name, should_validate_word):
    total_calibration = 0

    with open(file_name, 'r') as file:
        for line in file:

            numbers = []
            word = ''
            for char in line:
                if char.isdigit():
                    numbers.append(int(char))
                elif should_validate_word:
                    word += char
                    if wordIsKey(word):
                        numbers.append(extractNumber(word))
                    word = clearWord(word)

            if len(numbers) >= 2: 
                first_number = numbers.pop(0)
                last_number = numbers.pop(-1)
            else:
                first_number = numbers.pop(0)
                last_number = first_number

            two_digits_number = int(str(first_number) + str(last_number))
            total_calibration += two_digits_number

    return total_calibration  

def keysContainKeyStartingWithWord(word):
    for key in numbers_in_str_format.keys():
        if key.startswith(word):
            return True
    return False

def wordIsKey(word):
    for key in numbers_in_str_format.keys():
        if key == word:
            return True
    return False

def clearWord(word):
    new_word = word
    while len(new_word) > 0 and (wordIsKey(new_word) or not keysContainKeyStartingWithWord(new_word)):
        new_word = new_word[1:]
    return new_word

def extractNumber(word):
    return numbers_in_str_format.get(word)

print("(1) The total calibration for test is: " + str(getTotalCalibration('test1.txt', False)))
print("(1) The total calibration is: " + str(getTotalCalibration('input.txt', False)))

print("(2) The total calibration for test is: " + str(getTotalCalibration('test2.txt', True)))
print("(2) The total calibration is: " + str(getTotalCalibration('input.txt', True)))