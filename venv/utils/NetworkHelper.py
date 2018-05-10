from utils.Tags import LayersTags
from factories.NodeFactory import NodeFactory
from utils.Tags import NodesTags

class NetworkHelper():

    @staticmethod
    def merge_autoencoder_to_mlp(encoder,mlp):
        for i in range(len(encoder.layers_list)):
            if encoder.layers_list[i].tag==LayersTags.ENCODER:
                mlp.layers_list.insert(i,encoder.layers_list[i])

        for i in range(len(mlp.layers_list)):
            if mlp.layers_list[i].tag == LayersTags.ENCODER and mlp.layers_list[i+1].tag == LayersTags.HIDDEN_LAYER:
                mlp.layers_list[i].delete_forward_connections()
                mlp.layers_list[i+1].delete_backward_connections()
                mlp.layers_list[i].connect_to_next_layer(mlp.layers_list[i+1])

            if mlp.layers_list[i].tag == LayersTags.INPUT_LAYER and mlp.layers_list[i+1].tag == LayersTags.ENCODER:
                mlp.layers_list[i].delete_forward_connections()
                mlp.layers_list[i+1].delete_backward_connections()
                mlp.layers_list[i].connect_to_next_layer(mlp.layers_list[i+1])

        return mlp

    @staticmethod
    def add_neurons_to_first_hidden_layer(network,number_of_neurons):
        index=0
        for layer in network.layers_list:
            if layer.tag == LayersTags.HIDDEN_LAYER:
                break
            index=index+1

        for i in range(number_of_neurons):
            #print ("index" + sindex)
            network.layers_list[index].neuron_vector.append(NodeFactory.create(NodesTags.MLPNeuron,index,i+50))
            network.layers_list[index].connect_backward_concrete_neuron(-1, network.layers_list[0]) #connecting previously added neuron with input layer
            network.layers_list[index].connect_forward_concrete_neuron(-1, network.layers_list[index+1]) #connecting previously added neuron with next layer

        return network