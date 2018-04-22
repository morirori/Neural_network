from factories.NeuronFactory import NeuronFactory
from factories.BiasFactory import BiasFactory
from model.Layer import Layer

class LayerFactory:
    @staticmethod
    def create(layer_num,number_of_neuron):
        neuron_list=[]

        for i in range(number_of_neuron):
            neuron_list.append(NeuronFactory.create(layer_num,i))

        layer = Layer(neuron_list)
        return layer