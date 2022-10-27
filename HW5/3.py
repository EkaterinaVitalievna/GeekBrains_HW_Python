#Создайте программу для игры в ""Крестики-нолики"".
import random as r

# рисуем поле
board = list(range (1, 10))
def play_form ():
    print('-------------')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')
play_form ()

# определение конца игры
def vin_table(chec_vin, pl, step, simbol):
    if step == 8:
        print ("Победителей нет")
        return True
    for i in range(len(chec_vin)-1):
        if chec_vin[i][0] == chec_vin[i][1] == chec_vin[i][2]:
                print (f'Победил игрок играющией  {simbol}')
                return True


# Запоминание действий игроков
def enter_simbol (simbol, pl, memory_vin, step):
    num = int(input(f'Игрок номер {pl} определите номер ячейки в которую ставим {simbol} : '))
    while board [num-1] == "X" or board [num-1] == "O":
        print ("Эта ячейка уже занята")
        num = int(input(f'Игрок номер {pl} еще раз определите номер ячейки в которую ставим {simbol} : '))
    else:
        board [num-1] = simbol
        step +=1
        for i in range(len(memory_vin)):
            for j in range(3):
                if memory_vin[i][j] == num:
                    memory_vin[i][j] = simbol
    return 


print ('Первый игрок  "X", второй игрок играет "O"\n Выберите кто играет первым первый или второй игрок\n')
player = int(input("Введите номер игрока :"))
step = 0
if player == 1: 
    sim_play = 'X'
elif player == 2:
    sim_play = 'O'

memory = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
while vin_table(memory, player, step, sim_play) != True:
    if player == 1:
        sim_play = "X"
        enter_simbol(sim_play, 1, memory, step)
        player =2
        play_form()
    elif player == 2:
        sim_play = "O"
        enter_simbol(sim_play, 2, memory, step)
        player =1
        play_form()

exit ()

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Выш ход," + turn + ".Куда поставить знак?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Эта позиция уже занята.\nКуда поставить знак?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard[
                '9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard[
                '6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard[
                '3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard[
                '7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard[
                '8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard[
                '9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard[
                '3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard[
                '9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break

        if count == 9:
            print("\nКонец игры.\n")
            print("Ничья!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Хотите сыграть ещё раз?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()