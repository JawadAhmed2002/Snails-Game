import arcade
import os
import numpy as np

# Load Files from current directory
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
WelcomeImage = os.path.join(THIS_FOLDER, 'welcome.jpg')
Background_image = arcade.load_texture(
    os.path.join(THIS_FOLDER, "background.jpeg"))
Backend_Background = arcade.load_texture(
    os.path.join(THIS_FOLDER, "backend_Background.jpg"))
Instruction_Screen = arcade.load_texture(
    os.path.join(THIS_FOLDER, "instruction.jpg"))
vs = arcade.load_texture(os.path.join(THIS_FOLDER, "vs.png"))
logo = arcade.load_texture(os.path.join(THIS_FOLDER, "logo.png"))
# silver player is Bot
silverPlayer = arcade.load_texture(
    os.path.join(THIS_FOLDER, "silverPlayer.png"))
silverSplash = arcade.load_texture(
    os.path.join(THIS_FOLDER, "silverSplash.png"))
# Red Player human
redPlayer = arcade.load_texture(os.path.join(THIS_FOLDER, "redPlayer.png"))
redSplash = arcade.load_texture(os.path.join(THIS_FOLDER, "redSplash.png"))

# Screen Title and its Length, Width
SCREEN_TITLE = "Snails Game "
Length = 700
Width = 1100

# Welcome Screen


class MenuView(arcade.View):
    def on_show(self):
        self.welcome = arcade.load_texture(WelcomeImage)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(550, 350, 1100,
                                      700, self.welcome)
        arcade.draw_text("Welcome To Snails Game", 560, 600,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        arcade.draw_text("Click Will Switch to Rules Page", 560, 560,
                         arcade.color.BLACK_BEAN, font_size=17, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

# Snails Game Screen


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.backend_Background = Backend_Background
        self.logo = logo
        self.vs = vs
        self.grid = []
        self.silverPlayer = "1"
        self.redPlayer = "2"
        self.win = "0"
        self.state = "InstructionMenu"
        self.turn = "Red_Player"
        self.silverPlayerPosition = 0, 9
        self.redPlayerPosition = 9, 0
        self.silverScore = 0
        self.redScore = 0
        self.turnsCount = 0
        self.gridInitialization()

    def gridInitialization(self):
        self.grid = np.zeros((10, 10))
        self.grid[0][9] = 1
        self.grid[9][0] = 2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(650, 350, 1300,
                                      850, self.backend_Background)
        # Instruction Menu
        if self.state == "InstructionMenu":
            arcade.draw_texture_rectangle(600, 400, 1600,
                                          800, Instruction_Screen)
            arcade.draw_text("Instructions Screen", 560, 600,
                             arcade.color.BLACK, font_size=50, anchor_x="center")
            arcade.draw_text("Press Space Button to Play Game", 560, 560,
                             arcade.color.DARK_BLUE, font_size=20, anchor_x="center")

            arcade.draw_text("Rules", 60, 500,
                             arcade.color.BLACK, font_size=20, anchor_x="center")

            arcade.draw_text("1- Capture maximum number of boxes to win the Game.",
                             50, 470, arcade.color.BLACK, font_size=15)
            arcade.draw_text("2- You can roll back through your own splashes.",
                             50, 440, arcade.color.BLACK, font_size=15)
            arcade.draw_text("3- Any Player that capture 50 boxes will be winner.",
                             50, 410, arcade.color.BLACK, font_size=15)
            arcade.draw_text("4- You cannot move/jump through opponent's player snail/splash.",
                             50, 380, arcade.color.BLACK, font_size=15)
            arcade.draw_text("5- Bot Snail is at TOP RIGHT CORNER.",
                             50, 350, arcade.color.BLACK, font_size=15)
            arcade.draw_text("6- Human Snail is at BOTTOM LEFT CORNER.",
                             50, 320, arcade.color.BLACK, font_size=15)
            arcade.draw_text("7- Turn will be lost if you click on opponent Snail/Splash.",
                             50, 290, arcade.color.BLACK, font_size=15)
            arcade.draw_text("8- You can only move LEFT, RIGHT, UP, DOWN.",
                             50, 260, arcade.color.BLACK, font_size=15)
            arcade.draw_text("9- Always click on box that is next to your Snail.",
                             50, 230, arcade.color.BLACK, font_size=15)
            arcade.draw_text("     Otherwise you will lose your TURN.",
                             50, 200, arcade.color.BLACK, font_size=15)

        elif self.state == "GameOn":
            arcade.draw_lrwh_rectangle_textured(
                0, 0, 600, 600, Background_image)
            # Draw Logo
            arcade.draw_texture_rectangle(870, 620, 140,
                                          140, self.logo)
            # Side Title
            arcade.draw_text("Snails Game", 720, 500,
                             arcade.color.DARK_ORANGE, 33)
            arcade.draw_rectangle_filled(870, 430, 450,
                                         120, arcade.color.SILVER_LAKE_BLUE)

            arcade.draw_texture_rectangle(870, 410, 60,
                                          60, self.vs)
            arcade.draw_text("PLAYERS:  ", 650, 450,
                             arcade.color.WHITE, 19)

            arcade.draw_text("Red-Bird(Human) ", 650, 420,
                             arcade.color.WHITE, 17)

            arcade.draw_text("Silver-Bird(Bot) ", 900, 420,
                             arcade.color.WHITE, 17)

            # Score
            arcade.draw_text("Red-Bird Score: ", 650, 380,
                             arcade.color.WHITE, 13.5)

            arcade.draw_text("Silver-Bird Score: ", 900, 380,
                             arcade.color.WHITE, 13.5)

            arcade.draw_text(str(self.redScore), 800, 380,
                             arcade.color.WHITE, 13.5)

            arcade.draw_text(str(self.silverScore), 1060, 380,
                             arcade.color.WHITE, 13.5)

            if self.turn == 'Red_Player':
                arcade.draw_text("Red-Bird(Human) ", 650, 420,
                                 arcade.color.BLACK, 17)

                arcade.draw_text(str(self.redScore), 800, 380,
                                 arcade.color.BLACK, 13.5)

                arcade.draw_text("Red-Bird Score: ", 650, 380,
                                 arcade.color.BLACK, 13.5)
                arcade.draw_text("HUMAN TURN ", 790, 450,
                                 arcade.color.BLACK_BEAN, 19)

            else:
                arcade.draw_text("Silver-Bird(Bot) ", 900, 420,
                                 arcade.color.BLACK, 17)

                arcade.draw_text(str(self.silverScore), 1060, 380,
                                 arcade.color.BLACK, 13.5)

                arcade.draw_text("Silver-Bird Score: ", 900, 380,
                                 arcade.color.BLACK, 13.5)

            # Draw Grid (Horizontal and Vertical Lines)
            for x in range(0, 600, 60):
                arcade.draw_line(x, 0, x, 600, arcade.color.SEA_BLUE, 2)

            for y in range(0, 600, 60):
                arcade.draw_line(0, y, 600, y, arcade.color.SEA_BLUE, 2)

            # Synchronize grid with frontend
            row1 = 540
            col2 = 60  # grid box size
            row2 = 60
            for R in range(10):
                col1 = 0  # change position
                for C in range(10):
                    if self.grid[R][C] == 1:
                        arcade.draw_lrwh_rectangle_textured(
                            col1, row1, col2, row2, silverPlayer)
                    elif self.grid[R][C] == 2:
                        arcade.draw_lrwh_rectangle_textured(
                            col1, row1, col2, row2, redPlayer)
                    elif self.grid[R][C] == 11:
                        arcade.draw_lrwh_rectangle_textured(
                            col1+5, row1+5, col2-10, row2-10, silverSplash)
                    elif self.grid[R][C] == 22:
                        arcade.draw_lrwh_rectangle_textured(
                            col1+5, row1+5, col2-10, row2-10, redSplash)
                    col1 = col1+60
                row1 = row1-60

        elif self.state == "GameEnd":
            # arcade.draw_rectangle_filled(550, 600, 400,
            #  300, arcade.color.LIGHT_GRAY)

            arcade.draw_text("Status  ", 480, 515,
                             arcade.color.WHITE, 35)

            arcade.draw_text("Close And Start Again The Game  ", 430, 410,
                             arcade.color.BLACK_BEAN, 15)

            if self.win == 'botWin':
                arcade.draw_text("Alas!! Bot Won  ", 410, 450,
                                 arcade.color.WHITE, 35)
            if self.win == 'matchDraw':
                arcade.draw_text("Game Draw!!  ", 410, 450,
                                 arcade.color.WHITE, 35)
            if self.win == 'humanWin':
                arcade.draw_text("Congrats! You Won The Game  ", 320, 450,
                                 arcade.color.WHITE, 35)

    # Finding Box Size
    def boxSize(self, x, y):
        col1 = y // 60
        row1 = x // 60
        return 9-col1, row1

    # Check Move Is Legal
    def isLegalMove(self, currRow, currCol, turn):
        # check player Turn
        if turn == 1:
            row, col = self.silverPlayerPosition[0], self.silverPlayerPosition[1]
        else:
            row, col = self.redPlayerPosition[0], self.redPlayerPosition[1]
        # Check out the movement is valid or not
        if currRow == row+1 and currCol == col:
            return 1, "down"
        elif currRow == row-1 and currCol == col:
            return 1, "up"
        elif currRow == row and currCol == col+1:
            return 1, "right"
        elif currRow == row and currCol == col-1:
            return 1, "left"
        else:
            return 0, False

    # check out the score by evaluating the grid
    def evaluateScore(self, b):
        # redScore = 0
        # silverScore = 0
        # for row in range(len(b)):
        #     for col in range(len(b[row])):
        #         if b[row][col] == 0:
        #             continue
        #         elif b[row][col] == 2 or b[row][col] == 22:
        #             redScore += 1
        #         elif b[row][col] == 1 or b[row][col] == 11:
        #             silverScore += 1

        # if silverScore == redScore:
        #     return 50
        # elif silverScore > redScore:
        #     return 200
        # elif redScore > silverScore:
        #     return 100
        for row in range(len(b)):
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == 2) or (b[row][0] == 22):
                    return 100
                elif (b[row][0] == 1) or (b[row][0] == 11):
                    return 200

        for col in range(len(b)):
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
                if (b[0][col] == 2) or (b[0][col] == 22):
                    return 100
                elif (b[0][col] == 1) or (b[0][col] == 11):
                    return 200

        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
            if (b[0][0] == 2) or (b[0][0] == 22):
                return 100
            elif (b[0][0] == 1) or (b[0][0] == 11):
                return 200

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

            if (b[0][2] == 2) or (b[0][2] == 22):
                return 100
            elif (b[0][2] == 1) or (b[0][2] == 11):
                return 200
        # Else if none of them have won then return 50 draw
        return 50
#_______________________________________________________________________________________________________________________________________________#
    # Slippery Functions
    def leftMove(self, turn):
        if turn == 1:
            x, y = self.silverPlayerPosition[0], self.silverPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 22 or self.grid[x][y] == 2:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y+1] = 1
                    self.silverPlayerPosition = x, y+1
                    self.turn = "Red_Player"
                    break
                elif y == 0:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y] = 1
                    self.silverPlayerPosition = x, y
                    self.turn = "Red_Player"
                    break
                else:
                    y = y-1
        else:
            x, y = self.redPlayerPosition[0], self.redPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 11 or self.grid[x][y] == 1:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y+1] = 2
                    self.redPlayerPosition = x, y+1
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                elif y == 0:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y] = 2
                    self.redPlayerPosition = x, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                else:
                    self.turnsCount += 1
                    y = y-1
#_______________________________________________________________________________________________________________________________________________#
    def rightMove(self, turn):
        if turn == 1:
            x, y = self.silverPlayerPosition[0], self.silverPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 22 or self.grid[x][y] == 2:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y-1] = 1
                    self.silverPlayerPosition = x, y-1
                    self.turn = "Red_Player"
                    break
                elif y == 9:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y] = 1
                    self.silverPlayerPosition = x, y
                    self.turn = "Red_Player"
                    break
                else:
                    y = y+1
        else:
            x, y = self.redPlayerPosition[0], self.redPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 11 or self.grid[x][y] == 1:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y-1] = 2
                    self.redPlayerPosition = x, y-1
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                elif y == 9:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y] = 2
                    self.redPlayerPosition = x, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                else:
                    y = y+1
#_______________________________________________________________________________________________________________________________________________#
    def upwardMove(self, turn):
        if turn == 1:
            x, y = self.silverPlayerPosition[0], self.silverPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 22 or self.grid[x][y] == 2:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x+1][y] = 1
                    self.silverPlayerPosition = x+1, y
                    self.turn = "Red_Player"
                    break
                elif x == 0:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y] = 1
                    self.silverPlayerPosition = x, y
                    self.turn = "Red_Player"
                    break
                else:
                    x = x-1
        else:
            x, y = self.redPlayerPosition[0], self.redPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 11 or self.grid[x][y] == 1:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x+1][y] = 2
                    self.redPlayerPosition = x+1, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                elif x == 0:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y] = 2
                    self.redPlayerPosition = x, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                else:
                    x = x-1
#_______________________________________________________________________________________________________________________________________________#
    def downwardMove(self, turn):
        if turn == 1:
            x, y = self.silverPlayerPosition[0], self.silverPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 22 or self.grid[x][y] == 2:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x-1][y] = 1
                    self.silverPlayerPosition = x-1, y
                    self.turn = "Red_Player"
                    break
                elif x == 9:
                    self.grid[self.silverPlayerPosition[0]
                              ][self.silverPlayerPosition[1]] = 11
                    self.grid[x][y] = 1
                    self.silverPlayerPosition = x, y
                    self.turn = "Red_Player"
                    break
                else:
                    x = x+1
        else:
            x, y = self.redPlayerPosition[0], self.redPlayerPosition[1]
            while(True):
                if self.grid[x][y] == 0 or self.grid[x][y] == 11 or self.grid[x][y] == 1:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x-1][y] = 2
                    self.redPlayerPosition = x-1, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                elif x == 9:
                    self.grid[self.redPlayerPosition[0]
                              ][self.redPlayerPosition[1]] = 22
                    self.grid[x][y] = 2
                    self.redPlayerPosition = x, y
                    self.turn = "Silver_Player"
                    self.botMovement()
                    break
                else:
                    x = x+1

    def on_key_press(self, key, modifiers):
        if self.state == "InstructionMenu":
            if key == arcade.key.SPACE:
                self.state = "GameOn"
#_______________________________________________________________________________________________________________________________________________#
    # heuristic Technique function for heuristic
    def heuristicTechnique(self, row, col, position):
        winChances = 0
        for i in range(10):
            for j in range(10):
                if self.grid[i][j] == 11:
                    winChances = winChances + 1
        # Check out the left side in the grid
        if position == "left":
            if col-1 >= 0:
                if self.grid[row][col-1] == 22 or self.grid[row][col-1] == 2:
                    return -1
            if row == 9 or col == 0 or row == 0 or col == 9:
                if col-1 < 0:
                    return -1
            else:
                winChances = winChances
            for i in range(10):
                col = col - 1
                if col > 9 or col < 0:
                    return winChances
                if self.grid[row][col] == 22 or self.grid[row][col] == 2:
                    return winChances
                elif self.grid[row][col] == 11:
                    continue
                elif self.grid[row][col] == 0 and self.grid[row][col+1] != 11:
                    winChances = winChances + 2
                elif self.grid[row][col] == 0 and self.grid[row][col+1] == 11:
                    winChances = winChances + 0.1
                else:
                    return winChances
         # Check out the right side in the grid
        elif position == "right":
            if col+1 <= 9:
                if self.grid[row][col+1] == 22 or self.grid[row][col+1] == 2:
                    return -1
            if row == 9 or col == 0 or row == 0 or col == 9:
                if col+1 > 9:
                    return -1
            else:
                winChances = winChances
            for i in range(10):
                col = col + 1
                if col > 9 or col < 0:
                    return winChances
                if self.grid[row][col] == 22 or self.grid[row][col] == 2:
                    return winChances
                elif self.grid[row][col] == 11:
                    continue
                elif self.grid[row][col] == 0 and self.grid[row][col-1] != 11:
                    winChances = winChances + 2
                elif self.grid[row][col] == 0 and self.grid[row][col-1] == 11:
                    winChances = winChances + 0.1
                else:
                    return winChances
         # Check out the upward side in the grid
        elif position == "up":
            if row-1 >= 0:
                if self.grid[row-1][col] == 22 or self.grid[row-1][col] == 2:
                    return -1
            if row == 9 or col == 0 or row == 0 or col == 9:
                if row-1 < 0:
                    return -1
            else:
                winChances = winChances
            for i in range(10):
                row = row - 1
                if row > 9 or row < 0:
                    return winChances
                if self.grid[row][col] == 22 or self.grid[row][col] == 2:
                    return winChances
                elif self.grid[row][col] == 11:
                    continue
                elif self.grid[row][col] == 0 and self.grid[row+1][col] != 11:
                    winChances = winChances + 2
                elif self.grid[row][col] == 0 and self.grid[row+1][col] == 11:
                    winChances = winChances + 0.1
                else:
                    return winChances
         # Check out the downward side in the grid
        elif position == "down":
            if row+1 <= 9:
                if self.grid[row+1][col] == 22 or self.grid[row+1][col] == 2:
                    return -1
            if row == 9 or col == 0 or row == 0 or col == 9:
                if row+1 > 9:
                    return -1
            else:
                winChances = winChances
            for i in range(10):
                row = row + 1
                if row > 9 or row < 0:
                    return winChances
                if self.grid[row][col] == 22 or self.grid[row][col] == 2:
                    return winChances
                elif self.grid[row][col] == 11:
                    continue
                elif self.grid[row][col] == 0 and self.grid[row-1][col] != 11:
                    winChances = winChances + 2
                elif self.grid[row][col] == 0 and self.grid[row-1][col] == 11:
                    winChances = winChances + 0.1
                else:
                    return winChances
#_______________________________________________________________________________________________________________________________________________#
    def checkZeros(self, board):
        for i in range(10):
            for j in range(10):
                if board[i][j] == 0:
                    return True
        return False
#_______________________________________________________________________________________________________________________________________________#
    def minimax(self, board, depth, isMax, Pos):
        score = self.evaluateScore(board)
        if score == 100 or score == 200 or score == 50 or depth == 7:
            # print(score + self.heuristicTechnique(self.silverPlayerPosition[0],self.silverPlayerPosition[1],Pos),'\n')
            return score + self.heuristicTechnique(self.silverPlayerPosition[0], self.silverPlayerPosition[1], Pos)
        # If there are no more moves and no winner then
        # it is a tie
        if self.checkZeros(board) == False:
            return 0
        # If this maximizer's move
        if (isMax):
            best = -1000
            # Traverse all cells
            # print(board, '\n')
            for i in range(len(board)):
                for j in range(len(board)):

                    # Check if cell is empty
                    if (board[i][j] == 0):
                        # Make the move
                        board[i][j] = 2
                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, self.minimax(board,
                                                      depth + 1,
                                                      not isMax, Pos))
                        # Undo the move
                        board[i][j] = 0
            return best
        # If this minimizer's move
        else:
            best = 1000
            # print(board)
            # Traverse all cells
            for i in range(len(board)):
                for j in range(len(board)):
                    # Check if cell is empty
                    if (board[i][j] == 0):
                        # Make the move
                        board[i][j] = 1
                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self.minimax(
                            board, depth + 1, not isMax, Pos))
                        # Undo the move
                        board[i][j] = 0
            return best
#_______________________________________________________________________________________________________________________________________________#
    def findBestMove(self):
        #Keep Record Of Moves
        winningChances = []
        # find optimal left side movement
        left_score = self.minimax(self.grid, 0, False, "left")
        winningChances.append([left_score, "left"])
        # find optimal right side movement
        right_score = self.minimax(self.grid, 0, False, "right")
        winningChances.append([right_score, "right"])
        # find optimal upward movement
        up_score = self.minimax(self.grid, 0, False, "up")
        winningChances.append([up_score, "up"])
        # find optimal downward movement
        down_score = self.minimax(self.grid, 0, False, "down")
        winningChances.append([down_score, "down"])
        # Find the best among the above movement
        sorted_winningChances = sorted(
            winningChances,  reverse=True)
        # If not finding path return False
        print('Value Of Best Move and Its Direction Is: ',winningChances[0],'\n')
        if sorted_winningChances[0][1] == -1:
            self.turnsCount += 1
            return False
        else:
            # print(winningChances)
            return sorted_winningChances[0][1]
#_______________________________________________________________________________________________________________________________________________#
    # Function to move Bot
    def botMovement(self):
        self.turn = "Silver_Player"
        row = self.silverPlayerPosition[0]
        col = self.silverPlayerPosition[1]
        best_move = self.findBestMove()
        if best_move == False:
            self.turn = "Red_Player"
        elif best_move == "left":
            if self.grid[row][col-1] == 11:
                self.leftMove(1)
            else:
                self.grid[self.silverPlayerPosition[0]
                          ][self.silverPlayerPosition[1]] = 11
                self.silverPlayerPosition = row, col-1
                self.grid[row][col-1] = 1
                self.silverScore += 1
                self.turn = "Red_Player"
                if self.silverScore >= 50:
                    if self.silverScore == 50 and self.redScore == 50:
                        self.win = "matchDraw"
                        self.state = "GameEnd"
                    self.state = "GameEnd"
                    self.win = "botWin"
        elif best_move == "right":
            if self.grid[row][col+1] == 11:
                self.rightMove(1)
            else:
                self.grid[self.silverPlayerPosition[0]
                          ][self.silverPlayerPosition[1]] = 11
                self.silverPlayerPosition = row, col+1
                self.grid[row][col+1] = 1
                self.silverScore += 1
                self.turn = "Red_Player"
                if self.silverScore >= 50:
                    if self.silverScore == 50 and self.redScore == 50:
                        self.win = "matchDraw"
                        self.state = "GameEnd"
                    self.state = "GameEnd"
                    self.win = "botWin"
        elif best_move == "up":
            if self.grid[row-1][col] == 11:
                self.upwardMove(1)
            else:
                self.grid[self.silverPlayerPosition[0]
                          ][self.silverPlayerPosition[1]] = 11
                self.silverPlayerPosition = row-1, col
                self.grid[row-1][col] = 1
                self.silverScore += 1
                self.turn = "Red_Player"
                if self.silverScore >= 50:
                    if self.silverScore == 50 and self.redScore == 50:
                        self.win = "matchDraw"
                        self.state = "GameEnd"
                    self.state = "GameEnd"
                    self.win = "botWin"
        elif best_move == "down":
            if self.grid[row+1][col] == 11:
                self.downwardMove(1)
            else:
                self.grid[self.silverPlayerPosition[0]
                          ][self.silverPlayerPosition[1]] = 11
                self.silverPlayerPosition = row+1, col
                self.grid[row+1][col] = 1
                self.silverScore += 1
                self.turn = "Red_Player"
                if self.silverScore >= 50:
                    if self.silverScore == 50 and self.redScore == 50:
                        self.win = "matchDraw"
                        self.state = "GameEnd"
                    self.state = "GameEnd"
                    self.win = "botWin"
        else:
            if self.silverScore >= 50:
                if self.silverScore == 50 and self.redScore == 50:
                    self.win = "matchDraw"
                    self.state = "GameEnd"
                self.state = "GameEnd"
                self.win = "botWin"
#_______________________________________________________________________________________________________________________________________________#
    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            # redPlayer turn
            if self.turn == "Red_Player":
                row, col = self.boxSize(x, y)
                check, status = self.isLegalMove(row, col, 2)
                if check == 1:
                    if self.grid[row][col] == 22:
                        if status == "left":
                            self.leftMove(2)
                        elif status == "right":
                            self.rightMove(2)
                        elif status == "up":
                            self.upwardMove(2)
                        elif status == "down":
                            self.downwardMove(2)
                    elif self.grid[row][col] == 0:
                        self.grid[self.redPlayerPosition[0]
                                  ][self.redPlayerPosition[1]] = 22
                        self.redPlayerPosition = row, col
                        self.grid[row][col] = 2
                        self.redScore += 1
                        self.botMovement()
                        if self.redScore >= 50:
                            if self.silverScore == 50 and self.redScore == 50:
                                self.win = "matchDraw"
                                self.state = "GameEnd"
                            self.state = "GameEnd"
                            self.win = "humanWin"
                    else:
                        self.botMovement()
                else:
                    self.botMovement()
        if self.turnsCount >= 7:
            if self.silverScore == 50 and self.redScore == 50:
                self.win = "matchDraw"
                self.state = "GameEnd"
            elif self.silverScore >= 50:
                self.win = "botWin"
                self.state = "GameEnd"
            else:
                self.win = "humanWin"
                self.state = "GameEnd"

        #Print The Current Grid
        print("Game in Continued State")
        print(self.grid, '\n')
#_______________________________________________________________________________________________________________________________________________#
# Main Function
def main():
    window = arcade.Window(Width, Length, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
if __name__ == "__main__":
    main()
