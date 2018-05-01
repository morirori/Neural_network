from abc import ABCMeta, abstractmethod


class AbstractUpdatingWeightsStrategy(metaclass=ABCMeta):

    @abstractmethod
    def update(self,layer,activation_fun,beta):
        pass