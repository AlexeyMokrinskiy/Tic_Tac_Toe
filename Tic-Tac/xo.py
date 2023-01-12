import emoji

map = list(range(1,10))

def draw_board(map):
    print(emoji.emojize(':white_large_square:') * 9)
    for i in range(3):
        print(emoji.emojize(':white_large_square:'), map[0+i*3], emoji.emojize(':white_large_square:') , 
        map[1+i*3], emoji.emojize(':white_large_square:'), map[2+i*3], emoji.emojize(':white_large_square:'))
        print(emoji.emojize(':white_large_square:') * 9)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+" ? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(map[player_answer-1]) not in "XO"):
                map[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(emoji.emojize(':cross_mark:'))
        else:
            take_input(emoji.emojize(':hollow_red_circle:'))
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(map)

# py -m pip freeze > requirements.txt
# py -m pip install -r requirements.txt