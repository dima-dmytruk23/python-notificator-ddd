from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class NotificationContext:
    _notification: NotificationBase

    @property
    def notification(self) -> NotificationBase:
        return self._notification

    @notification.setter
    def notification(self, notification: NotificationBase) -> None:
        self._notification = notification

    def send_notification(self) -> None:
        self._notification.run()


class NotificationBase(ABC):
    @abstractmethod
    def run(self):
        pass
