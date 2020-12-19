import numpy as np

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0 # The amount of prize money for this player
        self.prizes = [] # The prizes this player has won so far

    def addMoney(self, amt):
        """
        Add amt to self.prizeMoney
        :param amt:
        :return:
        """
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)


class WOFHumanPlayer(WOFPlayer):

    def __init__(self, name):
        WOFPlayer.__init__(self, name)

    def getMove(self, category, obscured_phrase, guessed):
        """
        Ask the user to enter a move
        :param obscuredPhrase:
        :param guessed:
        :return:
        """

        print(
            """
            {} has ${}

            Category: {}
            Phrase:  {}
            Guessed: {}

            Guess a letter, phrase, or type 'exit' or 'pass':
            """.format(self.name, self.prizeMoney, category, obscured_phrase, guessed)
        )

        user_input = input()

        try:
            user_input = str(user_input.lower())  # try casting to an str
            if user_input == 'exit':
                # exit game
                return
            elif user_input == 'pass':
                return 'pass'
            elif len(user_input) == 1:
                # A single character to guess that letter
                return user_input
            else:
                # A complete phrase (a multi-character phrase other than 'exit' or 'pass')
                return user_input

        except Exception:
            print('input cannot be casted as string')


class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE' # class variable

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty # extra Instance variable

    @property
    def smartCoinFlip(self):
        """
        Decide semi-randomly whether to make a “good” or “bad” move
        :return:
        """
        if np.random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):

