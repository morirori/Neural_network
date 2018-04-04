from model.Neuron import  Neuron

class Synapse():

    def __init__(self):
        self.synapses=[]


    def add_connection(self,neuron,weight):
            temp_dict={}
            temp_dict["neuron"]=neuron
            temp_dict["weight"]=weight
            self.synapses.append(temp_dict)

    def update_neuron(self,index,neuron):
            self.synapses[index]["neuron"]=neuron


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

    def print(self):
        toReturn=""
        for x in self.synapses:
            toReturn+= "neuron id: {0} layer id:  {1} output{2} weight {3} ".format(str(x["neuron"].id), str(x["neuron"].layer_id),
                                                                                    str(x["neuron"].output), str(x["weight"]))

        return toReturn
