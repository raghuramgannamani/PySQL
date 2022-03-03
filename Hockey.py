def main():
    Team = input("Enter Team Name:")
    Wins = int(input("Enter No of Wins:"))
    Loss = int(input("Enter No of Loss:"))
    Total = Wins + Loss
    print(f"{Team} played {Total} matches and won {Wins} and Lost {Loss} with a win percent of", (Wins/Total)*100, "%")
main()