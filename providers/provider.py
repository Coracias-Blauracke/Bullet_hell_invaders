class Provider:

    def __init__(self, register, resolve):
        self.register = register
        self.resolve = resolve
    
    def register_services(self):
        raise NotImplementedError
    
    def run_services(self):
        raise NotImplementedError