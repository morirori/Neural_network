from utils.DataImporter import Data_importer
from model.Layers import InputLayer
from model.Neuron import Neuron
from model.Layers import Layer
from model.Synapse import Synapse


importer= Data_importer("resources/IrisDataTrain.xls")
data=importer.import_data_to_list_of_dict(1)

input_vector=[]
print("input data")
print(data[0])

input_vector.append(data[0]["leaf-length"])
input_vector.append(data[0]["leaf-width"])
input_vector.append(data[0]["petal-length"])
input_vector.append(data[0]["petal-width"])

synapse = Synapse()
synapse.add_neuron(input_vector[0],0.1)
synapse.add_neuron(input_vector[1],0.4)
synapse.add_neuron(input_vector[2],1.0)
synapse.add_neuron(input_vector[3],0.5)

neuron = Neuron(synapse)
print("synapses")
print(neuron.input_synapses)
neuron.calucate_weights()
print("unnormalized data")
print(synapse.get_raw_data())
neuron.normalize_data()
print("normalized data")
print(neuron.normalized_input_data)


neuron.calculate_output()
print("output")
print(neuron.output)




