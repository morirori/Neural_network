from utils.Tags import LayersTags
from abstracts.AbstractUpdatingStrategy import AbstractUpdatingStrategy
from utils.WinnerHolder import WinnerHolder


class MLPNUpdatingStrategy(AbstractUpdatingStrategy):

    def update(self, layer, activation_fun, beta):
        for neuron in layer.neuron_vector:
            neuron.update(activation_fun, beta)


class SOMUpdatingStrategy(AbstractUpdatingStrategy):

    def update(self, layer, activation_fun, beta):
        for neuron in layer.neuron_vector:
            neuron.update(activation_fun, beta)
            if WinnerHolder.get_winner() is not None and neuron.output < WinnerHolder.get_winner().output:
                WinnerHolder.set_winner(neuron)

            elif WinnerHolder.get_winner() is None:
                WinnerHolder.set_winner(neuron)


class UpdatingStrategyContext():

    def __init__(self, layer_tag):
        if layer_tag == LayersTags.SOM:
            self.strategy = SOMUpdatingStrategy()
        elif layer_tag != LayersTags.SOM and layer_tag != LayersTags.INPUT_LAYER:
            self.strategy = MLPNUpdatingStrategy()
