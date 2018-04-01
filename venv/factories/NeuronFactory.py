from model.Neuron import Neuron

class NeuronFactory:
    @staticmethod
    def create(layer_id,id):
        neuron=Neuron(layer_id,id)
        return neuron
