from providers.service_state import ServiceState


class ServiceStateFactory:

    def create_service_state(self, service_factory):
        return ServiceState(service_factory)