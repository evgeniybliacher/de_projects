from typing import Any, Protocol, runtime_checkable

@runtime_checkable
class Logger(Protocol):
    def debug(self, event: str, **kwargs: Any) -> Any: ...
    def info(self, event: str, **kwargs: Any) -> Any: ...
    def warning(self, event: str, **kwargs: Any) -> Any: ...
    def error(self, event: str, **kwargs: Any) -> Any: ...
    def exception(self, event: str, **kwargs: Any) -> Any: ...

class NullLogger:
    def debug(self, event: str, **kwargs: Any) -> None:
        pass

    def info(self, event: str, **kwargs: Any) -> None:
        pass

    def warning(self, event: str, **kwargs: Any) -> None:
        pass

    def error(self, event: str, **kwargs: Any) -> None:
        pass

    def exception(self, event: str, **kwargs: Any) -> None:
        pass