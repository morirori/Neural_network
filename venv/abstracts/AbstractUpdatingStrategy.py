from abc import ABCMeta, abstractmethod


class AbstractUpdatingStrategy(metaclass=ABCMeta):

    @abstractmethod
    def update(self,layer,activation_fun,beta):
        pass