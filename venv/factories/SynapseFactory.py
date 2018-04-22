from model.Synapse import Synapse
from numpy.random import random
import random
class SynapseFactory:
    @staticmethod
    def create(input_neuron,output_neuron):
        synapse = Synapse()
        weight=random.uniform(-5,5)
        synapse.add_connection(input_neuron,weight,output_neuron)
        return synapse

    @staticmethod
    def create_bias(bias,neuron):
        synapse = Synapse()
        weight=random.uniform(-5,5)
        synapse.add_connection(bias,weight,neuron)
        return synapse
