import random as R

# Function to roll 2 digital dice by getting a random integer
def roll_dice():
    roll1 = R.randint(1,6)
    roll2 = R.randint(1,6)
    rolls = roll1, roll2
    return rolls

# Function to take the computers turn with a set goal
def computer_turn(game_score, goal):
    turn_total = 0
    ones = 0
    while turn_total < goal:
        turn = roll_dice()
        for num in turn:
            if num == 1:
                ones += 1
        if ones == 2:
            turn_total = 0
            print(f'Computer rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
            game_score = 0
            return game_score
        if ones == 1:
            game_score -= turn_total
            turn_total = 0
            print(f'Computer rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
            return game_score
        else:
            turn_total += sum(turn)
            game_score += sum(turn)
            print(f'Computer rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
    return game_score

def human_turn(game_score):
    turn_total = 0
    while True:
        ones = 0
        roll = input("Roll again (y/n)? ").lower()
        if roll == 'n':
            return game_score
        elif roll == 'y':
            turn = roll_dice()
            for num in turn:
                if num == 1:
                    ones += 1
            if ones == 2:
                game_score = 0
                turn_total = 0
                print(f'You rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
                return game_score
            elif ones == 1:
                game_score -= turn_total
                turn_total = 0
                print(f'You rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
                return game_score
            else:
                turn_total += sum(turn)
                game_score += sum(turn)
                print(f'You rolled {turn[0]},{turn[1]} Turn total: {turn_total}')
        else:
            print("Invalid input. Please enter 'y' to roll or 'n' to end turn.")

def human_vs_computer():
    human_score = 0
    computer_score = 0
    goal = 100
    
    while human_score < goal and computer_score < goal:
        human_score = human_turn(human_score)
        print(f'You: {human_score} Computer: {computer_score}------------------------------')

        computer_score = computer_turn(computer_score, 20)
        print(f'You: {human_score} Computer: {computer_score}------------------------------')

def computer_solo(goal):
    computer_score = 0
    turn = 0
    while computer_score < 100:
        computer_score = computer_turn(computer_score, goal)
        turn += 1
        print(f'Turn: {turn} Score: {computer_score}-------------------')
    print(f'Turns {turn}')
    return turn

def world_championship(games, goal_1, goal_2):
    cpu1_games = 0
    cpu2_games = 0
    game = 1
    for game in range(games):
        computer_1_score = 0
        computer_2_score = 0
        while computer_1_score < 100 and computer_2_score < 100:
            computer_1_score = computer_turn(computer_1_score, goal_1)
            print(f'Alexa: {computer_1_score} Siri: {computer_2_score}')
            if computer_1_score >= 100:
                cpu1_games += 1
            computer_2_score = computer_turn(computer_2_score, goal_2)
            print(f'Alexa: {computer_1_score} Siri: {computer_2_score}')
            if computer_2_score >= 100:
                cpu2_games += 1
        print(f'Alexa: {cpu1_games} Siri: {cpu2_games}')
        game += 1
    return cpu1_games, cpu2_games

if __name__ == '__main__':
    world_championship(7, 30, 25)




