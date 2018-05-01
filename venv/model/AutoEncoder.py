from model.MLPNetwork import MLPNetwork
from utils.Tags import LayersTags
class AutoEncoder(MLPNetwork):

    def calculate(self,beta,activation_function):
        for layer in self.layers_list:
            if layer.tag != LayersTags.INPUT_LAYER:
                layer.update(activation_function, beta)

    def backpropagation(self, learning_factor, activation_function):
        for layer in reversed(self.layers_list):
            if layer.tag == LayersTags.OUTPUT_LAYER:
                self.set_output_delta()
                layer.update_weights(activation_fun=activation_function,learning_factor=learning_factor)
            elif layer.tag == LayersTags.INPUT_LAYER:
                pass
            else:
                layer.update_weights(activation_fun=self.activation_function,learning_factor=learning_factor)

    def remove_unneeded_layers(self):
        index = round((len(self.layers_list))/2)+1
        del self.layers_list[index:]