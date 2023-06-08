#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Ethan Chang
# email: chang115@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Seoyeon Lee
# partner's email: leeseo@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ Constructor for a new Searcher object by initializing the 
            following attributes.
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def add_state(self, new_state):
        """ Takes a single State object called new_state and adds it to the
            Searcher's list of untested states.
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ Takes a State object called state and returns True if the called 
            Searcher should add state to its list of untested states, and 
            False otherwise.
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
        
    def add_states(self, new_states):
        """ Takes a list State objects called new_states, and processes the 
            elements of new_states one at a time.
        """
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)
                
    def next_state(self):
        """ Chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it.
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
            
    def find_solution(self, init_state):
        """ Performs a full state-space search that begins at the specified
            initial state init_state and ends when the goal state is found or
            when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.board.tiles == GOAL_TILES :
                return s
            else:
                x = s.generate_successors()
                self.add_states(x)
        return None
        
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ A class for searcher objects that perform breadth-first search instead
        of random search.
    """
    
    def next_state(self):
        """ Chooses the next state to be tested from the list of untested
            states, removing it from the list and returning it.
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """ A class for searcher objects that perform depth-first search instead
        of a random search.
    """    
    
    def next_state(self):
        """ Chooses the next state to be tested from the list of untested
            states, removing it from the list and returning it.
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ Takes a State object called state, and computes and returns an 
        estimate of how many additional moves are needed to get from state
        to the goal state.
    """
    return state.board.num_misplaced()

def h2(state):
    """ Takes a State object called state, and computes and returns an 
        estimate of how many additional moves are needed to get from state
        to the goal state.
    """
    return state.board.num_misplaced_row() + state.board.num_misplaced_col()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ Constructs a new GreedySearcher object.
        """
        super().__init__(-1)
        self.heuristic = heuristic
        
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ Computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher.
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ Adds a sublist that is a [priority, state] pair.
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ Chooses one of the states with the highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]
    
### Add your AStarSeacher class definition below. ###
class AStarSearcher(Searcher):
    """ Constructs a new AStarSearcher object.
    """
    
    def __init__(self, heuristic):
        """ Constructs a new AStarSearcher object.
        """
        super().__init__(-1)
        self.heuristic = heuristic
        
    def __repr__(self):
        """ returns a string representation of the AStarSearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
        
    def priority(self, state):
        """ Computes and returns the priority of the specified state, based
            on the heuristic function used by the searcher and the number of
            moves to the called state.
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    def add_state(self, state):
        """ Adds a sublist that is a [priority, state] pair.
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ Chooses one of the states with the highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]
