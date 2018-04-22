from factories.SynapseFactory import SynapseFactory
from utils.LayersTags import LayersTags
class Layer():

    def __init__(self,neuron_vector ):
         self.neuron_vector=neuron_vector
         self.tag=""
         self.id=0
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
        for neuron in self.neuron_vector:
            neuron.update(activation_fun,beta)

    def update_weights(self,activation_fun,learning_factor):
        if self.tag != LayersTags.OUTPUT_LAYER:
            for neuron in self.neuron_vector:
                neuron.calculate_delta(activation_fun=activation_fun)
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)
        else:
            for neuron in self.neuron_vector:
                neuron.update_weights(learning_factor=learning_factor,activation_fun=activation_fun)

    def get_layer_output(self):
        output=list()
        for neuron in self.neuron_vector:
            output.append(neuron.output)

        return output

    def print(self):
        print("TAG: {}  layer_id: {} bias {}".format(self.tag,self.id,self.bias))
        for neuron in self.neuron_vector:
            print(neuron)
