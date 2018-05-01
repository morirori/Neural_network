from utils.Tags import LayersTags
from abstracts.AbstractUpdatingWeightsStrategy import AbstractUpdatingWeightsStrategy


class MLPNUpdatingWeightsStrategy(AbstractUpdatingWeightsStrategy):

    def update(self, layer, activation_fun,learning_factor):

        if layer.tag != LayersTags.OUTPUT_LAYER:
            for neuron in layer.neuron_vector:
                neuron.calculate_delta(activation_fun=activation_fun)
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)
        else:
            for neuron in layer.neuron_vector:
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)


class SOMUpdatingWeightsStrategy(AbstractUpdatingWeightsStrategy):

    def update(self, layer, activation_fun, beta):
        #TODO updating weights strategy
        pass


class UpdatingWeightsStrategyContext:

    def __init__(self, layer_tag):
        if layer_tag == LayersTags.SOM:
            pass
        else:
            self.strategy = MLPNUpdatingWeightsStrategy()

