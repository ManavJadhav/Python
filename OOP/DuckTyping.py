# Duck Typing : It is a concept where the type of an object is determined
# by its behaviour , not by its class 

class InkjetPrinter :
    def printdocument(self,document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser printer printing : ",document)

class PDFWriter:
    def printdocument(self,document):
        print(f"Saving {document} as PDF ")

def StartPrinting(Device):
    Device.printdocument("Python Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()