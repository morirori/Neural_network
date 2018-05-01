from enum import Enum


class NetworkTags(Enum):
    MLPWithContiguousConnection="MLPWithContiguousConnection"
    AutoEncoder="AutoEncoder"
    SOM="SOM"
    MLPWithEachLayerConnection="MLPWithEachLayerConnection"


class LayersTags(Enum):
    INPUT_LAYER="input layer"
    OUTPUT_LAYER="output_layer"
    HIDDEN_LAYER="hidden_layer"
    ENCODER="encoder"
    DECODER="decoder"
    SOM="SOM"


class NodesTags(Enum):
    SOMNeuron = "SOM"
    Bias = "Bias"
    MLPNeuron = "MLPNeuron"