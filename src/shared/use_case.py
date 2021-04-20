from abc import ABC, abstractmethod


class BaseUseCase(ABC):
    @abstractmethod
    def run(self, files: tuple[str] = ()):
        pass

    @abstractmethod
    def message_create(self):
        pass

    @abstractmethod
    def message_send(self):
        pass
