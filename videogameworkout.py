from flask import Flask, render_template, request
import random
workouts = ["Pushups", "Goblet Squats", "Kettlebell Swings", "Bicycles", "Shoulder Press", "Ab Roller", "Bicep Curls", "Tricep Extensions", "Bent Rows", "Shoulder Raises", "Meditation"]
workoutInfo = {}

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world. This will soon be a workout app for Overwatch and Rocket League'

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome. Use this form to generate a workout')

@app.route('/results', methods=['POST'])
def display_results() -> 'html':
    game = request.form['game']
    result = request.form['Result']
    gold = request.form['Gold']
    silver = request.form['Silver']
    bronze = request.form['Bronze']
    kills = request.form['Kills']
    deaths = request.form['Deaths']
    healing = request.form['Healing']
    #create a new variable to get the workout. Include it to be passed to the browser
app.run(debug=True)

"""
def main():
    game = ""
    while (game.lower() != 'q'):
        game = determineGame() #returns "overwatch" or "rocket league"
        gameInfo = getStatistics(game) #gets information about the game and saves it in a dictionary
        if gameInfo['name'] == "Overwatch":
            owWorkout(gameInfo) #pass in stat
        elif gameInfo['name'] == "Rocket League":
            rlWorkout(gameInfo)
        else:
            print("you screwed up somewhere")
        printStats(gameInfo)
        printAccumulatedWorkout(workoutInfo)
        saveGameData(gameInfo)
        saveWorkoutData(workoutInfo)
        game = input("Another game? (q to quit)")
        
def rlWorkout(gameInfo):
    
    
    if gameInfo['myScore'] >= 0 and gameInfo['opponentScore'] >= 0:
        if gameInfo['myScore'] > gameInfo['opponentScore']:
            determineRocketLeagueWin(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
        else:
            determineRocketLeagueLoss(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
    else:
        print("Doesn't make sense dude")
    return workoutInfo
    
def owWorkout(gameInfo):
    
    
    if gameInfo['result'] == "w":
        determineOverwatchWin(gameInfo['gold'], gameInfo['silver'], gameInfo['bronze'])
    elif gameInfo['result'] == "l":
        determineOverwatchLoss(gameInfo['gold'], gameInfo['silver'], gameInfo['bronze'])
    else:
        print("That's not what I asked bitch!")
    return workoutInfo
    
def nbaWorkout(gameInfo):
    if gameInfo['myScore'] >= 0 and gameInfo['opponentScore'] >= 0:
        if gameInfo['myScore'] > gameInfo['opponentScore']:
            determineRocketLeagueWin(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
        else:
            determineRocketLeagueLoss(gameInfo['goals'], gameInfo['assist'], gameInfo['saves'])
    else:
        print("Doesn't make sense dude")
    return workoutInfo
def determineRocketLeagueLoss(goals, assist, saves):
    
    workoutInfo['Exercise'] = random.choice(workouts)
    workoutInfo['Reps'] = int(round((20 - (goals * 2) - assist - saves)))
    return workoutInfo

def determineRocketLeagueWin(goals, assist, saves):

    workoutInfo['Exercise'] = random.choice(workouts)
    workoutInfo['Reps'] = random.randint(1, 10)
    return workoutInfo

def determineOverwatchWin(gold, silver, bronze):
    
    workoutInfo['Exercise'] = random.choice(workouts)
    workoutInfo['Reps'] = random.randint(1, 5)
    return workoutInfo
 
def determineOverwatchLoss(gold, silver, bronze):
    
    workoutInfo['Exercise'] = random.choice(workouts)
    workoutInfo['Reps'] = 20 - (gold * 3) - (silver * 2) - (bronze)
    return workoutInfo

def getStatistics(game):
    gameInfo = {}
    
    if game == "o":
        gameInfo['name'] = "Overwatch"
        gameInfo['result'] = input("Did you win(w) or lose(l)? ")
        gameInfo['gold'] = int(input("How many gold medals did you get? "))
        gameInfo['silver'] = int(input("How many silver medals did you get? "))
        gameInfo['bronze'] = int(input("How many bronze medals did you get? "))    
    elif game == "r":
        gameInfo['name'] = "Rocket League"
        gameInfo['myScore'] = int(input("How many goals did your team score? "))
        gameInfo['opponentScore'] = int(input("How many goals did the other team score? "))
        gameInfo['goals'] = int(input("How many goals did you score? "))
        gameInfo['assist'] = int(input("How many assists did you make? "))
        gameInfo['saves'] = int(input("How many goals did you save? "))
    elif game == "n":
        gameInfo['name'] = "NBA 2k18"
        gameInfo['myScore'] = int(input("How many goals did your team score? "))
        gameInfo['opponentScore'] = int(input("How many goals did the other team score? "))
        gameInfo['points'] = int(input("How many points did you score? "))
        gameInfo['assist'] = int(input("How many assists did you make? "))
        gameInfo['rebounds'] = int(input("How many rebounds did you have? "))
        gameInfo['steals'] = int(input("How many steals did you have? "))
        gameInfo['blocks'] = int(input("How many blocks did you have? "))
        
    else:
        print("Not Supported")
    return gameInfo

def printStats(game):
    for k, v in game.items():
        print(k, ' :', v)

def saveGameData(gameInfo):
    
    game_stats = open('game_stats.txt', 'a')
    for k, v in gameInfo.items():
        game_stats.write('\n' + str(k) + ' :' + str(v))
    game_stats.close()

def saveWorkoutData(workoutInfo):
    
    workout_log = open('workout_log.txt', 'a')
    for k, v in workoutInfo.items():
        workout_log.write('\n' + str(k) + ' :' + str(v))
    workout_log.close()     

def determineGame():
    game_played = str(input("What game did you play? Answer 'o' for Overwatch, r for Rocket League, n for NBA"))
    if game_played.lower() == "o":
        return "o"
    elif game_played.lower() == "r":
        return "r"
    elif game_played.lower() == "n":
        return "n"
    else:
        print("That isn't supported")

def accumulateWorkout(workoutInfo):
    for exercise in workoutIinfo:
        accumulatedworkout[exercise] += workoutInfo['Reps: ']
    return workoutAccumulated

def printAccumulatedWorkout(workoutAccumulated):
    for k, v in workoutAccumulated.items():
        print(k, ' :', v)
main()"""
