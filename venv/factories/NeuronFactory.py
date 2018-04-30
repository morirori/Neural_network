from model.MLPNeuron import MLPNeuron


class NeuronFactory():

    @staticmethod
    def create(layer_id,id):
        neuron=MLPNeuron(layer_id, id)
        return neuron
