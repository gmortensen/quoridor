# Author: Gabriel Mortensen
# Date: 8/12/2021
# Description: Final portfolio project for CS162. Class that allows two people to play the game Quoridor where two
#              people take turns either moving their pawns or placing fences. First pawn to the other side of the board
#              wins!

class QuoridorGame:
    """
    Class that represents an instance of the game, Quoridor.
    """

    def __init__(self):
        """
        Creates instance of the game board, as wells as default starting data members.
        """
        #  I use a dictionary to represent my game board. The numeric keys represent the spaces a pawn is able to move
        #  to, and the values of these keys are a list containing spaces to place a pawn, denoted as "", or a space to
        #  place a vertical fence, denoted ".". The "." spaces are used to mark there is NOT a vertical fence separating
        #  two horizontal spaces. The F1, F2, etc keys represent the horizontal lines between the rows where horizontal
        #  fences can be placed. "----" means there is no fence yet, and "====" means it has now been fenced. Similarly,
        #  "||" represents that there is a vertical fence separating two spaces
        self._game_board = {
            "top edge": ["||", "====", "====", "====", "====", "====", "====", "====", "====", "====", "||"],
            0: ["||", "", ".", "", ".", "", ".", "", ".", "P1", ".", "", ".", "", ".", "", ".", "", "||"],
            "F1": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            1: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F2": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            2: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F3": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            3: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F4": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            4: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F5": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            5: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F6": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            6: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F7": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            7: ["||", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", ".", "", "||"],
            "F8": ["||", "----", "----", "----", "----", "----", "----", "----", "----", "----", "||"],
            8: ["||", "", ".", "", ".", "", ".", "", ".", "P2", ".", "", ".", "", ".", "", ".", "", "||"],
            "bottom edge": ["||", "====", "====", "====", "====", "====", "====", "====", "====", "====", "||"], }

        self._turn_count = 1
        self._p1_token = "P1"
        self._p2_token = "P2"
        self._game_won = False
        self._p1_location = (4, 0)
        self._p2_location = (4, 8)
        self._p1_fences = 10
        self._p2_fences = 10
        self._h_fence_dict = {
            0: self._game_board["top edge"],
            1: self._game_board["F1"],  # This dictionary allows me to easily convert the target space
            2: self._game_board["F2"],  # entered for a horizontal fence to the proper place on the
            3: self._game_board["F3"],  # on the game board. It makes navigating the game board easier
            4: self._game_board["F4"],
            5: self._game_board["F5"],
            6: self._game_board["F6"],
            7: self._game_board["F7"],
            8: self._game_board["F8"],
            9: self._game_board["bottom edge"], }

    # ------------------------------------------------------------------------------------------------------------------
    #                                             Getter/Setter Methods
    def get_turn_count(self):
        """
        Returns the current turn of the game. Odd numbers mean it is P1's turn, even numbers mean it's P2's turn
        """
        return self._turn_count

    def get_game_won(self):
        """
        Method used to check if the private self._game_won variable is True or False
        """
        return self._game_won

    def set_game_won(self):
        """
        Sets the self._game_won variable to True
        """
        self._game_won = True

    def get_pawn_location(self):
        """
        Method to retrieve the current location of a pawn, returns a tuple of a pawn's current location
        """
        if self.get_turn_count() % 2 == 0:
            return self._p2_location
        else:
            return self._p1_location

    def set_pawn_location(self, target_location):
        """
        Method used to change a pawn's location to their targeted space, after it moves successfully
        """
        if self.get_turn_count() % 2 == 0:
            self._p2_location = target_location
        else:
            self._p1_location = target_location

    def get_fences_left(self, player_integer):
        """
        Method to check the number of fences each player has remaining
        """
        if player_integer == 1:
            return self._p1_fences
        elif player_integer == 2:
            return self._p2_fences
        else:
            return False

    def get_h_fence_dict(self):
        """
        Method to retrieve the dictionary used for horizontal fence placements
        """
        return self._h_fence_dict

    def get_game_board(self):
        """
        Method to retrieve the private self._game_board data member
        """
        return self._game_board

    def get_pawn(self, player_integer):
        """
        Gets the token representing the player's pawn on the board
        """
        if player_integer == 1:
            return self._p1_token
        else:
            return self._p2_token

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Utility Methods
    def increment_turn(self):
        """
        Method to increment the turn total to help keep track of whose turn it is
        """
        self._turn_count += 1

    def display_board(self):
        """
        Displays the current game board with current pawn and fence locations
        """
        for key in self._game_board:
            print(self._game_board[key])

    def turn_check(self, player_integer):
        """
        Method to check it is the turn of the player trying to make a move, returns false if it is not their turn
        """
        if player_integer == 1 and self.get_turn_count() % 2 == 0:
            return False
        if player_integer == 2 and self.get_turn_count() % 2 != 0:
            return False
        else:
            return

    @staticmethod
    def board_edges(target_location):
        """
        Checks to make sure a player isn't targeting a position off of the board's edges, returns false if the target
        location is off the edges of the game board
        """
        if target_location[0] < 0 or target_location[0] > 8:
            return False
        if target_location[1] < 0 or target_location[1] > 8:
            return False
        else:
            return

    def condition_check(self, player_integer, target_location):
        """
        Method that checks various conditions that would invalidate a player move. Checks to make sure it is the players
        turn, makes sure a player hasn't already won, makes sure the target space is on the board, and makes sure the
        targeted space does not already have another player's pawn
        """
        game_board = self.get_game_board()
        if self.turn_check(player_integer) is False:
            return False
        if self._game_won is True:
            return False
        if self.board_edges(target_location) is False:
            return False
        if game_board[target_location[1]][(target_location[0] * 2) + 1] != "":
            return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Move Methods
    def move_pawn(self, player_integer, target_location):
        """
        Method that moves a pawn to a selected space if it is a legal move. Calls other methods depending on the
        direction the pawn is trying to move
        """
        current_location = self.get_pawn_location()
        if self.condition_check(player_integer, target_location) is False:
            return False
        else:
            if self.is_legal_move(player_integer, target_location, current_location) is True:
                return True
            else:
                return False

    def is_legal_move(self, player_integer, target_location, current_location):  # Will add diagonal checks later
        """
        Checks to see if a desired move is legal, and determines if the pawn is making a normal move or a special move
        like moving diagonally or jumping another pawn
        """
        #  Diagonal Move
        if abs(current_location[0] - target_location[0]) == 1 and abs(current_location[1] - target_location[1]) == 1:
            if self.diagonal_move(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        #  Jumping Move
        elif abs(current_location[0] - target_location[0]) == 0 and abs(current_location[1] - target_location[1]) == 2:
            if self.jump_move(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        #  Horizontal Moves
        elif abs(current_location[0] - target_location[0]) == 1 and abs(current_location[1] - target_location[1]) == 0:
            if self.horizontal_move(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        #  Vertical Moves
        elif abs(current_location[0] - target_location[0]) == 0 and abs(current_location[1] - target_location[1]) == 1:
            if self.vertical_move(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Vertical Moves

    def vertical_move(self, player_integer, target_location, current_location):
        """
        Method that will be called to move a pawn in vertical directions
        """
        if target_location[1] > current_location[1]:  # Moving down the board
            if self.move_down(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        else:  # Moving up the board
            if self.move_up(player_integer, target_location, current_location) is True:
                return True
            else:
                return False

    def move_down(self, player_integer, target_location, current_location):
        """
        Method used to move a piece down the board as long as there is not a horizontal fence blocking their path
        """
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if h_fence_dict[current_location[1] + 1][current_location[0] + 1] == "----":
            game_board[target_location[1]][(target_location[0] * 2) + 1] = self.get_pawn(player_integer)
            game_board[current_location[1]][(target_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    def move_up(self, player_integer, target_location, current_location):
        """
        Method used to move a piece up the board as long as there is not a horizontal fence blocking their path
        """
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if h_fence_dict[current_location[1]][current_location[0] + 1] == "----":
            game_board[target_location[1]][(target_location[0] * 2) + 1] = self.get_pawn(player_integer)
            game_board[current_location[1]][(target_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Horizontal Moves

    def horizontal_move(self, player_integer, target_location, current_location):
        """
        Method that will be called to move a pawn in horizontal directions
        """
        if target_location[0] > current_location[0]:  # Moving to the right side of the board
            if self.move_right(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        else:                                         # Moving to the left side of the board
            if self.move_left(player_integer, target_location, current_location) is True:
                return True
            else:
                return False

    def move_right(self, player_integer, target_location, current_location):
        """
        Moves the pawn to the right of the board as long as there is not a vertical fence blocking their path
        """
        game_board = self.get_game_board()
        if game_board[current_location[1]][(current_location[0] * 2) + 2] == ".":
            game_board[current_location[1]][(current_location[0] * 2) + 3] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    def move_left(self, player_integer, target_location, current_location):
        """
        Moves the pawn to the left of the board as long as there is not a vertical fence blocking their path
        """
        game_board = self.get_game_board()
        if game_board[current_location[1]][(current_location[0] * 2)] == ".":
            game_board[current_location[1]][(current_location[0] * 2) - 1] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Diagonal Moves

    def diagonal_move(self, player_integer, target_location, current_location):
        """
        Method that will be used to make the special diagonal move when a pawn is blocked vertically by a fence and
        another pawn
        """
        if target_location[1] > current_location[1]:  # Upwards diagonal moves
            if self.diagonal_down(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        else:                                         # Downwards diagonal moves
            if self.diagonal_up(player_integer, target_location, current_location) is True:
                return True
            else:
                return False

    def diagonal_up(self, player_integer, target_location, current_location):
        """
        Moves the pawn up the board diagonally if there is a pawn and fence blocking their path upwards
        """
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if game_board[current_location[1] - 1][(current_location[0] * 2) + 1] != "" and \
                h_fence_dict[current_location[1] - 1][current_location[0] + 1] != "----":
            if target_location[0] > current_location[0]:
                if self.up_right(player_integer, target_location, current_location) is True:
                    return True
                else:
                    return False
            else:
                if self.up_left(player_integer, target_location, current_location) is True:
                    return True
                else:
                    return False

    def diagonal_down(self, player_integer, target_location, current_location):
        """
        Moves the pawn down the board diagonally if there is a pawn and fence blocking their path downwards
        """
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if game_board[current_location[1] + 1][(current_location[0] * 2) + 1] != "" and \
                h_fence_dict[current_location[1] + 2][current_location[0] + 1] != "----":
            if target_location[0] > current_location[0]:
                if self.down_right(player_integer, target_location, current_location) is True:
                    return True
                else:
                    return False
            else:
                if self.down_left(player_integer, target_location, current_location) is True:
                    return True
                else:
                    return False
        else:
            return False

    def down_left(self, player_integer, target_location, current_location):
        """Moves the pawn down one row, and left one space"""
        game_board = self.get_game_board()
        if game_board[current_location[1] + 1][(current_location[0] * 2) - 1] == "":
            game_board[current_location[1] + 1][(current_location[0] * 2) - 1] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    def down_right(self, player_integer, target_location, current_location):
        """Moves the pawn down one row, and right one space"""
        game_board = self.get_game_board()
        if game_board[current_location[1] + 1][(current_location[0] * 2) + 3] == "":
            game_board[current_location[1] + 1][(current_location[0] * 2) + 3] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    def up_left(self, player_integer, target_location, current_location):
        """Moves the pawn up one row, and left one space"""
        game_board = self.get_game_board()
        if game_board[current_location[1] - 1][(current_location[0] * 2) - 1] == "":
            game_board[current_location[1] - 1][(current_location[0] * 2) - 1] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    def up_right(self, player_integer, target_location, current_location):
        """Moves the pawn down up row, and right one space"""
        game_board = self.get_game_board()
        if game_board[current_location[1] - 1][(current_location[0] * 2) + 3] == "":
            game_board[current_location[1] - 1][(current_location[0] * 2) + 3] = self.get_pawn(player_integer)
            game_board[current_location[1]][(current_location[0] * 2) + 1] = ""
            self.set_pawn_location(target_location)
            self.is_winner(player_integer)
            self.increment_turn()
            return True
        else:
            return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Jump Moves

    def jump_move(self, player_integer, target_location, current_location):
        """
        Method for the special jump move when one pawn is blocked vertically by another
        """
        if target_location[1] > current_location[1]:
            if self.jump_down(player_integer, target_location, current_location) is True:
                return True
            else:
                return False
        else:
            if self.jump_up(player_integer, target_location, current_location) is True:
                return True
            else:
                return False

    def jump_down(self, player_integer, target_location, current_location):
        """Allows the pawn to jump down over another pawn, to two rows down"""
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if game_board[current_location[1] + 1][(current_location[0] * 2) + 1] != "":
            if h_fence_dict[current_location[1] + 2][current_location[0] + 1] == "----" and \
                    h_fence_dict[current_location[1] + 1][current_location[0] + 1] == "----":
                game_board[target_location[1]][(target_location[0] * 2) + 1] = self.get_pawn(player_integer)
                game_board[current_location[1]][(target_location[0] * 2) + 1] = ""
                self.set_pawn_location(target_location)
                self.is_winner(player_integer)
                self.increment_turn()
                return True
            else:
                return False

    def jump_up(self, player_integer, target_location, current_location):
        """Allows the pawn to jump up over another pawn, to two rows up"""
        game_board = self.get_game_board()
        h_fence_dict = self.get_h_fence_dict()
        if game_board[current_location[1] - 1][(current_location[0] * 2) + 1] != "":
            if h_fence_dict[current_location[1]][current_location[0] + 1] == "----" and \
                    h_fence_dict[current_location[1] - 1][current_location[0] + 1] == "----":
                game_board[target_location[1]][(target_location[0] * 2) + 1] = self.get_pawn(player_integer)
                game_board[current_location[1]][(target_location[0] * 2) + 1] = ""
                self.set_pawn_location(target_location)
                self.is_winner(player_integer)
                self.increment_turn()
                return True
            else:
                return False

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Fence Methods

    def fences_left(self, player_integer):
        """
        Checks if a player still has fences remaining. Returns false if they are out of fences
        """
        if self.get_fences_left(player_integer) < 1:
            return False
        else:
            return

    def decrement_fence(self, player_integer):
        """
        Reduces a player's fence total by one after they place a fence on their turn
        """
        if player_integer == 1:
            self._p1_fences -= 1
        else:
            self._p2_fences -= 1

    def already_fenced(self, v_or_h, target_location):
        """
        Method that checks if an entered fence target space is already occupied by another fence
        """
        if v_or_h.lower() == "h":
            target_column = target_location[0] + 1
            target_row = target_location[1]
            if self._h_fence_dict[target_row][target_column] != "----":
                return True
            else:
                return
        elif v_or_h.lower() == "v":
            target_column = (target_location[0] * 2)
            target_row = target_location[1]
            if self._game_board[target_row][target_column] != ".":
                return True
            else:
                return

    def place_fence(self, player_integer, v_or_h, target_location):
        """
        Method to place a fence at a targeted location if it passes the condition checks
        """
        if self.condition_check(player_integer, target_location) is False:
            return False
        if self.fences_left(player_integer) is False:
            return False
        if self.already_fenced(v_or_h, target_location) is True:
            return False
        else:
            if v_or_h.lower() == "v":
                self.vertical_fence(target_location)
                self.decrement_fence(player_integer)
                self.increment_turn()
                return True
            else:
                self.horizontal_fence(target_location)
                self.decrement_fence(player_integer)
                self.increment_turn()
                return True

    def horizontal_fence(self, target_location):
        """
        Method for placing a horizontal fence
        """
        target_column = target_location[0] + 1
        target_row = target_location[1]
        self._h_fence_dict[target_row][target_column] = "===="
        return

    def vertical_fence(self, target_location):
        """
        Method for placing a vertical fence
        """
        target_column = target_location[0]
        column_pos_in_dict = (target_column * 2)
        target_row = target_location[1]
        self._game_board[target_row][column_pos_in_dict] = "||"
        return

    # ------------------------------------------------------------------------------------------------------------------
    #                                               Check for Win Method

    def is_winner(self, player_integer):
        """
        Method to check if a player has moved their pawn to the other side of the board, and won the game. Is called by
        the move_pawn methods anytime a pawn moves successfully
        """
        if player_integer == 1:
            for value in self._game_board[8]:
                if value == "P1":
                    self.set_game_won()
                    return True
            return False
        elif player_integer == 2:
            for value in self._game_board[0]:
                if value == "P2":
                    self.set_game_won()
                    return True
            return False
        else:
            return False
