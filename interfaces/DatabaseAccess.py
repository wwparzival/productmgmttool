from abc import ABC, abstractmethod

# Abstract Class
class DatabaseAccess(ABC):
    
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass