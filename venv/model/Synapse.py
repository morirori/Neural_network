from model.Neuron import  Neuron

class Synapse():

    def __init__(self):
        self.synapses=[]


    def add_neuron(self,neuron,weight):
            temp_dict={}
            temp_dict["neuron"]=neuron
            temp_dict["weight"]=weight
            self.synapses.append(temp_dict)

    def get_synapses_list(self):
        return self.synapses

    def get_raw_data(self):
        to_return=[]
        for synapse in self.synapses:
            if isinstance(synapse["neuron"],Neuron):
                to_return.append(synapse["neuron"].get_output())
            else:
                to_return.append(synapse["neuron"])

        return to_return

    def __str__(self):
        toReturn=""
        for x in self.synapses:
            toReturn+= str(x)+"  "

        return toReturn