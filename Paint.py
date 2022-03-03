def main():

    print("Amount of paint required to paint the wall")
    WidthOfWall1 = int(input("Enter the Width of wall 1 : "))
    LenghtOfWall1 = input("Enter the Length of wall 1 : ")
    WidthOfWall2 = int(input("Enter the width of wall 2: "))
    LenghtOfWall2 = int(input("Enter the Lenght of wall 2:"))
#total number of walls in a room are 4. Wall 1,2 and Wall 3,4

    Area = 2*(WidthOfWall1 * int(LenghtOfWall1)) + 2*(WidthOfWall2 * LenghtOfWall2)
 
    print('Total Area to be painted:',Area)
    GallonsPaint = Area/150
    print('Total paint required to paint all four walls:',GallonsPaint)
main()