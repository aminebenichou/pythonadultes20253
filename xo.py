values=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def display_table():
    print(f" {values[0]} |  {values[1]} | {values[2]} ")
    print("___|____|___")
    print(f" {values[3]} |  {values[4]} | {values[5]} ")
    print("___|____|___")
    print(f" {values[6]} |  {values[7]} | {values[8]} ")
    print("   |    |   ")
turn = 0
player= "X"
running = True
while running:
    k=0
    l=0
    display_table()
    player_input = input("Enter a number between 1 and 9: ")
    if turn%2==0:
        player = "X"
    else:
        player="O"
    if 0<int(player_input)<10:
        i = 0
        while i<len(values):
            if int(player_input)==values[i]:
                values[i] = player
            i += 1
    turn += 1

    while k<7 and running:
        if values[k]==values[k+1]==values[k+2]:
            print(f"{player} Has Won")
            running=False
            break
        k += 3
    while running and l<3:
        if values[l]==values[l+3]==values[l+6]:
            print(f"{player} Has Won")
            running=False
            break
        l += 1
    