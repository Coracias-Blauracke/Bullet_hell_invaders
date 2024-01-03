class ServiceState:

    def __init__(self, service_factory):
        self.service_factory = service_factory
        self.service = None