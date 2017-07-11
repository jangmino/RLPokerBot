import numpy as np
from enum import Enum

class ActionType(Enum):
    Fold = 0
    Call = 1
    Raise = 2
    AllIn = 3

class Action:
    def __init__(self):
        self.actionType = ActionType.Fold
        self.actionSize = 0


class GameState:
    def __init__(self, maxPlayers=2, maxActions=4):
        """
        GameState
        """
        self.maxPlayers = maxPlayers
        self.maxActions = maxActions
        self.maxRounds = 4
        self.maxBoardCards = 5
        self.handID = 0
        self.maxSpent = 0
        self.minNoLimitRaiseTo = 0
        self.spent = np.zeros(maxPlayers)

        self.action = []
        self.actingPlayer = np.zeros((self.maxPlayers, self.maxActions), dtype=np.int32)
        self.numActions = np.zeros(self.maxRounds, dtype=np.int32)

        self.round = 0
        self.finished = False
        self.playerFolded = np.zeros(self.maxPlayers)

        self.boardCards = [] # string representation
        self.holeCards = [] # string representation


