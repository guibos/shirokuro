from abc import ABC, abstractmethod

from context.shared.domain.bus.command.command import Command


class CommandHandler(ABC):
    @abstractmethod
    def __call__(self, command: Command):
        pass
