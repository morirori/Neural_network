from factories.SynapseFactory import SynapseFactory
from utils.Tags import LayersTags
from utils.Strategies.UpdatingStrategyContext import UpdatingStrategyContext
from utils.Strategies.UpdatingWeightsStrategyContext import UpdatingWeightsStrategyContext
from abstracts.AbstractLayer import AbstractLayer


class D1Layer(AbstractLayer):

    def __init__(self,neuron_vector,id):
        self.__neuron_vector=neuron_vector
        self.__tag=""
        self.__id=id
        self.bias=""

    def add_neuron(self,vector):
        self.neuron_vector.append(vector)

    def add_bias(self,bias):
        if self.tag == LayersTags.HIDDEN_LAYER:
            self.bias=bias

    def delete_forward_connections(self):
        for neuron in self.neuron_vector:
            neuron.output_synapses = []

    def delete_backward_connections(self):
        for neuron in self.neuron_vector:
            neuron.input_synapses = []

    def connect_to_next_layer(self, layer):
        for neuron_input in self.neuron_vector:
            for neuron_output in layer.neuron_vector:
                synapse=SynapseFactory.create(neuron_input,neuron_output)
                neuron_input.add_output_synapse(synapse)
                neuron_output.add_input_synapse(synapse)
                if self.tag == LayersTags.HIDDEN_LAYER:
                    neuron_output.add_input_synapse(SynapseFactory.create_bias(self.bias,neuron_output))

    def connect_backward(self, synapse):
        for neuron in self.neuron_vector:
            neuron.add_input_synapse(synapse)
            if self.tag == LayersTags.HIDDEN_LAYER:
                neuron.add_input_synapse(SynapseFactory.create_bias(self.bias))

    def connect_backward_concrete_neuron(self,neuron_index,layer):
        for neuron_input in layer.neuron_vector:
            synapse = SynapseFactory.create(neuron_input,self.neuron_vector[neuron_index])
            neuron_input.add_output_synapse(synapse)
            self.neuron_vector[neuron_index].add_input_synapse(synapse)

    def connect_forward_concrete_neuron(self,neuron_index,layer):
        for neuron_output in layer.neuron_vector:
            synapse = SynapseFactory.create(self.neuron_vector[neuron_index],neuron_output)
            neuron_output.add_input_synapse(synapse)
            self.neuron_vector[neuron_index].add_output_synapse(synapse)

    def update_neuron_ids(self):
        for i in range(len(self.neuron_vector)):
            self.neuron_vector[i].id=i
            self.neuron_vector[i].layer_id=self.id

    def update(self,activation_fun,beta):
        context= UpdatingStrategyContext(self.tag)
        context.strategy.update(self, activation_fun, beta)

    def update_weights(self,activation_fun,learning_factor):
        context = UpdatingWeightsStrategyContext(self.tag)
        context.strategy.update(self, activation_fun, learning_factor)

    def get_layer_output(self):
        output = list()
        for neuron in self.neuron_vector:
            output.append(neuron.output)

        return output

    def print(self):
        print("TAG: {}  layer_id: {} bias {}".format(self.tag,self.id,self.bias))
        for neuron in self.neuron_vector:
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

    @tag.setter
    def tag(self, value):
        self.__tag = value

    @neuron_vector.setter
    def neuron_vector(self, value):
        self.__neuron_vector = value

    @id.setter
    def id(self, value):
        self.__id = value
