from abc import ABCMeta, abstractmethod


class AbstractLayer(metaclass=ABCMeta):

    @property
    @abstractmethod
    def neuron_vector(self):
        pass

    @property
    @abstractmethod
    def tag(self):
        pass

    @property
    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def update_weights(self):
        pass

    @abstractmethod
    def update(self):
        pass