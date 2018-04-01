from model.Synapse import Synapse
import random
class SynapseFactory:
    @staticmethod
    def create(neuron_list):
        synapse = Synapse()
        for neuron in neuron_list:
            weight=random.uniform(0,1)
            synapse.add_connection(neuron,weight)
        return  synapse
