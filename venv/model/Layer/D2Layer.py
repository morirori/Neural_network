from factories.SynapseFactory import SynapseFactory
from utils.Tags import LayersTags
from utils.Strategies.UpdatingStrategyContext import UpdatingStrategyContext
from utils.Strategies.UpdatingWeightsStrategyContext import UpdatingWeightsStrategyContext
from abstracts.AbstractLayer import AbstractLayer


class D2Layer(AbstractLayer):

    def __init__(self, neuron_vector, id):
        self.__neuron_vector=neuron_vector
        self.__tag=""
        self.__id=id
        self.bias=""

    def print(self):
        print("TAG: {}  layer_id: {} bias {}".format(self.tag, self.id, self.bias))
        for neuron in self.__neuron_vector:
            print(neuron)

    @property
    def neuron_vector(self):
        return self.__neuron_vector

    @property
    def tag(self):
        return self.__tag

    @property
    def id(self):
        return self.__id

    def update_weights(self):
        pass

    def update(self):
        pass
