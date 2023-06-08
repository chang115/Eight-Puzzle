#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Ethan Chang
# email: chang115@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Seoyeon Lee
# partner's email: leeseo@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
            

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ Takes a string direction as an input and modifies the contents
            of the called Board according to the specified direction. Returns
            True or False based on if the requested move is possible
        """
        temp_r = self.blank_r
        temp_c = self.blank_c
        blank = self.tiles[self.blank_r][self.blank_c]
        if direction == 'up':
            temp_r -= 1
            if temp_r > len(self.tiles) - 1 or temp_r < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[temp_r][temp_c]
                self.tiles[temp_r][temp_c] = blank
                self.blank_r = temp_r
                return True
        elif direction == 'down':
            temp_r += 1
            if temp_r > len(self.tiles) - 1 or temp_r < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[temp_r][temp_c]
                self.tiles[temp_r][temp_c] = blank
                self.blank_r = temp_r
                return True
        elif direction == 'left':
            temp_c -= 1
            if temp_c > len(self.tiles[0]) - 1 or temp_c < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[temp_r][temp_c]
                self.tiles[temp_r][temp_c] = blank
                self.blank_c = temp_c
                return True
        elif direction == 'right':
            temp_c += 1
            if temp_c > len(self.tiles[0]) - 1 or temp_c < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[temp_r][temp_c]
                self.tiles[temp_r][temp_c] = blank
                self.blank_c = temp_c
                return True
        else:
            return False
        
    def digit_string(self):
        """ Creates and returns a string of digits that corresponds to the 
            current contents of the called Board object's tiles attribute.
        """
        x = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                x += self.tiles[r][c]
        return x
    
    def copy(self):
        """ Returns a newly-constructed Board object that is a deep copy of
            the calleed object.
        """
        x = Board(self.digit_string())
        return x
    
    def num_misplaced(self):
        """ Counts and returns the number of tiles in the called Board object
            that are not where they should be in the goal state.
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    count += 1
        return count - 1
    
    def __eq__(self, other):
        """ Called when the == operator is used to compare two Board objects.
            Returns True if the called object and the argument have the same
            tiles attribute, and False otherwise.
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    def num_misplaced_row(self):
        """ Counts and returns the number of tiles in the called Board object
            that are not in the correct row compared to the goal state.
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if int(self.tiles[r][c]) // 3 != r:    
                    count += 1
        return count - 1 
    
    def num_misplaced_col(self):
        """ Counts and returns the number of tiles in the called Board object
            that are not in the correct column compared to the goal state.
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if int(self.tiles[r][c]) % 3 != c:    
                    count += 1
        return count - 1         
                
            
            
                