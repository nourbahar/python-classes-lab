class Game():

    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }


    winning_combinations = [
        ['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],
        ['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],
        ['a1','b2','c3'],['c1','b2','a3']
        ]
    
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def play_game(self):    
       print("Welcome Tic Tac Toe!")

       while not(self.winner) and not(self.tie):
        self.render()
        move=self.get_move()
        self.board[move] = self.turn 
        self.check_winner()
        self.check_tie()
        self.switch_turn()
        self.render()

   
    def print_message(self):
        if(self.tie):
            print("It's a tie!")
        elif(self.winner):
            print(f'{self.winner} wins the game!')
        else:
            print(f"it's player {self.turn}'s turn!")

    def render(self):
        Game.print_board(self)
        Game.print_message(self)
    
    def get_move(self):
        while True:
            self.move = input(f"Enter your move: ").lower()
            if(self.move in self.board and not self.board[self.move]):
                self.board[self.move] = self.turn
                break
            else:
                print("Invalid move! Please try again.")
    
    def check_winner(self):
        b = self.board
        for combo in Game.winning_combinations:
            if (b[combo[0]] and b[combo[0]] == b[combo[1]] and b[combo[0]] == b[combo[2]]):
                self.winner = self.turn

    def check_tie(self):
        if(not None in self.board.values() and self.winner == None):
            self.tie = True

    def switch_turn(self):
        if (self.turn == 'X'):
            self.turn = 'O'
        elif (self.turn == 'O'):
            self.turn = 'X'

game_instance = Game()
game_instance.play_game()