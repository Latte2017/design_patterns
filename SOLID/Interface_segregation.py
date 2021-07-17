#Donot create a complex interface
#If needed create multiple interfaces and inherit from it

from abc import ABC, abstractmethod

class print(ABC):

    def print(self, document):
        raise NotImplementedError

class scan(ABC):

    def scan(self, document):
        raise NotImplementedError


class fax(ABC):

    def scan(self, document):
        raise NotImplementedError


class OldFashionedScannerPrinter(scan, print):
    """Only implements scanner and printer"""

    def scan(self, document):
        print(f"document scanned {document}")
    
    def print(self, document):
        print(f"document printer {document}")

class Photocopier(scan, print):

    
    def scan(self, document):
        print(f"document scanned {document}")
    
    
    def print(self, document):
        print(f"document printer {document}")
    
    def copy_photo(self, document):
        #First scan photo and print it
        self.scan()
        self.print()
    
