
from colorama import Fore, Style
o = f'{Fore.YELLOW}o{Style.RESET_ALL}'
x = f'{Fore.LIGHTBLUE_EX}x{Style.RESET_ALL}'
def dead_heat(board: list) -> bool:
    for i in board:
        if i != x and i != o:
           return False
    return True

def make_move(board: list, index: str, current_layer: str) -> bool:
    if index == '' or index.isdigit() == False:
        print(f'{Fore.RED}введите цифры{Style.RESET_ALL}')
        return False
    elif 9 > int(index) >= 0 and board[int(index)] != x and board[int(index)] != o:
        board[int(index)] = current_layer
        return True
    else:
        print(f'{Fore.RED}так нельзя, попробуйте снова{Style.RESET_ALL} ')
        return False

def create_board() -> list:
    list=[]
    for i in range(9):
        list.append(str(i))
    return list

def draw_board(board:list):
    for i in range(0,9,3):
        print('\t\t\t',' | '.join(board[i:i+3]))
        if i!=6:
           print('\t\t\t','-'*9)

def chek_winner(board:list,current_player:str)->bool:
    for i in range(0,9,3):#проверяет 0 1 2 , 3 4 5 , 6 7 8
       if board[i]==board[i+1]==board[i+2]==current_player:
           return True
    for i in range(0,3):#0 3 6, 2 5 8, 1 4 7
       if board[i]==board[i+3]==board[i+6]==current_player:
           return True
    if board[0]==board[4]==board[8]==current_player:#0 4 8
        return True
    if board[2]==board[4]==board[6]==current_player:#2 4 6
        return True
    return False

def main():
    print(f'{Fore.GREEN}\n\tДОБРО ПОЖАЛОВАТЬ В ИГРУ "КРЕСТИКИ НОЛИКИ"\n{Style.RESET_ALL}')
    board=create_board()
    draw_board(board)
    players=[x,o]
    current_player=players[0]
    while True:
        print(f'{Fore.CYAN}\n\t\t\tход игрока {current_player}{Style.RESET_ALL}')
        index=input(f'{Fore.LIGHTBLUE_EX}\n\t\tвведите индекс (0-8):{Style.RESET_ALL} ')
        if make_move(board,index,current_player)==True:
            draw_board(board)
            if chek_winner(board,current_player)==True:
                print(f'{current_player}{Fore.LIGHTGREEN_EX} победил!{Style.RESET_ALL}')
                break
            elif dead_heat(board):
                 print(f'{Fore.LIGHTWHITE_EX}Ничья{Style.RESET_ALL}')
                 break
            else:
                if current_player==x:
                    current_player=players[1]
                else:
                    current_player=players[0]

main()

