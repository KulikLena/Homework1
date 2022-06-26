import time

class MultiplayerConsoleGame(object):
    
    board=[' ' for i in range(1,10)]

    def __init__(self,game):
        self.game=game 

    def get_answer(self):
        answer = int(input("Enter 1 or 2: "))
        return answer

    def show_menu(self):
        print("Please, chose the option \n1. Play a game\n2. Show statistic\n")

    def change_player():
         pass

    def show_the_board (self, board):
        self.board=board 
        print("   A    B    C")
        print()
        print ('1',' ',board[0],'|',board[1],'|', board[2])
        print("    _________")
        print ('2',' ',board[3],'|',board[4],'|', board[5])
        print("    _________")
        print ('3',' ',board[6],'|',board[7],'|', board[8])
        print()
        return board 

    def update_the_board (self,board):
        self.board=board 
        self.show_the_board(board)
        return board

    def get_the_move(self, sighn):
        r=True
        while r: 
            row=input("Number of rows: 1, 2 or 3 ")
            column=input("Number of columns: A, B or C ")
            player_move=[row,column]
            match player_move:
                case ['1','A']:
                    i=0
                case ['1','B']:
                    i=1
                case ['1','C']:
                    i=2
                case ['2','A']:
                    i=3
                case ['2','B']:
                    i=4
                case ['2','C']:
                    i=5
                case ['3','A']:
                    i=6
                case ['3','B']:
                    i=7
                case ['3','C']:
                    i=8
            if self.board[i]=="x" or self.board[i]=="o":
                 print ("The cell you trying to move is not empty. Let's try again")
            else: 
                self.board[i]=sighn
                r=False

        return self.board

    def check_result(self, board):
        result = False
        res=''
        if  board[0]!=" " and board[0]==board[1] and board[0]==board[2]:
                result=True
                print (f"Player {board[0]} has won" )
                res=board[0]
        elif board[3]!=" " and board[3]==board[4] and board[3]==board[5]:
                result=True
                res=board[3]
                print (f"Player {board[3]} has won" )
        elif board[6]!=" " and board[6]==board[7] and board[6]==board[8]:
                result=True
                res=board[6]
                print (f"Player {board[6]} has won" )
        elif  board[0]!=" " and board[0]==board[3] and board[0]==board[6]:
                result=True
                print (f"Player {board[0]} has won" )
                res=board[0]
        elif board[1]!=" " and board[1]==board[4] and board[1]==board[7]:
                result=True
                res=board[1]
                print (f"Player {board[3]} has won" )
        elif board[2]!=" " and board[2]==board[5] and board[2]==board[8]:
                result=True
                res=board[2]
                print (f"Player {board[6]} has won" )
        elif board[0]!=" " and board[0]==board[4] and board[0]==board[8]:
                result=True
                res=board[0]
                print (f"Player {board[6]} has won" )
        elif board[2]!=" " and board[2]==board[4] and board[2]==board[6]:
                result=True
                res=board[2]
                print (f"Player {board[2]} has won" )

        elif " " not in self.board:
                result=True
                res='draw'
                print ('It is a draw!' )
        return result,res

    def write_stats (self, x,o, draw, avg_duration):
        self.x=x
        self.o=o
        self.draw=draw
        self.avg_duration=avg_duration
        st = open('some_stats.txt','w')
        line1=str(f'Player x has won {x} times\n',)
        line2=str(f'Player o has won {o} times\n')
        line3=str(f'Draw has occureed {draw} times\n')
        line4=str(f'Average duration of the games is: {avg_duration} sec ')
        st.write(line1)
        st.write(line2)
        st.write(line3)
        st.write (line4)
        st.seek(0)
        st.close()
        return st

    def play_game(self):
        count = 0
        countin= True
        player_x=0
        player_o=0
        draw=0
        duration=0
        number_of_games=0
        result=False
        while countin:
              self.board=[' ' for i in range(1,10)]
              self.show_the_board(self.board)
              start=time.time()
              while " " in self.board and result==False:
                if count%2==0:
                    print("It's turn of player 1. Please, choose the epmty cell: ")
                    self.get_the_move("x")
                    result=self.check_result(self.board)[0]
                else: 
                    print("It's turn of player 2. Please, choose the epmty cell: ")
                    self.get_the_move("o")
                    result=self.check_result(self.board)[0]
                self.update_the_board(self.board)
                count=count+1
              if  self.check_result(self.board)[1] == 'x':
                  player_x=player_x+1
              elif self.check_result(self.board)[1] == 'o':
                  player_o=player_o+1
              elif self.check_result(self.board)[1]  =='draw':
                  draw=draw+1
              number_of_games=number_of_games+1
              end = time.time()
              game_duration = end-start
              print(game_duration)
              duration = duration + game_duration
              print(duration)
              average_duration = duration/number_of_games
              answer_to_continue =input("Do you want to continue the game: Y or N?: ")
              if answer_to_continue=='Y':
                  result=False
                  countin = True
                  print(player_x)
                  print(player_o)
                  print(draw)
              else:
                  countin = False

        self.write_stats(player_x,player_o,draw, average_duration)
        return player_x, player_o, draw

    
    def show_statistic(self,file):
        self.file=open(file, 'r')
        print(self.file.read())
        self.file.close()
       
    def close_the_game():
        pass


def main():
    con=True
    while con:
        tttoe=MultiplayerConsoleGame('tic_tac_toe')
        tttoe.show_menu()
        answ=tttoe.get_answer()
        if answ==1:
            tttoe.play_game()
        elif answ==2:
            tttoe.show_statistic('some_stats.txt')

        
        answer = input("Do you want to continue the session: Y or N? ")
        if answer=='N':
            con=False


if __name__ == '__main__':
   main()
