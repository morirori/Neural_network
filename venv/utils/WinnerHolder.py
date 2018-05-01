class WinnerHolder():

    winner = None

    @staticmethod
    def set_winner(neuron):
        WinnerHolder.winner=neuron

    @staticmethod
    def get_winner():
        return WinnerHolder.winner