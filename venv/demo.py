from utils.DataImporter import Data_importer
from model.Layers import InputLayer
from model.Neuron import Neuron
from model.Layers import Layer
from model.Synapse import Synapse




importer= Data_importer("resources/IrisDataTrain.xls")
data=importer.import_data_to_list_of_dict(127)

input_vector=[]
print("input data")
print(data[0])
label = importer.class_to_label(127)

synapse = Synapse()
synapse2 = Synapse()
synapse3 = Synapse()

neuron = Neuron(synapse)

neuron2 = Neuron(synapse2)

neuron3 = Neuron(synapse3)
neuron_vector = [neuron, neuron2, neuron3]
layer=Layer(neuron_vector,label=label[1])

print (data)

for i in range(len(data)):

#    print(label)

    if i ==0:
        # input_vector.append(data[i]["leaf-length"])
        # input_vector.append(data[i]["leaf-width"])
        # input_vector.append(data[i]["petal-length"])
        # input_vector.append(data[i]["petal-width"])

        # synapse2.add_connection(input_vector[0],0.5)
        # synapse2.add_connection(input_vector[1],0.3)
        # synapse2.add_connection(input_vector[2],0.2)
        # synapse2.add_connection(input_vector[3],0.75)
        #
        # synapse3.add_connection(input_vector[0],0.14)
        # synapse3.add_connection(input_vector[1],0.26)
        # synapse3.add_connection(input_vector[2],0.78)
        # synapse3.add_connection(input_vector[3],0.85)



        synapse.add_connection(data[i]["leaf-length"],0.1)
        synapse.add_connection(data[i]["leaf-width"],0.4)
        synapse.add_connection(data[i]["petal-length"],1.0)
        synapse.add_connection(data[i]["petal-width"],0.5)

        synapse2.add_connection(data[i]["leaf-length"],0.14)
        synapse2.add_connection(data[i]["leaf-width"],0.3)
        synapse2.add_connection(data[i]["petal-length"],0.2)
        synapse2.add_connection(data[i]["petal-width"],0.75)

        synapse3.add_connection(data[i]["leaf-length"],0.5)
        synapse3.add_connection(data[i]["leaf-width"],0.26)
        synapse3.add_connection(data[i]["petal-length"],0.78)
        synapse3.add_connection(data[i]["petal-width"],0.85)

        print("neuron1")
        print(neuron.input_synapses)
        print("neuron2")
        print(neuron2.input_synapses)
        print("neuron3")
        print(neuron3.input_synapses)


    else:

        synapse.update_neuron(0,data[i]["leaf-length"])
        synapse.update_neuron(1,data[i]["leaf-width"])
        synapse.update_neuron(2,data[i]["petal-length"])
        synapse.update_neuron(3,data[i]["petal-width"])

        synapse2.update_neuron(0,data[i]["leaf-length"])
        synapse2.update_neuron(1,data[i]["leaf-width"])
        synapse2.update_neuron(2,data[i]["petal-length"])
        synapse2.update_neuron(3,data[i]["petal-width"])

        synapse3.update_neuron(0,data[i]["leaf-length"])
        synapse3.update_neuron(1,data[i]["leaf-width"])
        synapse3.update_neuron(2,data[i]["petal-length"])
        synapse3.update_neuron(3,data[i]["petal-width"])


    layer.update_label(label[i])
    print(layer.label)
    layer.train()

    print("neuron1 output")
    print(neuron.output)
    print("label")
    print(layer.label)
    print("delta")
    print(neuron.delta)
    print("synapsy")
    print(neuron.input_synapses)

    print("neuron2 output")
    print(neuron2.output)
    print("label")
    print(layer.label)
    print("delta")
    print(neuron2.delta)
    print("synapsy")
    print(neuron2.input_synapses)

    print("neuron3 output")
    print(neuron3.output)
    print("label")
    print(layer.label)
    print("delta")
    print(neuron3.delta)
    print("synapsy")
    print(neuron3.input_synapses)

