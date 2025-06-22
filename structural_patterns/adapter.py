
# Old interface, expecting this method 
class OldPrinter:
    def print_text(self, text):
        print(f"Old Printer: {text}")
        
# Class with new interface
class NewPrinter:
    def print_modern(self, message):
        print(f"New Printer: {message}")
        
# Adapter that adjusting new interface to old interface
class PrinterAdapter:
    def __init__(self, new_printer):
        self.new_printer = new_printer
        
    def print_text(self, text):
        # Adapter translating the method to new interface
        self.new_printer.print_modern(text)
        
def client_code(printer_type, msg):
    printer_type.print_text(msg)
        
        
if __name__ == "__main__":
    old = OldPrinter()
    new = NewPrinter()
    adapter = PrinterAdapter(new)
    
    client_code(old, "Hello")
    client_code(adapter, "Hello New")