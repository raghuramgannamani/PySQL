
"""
Student Name:     
Program Title:  Hockey  
Description:   It's hockey! 

Write a program that will ask the user to
1. enter the name of a hockey team, 
2. how many wins the team has and 
3.how many losses the team has.

The program should calculate and display a single string output containing the team name, 
it's win-loss ratio and the win percentage formatted to 4 decimal places.

Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #1. Variables
    teamName = ""
    numWins = 0
    numLosses = 0 
    totalGames = 0
    winPct = 0.0  #win percentage variable

    #2. Welcome
    print("Welcome to the Team Program\n")
    
    #3. Ask user for team name 
    teamName = input("Please enter a team name: ")

    #4. Ask for # wins from user
    numWins = input("Please enter number of wins: ")

    #5. Ask for # losses from user
    numLosses = input("Please enter number of losses: ")

    #6. PROCESSING
    #   total games = wins + losses
    #   win pct = wins / total games
    totalGames = int(numWins) + int(numLosses)
    winPct = int(numWins) / totalGames

    #OUTPUT
    #7. Build and print display string
    #7A. Format win % to 4 decimals
    # print(teamName + " had " + numWins + " wins and " 
    #     + numLosses + " losses and a win percentage of " + str(round(winPct, 4)))

    outputString = "{0} had {1} wins and {2} losses and a win percentage of {3:.4f}".format(teamName, numWins, numLosses, winPct)
    print(outputString)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()