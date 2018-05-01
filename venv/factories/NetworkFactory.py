from utils.Tags import NetworkTags
from factories.MLPNetworkFactory import MLPNetworkFactory
from factories.AutoEncodersFactory import AutoEncoderFactory
from factories.SOMFactory import SOMFactory

class NetworkFactory():

    @staticmethod
    def create(network_type,layers):
        if network_type ==  NetworkTags.MLPWithContiguousConnection:
            return MLPNetworkFactory.create_with_contigious_connection(layers)

        elif network_type == NetworkTags.AutoEncoder:
            return AutoEncoderFactory.create(layers)

        elif network_type == NetworkTags.MLPWithEachLayerConnection:
            return MLPNetworkFactory.create_with_each_layer_connection(layers)

        elif network_type == NetworkTags.SOM:
            return SOMFactory.create(layers)


