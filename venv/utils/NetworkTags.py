from enum import Enum

class NetworkTags(Enum):
    MLPWithContiguousConnection="MLPWithContiguousConnection"
    AutoEncoder="AutoEncoder"
    SOM="SOM"
    MLPWithEachLayerConnection="MLPWithEachLayerConnection"