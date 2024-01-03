class ProviderRegistry:

    def __init__(self, service_state_factory):
        self.service_state_factory = service_state_factory
        self.providers = []
        self.services = {}

    def register_providers(self, provider_factories):
        for provider_factory in provider_factories:
            provider = provider_factory(self.register, self.resolve)
            self.providers.append(provider)

    def run_providers(self):
        for provider in self.providers:
            if provider.register_services:
                provider.register_services()
        self.create_services()
        for provider in self.providers:
            if provider.run_services:
                provider.run_services()
    
    def create_services(self):
        for service_state in self.services.values():
            if not service_state.service:
                service_state.service = service_state.service_factory()

    def get_service(self, service_name):
        if service_name not in self.services:
            raise Exception("Unknown service: " + service_name)
        return self.services[service_name].service

    def register(self, service_name, service_factory):
        service_state = self.service_state_factory.create_service_state(service_factory)
        self.services[service_name] = service_state

    def resolve(self, service_name):
        if service_name not in self.services:
            raise Exception("Unknown service: " + service_name)
        if not self.services[service_name].service:
            service_state = self.services[service_name]
            service_state.service = service_state.service_factory()
        return self.services[service_name].service