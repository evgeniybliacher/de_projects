from collections.abc import Callable


type Predicate[T] = Callable[[T], bool]


class GuardError(Exception):
    """Base exception for guard failures."""


class PreconditionError(GuardError):
    """Raised when a precondition is not satisfied."""


class PostconditionError(GuardError):
    """Raised when a postcondition is not satisfied."""


class InvariantError(GuardError):
    """Raised when an invariant is violated."""


class AssertionGuardError(GuardError):
    """Raised when an internal assertion is violated."""


def guard(
    condition: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates a boolean condition.

    Returns True when the condition is satisfied.
    Raises the supplied exception when the condition is False.
    """
    if isinstance(error, str):
        error = GuardError(error)
    if not condition:
        raise error or GuardError("Guard condition failed")

    return True


def guard_value[T](
    value: T,
    predicate: Predicate[T],
    error: Exception | None = None,
) -> T:
    """
    Validates a value using a predicate.

    Returns the original value when the predicate succeeds.
    Raises the supplied exception when the predicate fails.
    """
    if not predicate(value):
        raise error or GuardError("Guard condition failed")

    return value


def require(
    condition: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates a precondition before an operation.
    """
    return guard(
        condition,
        error or PreconditionError("Precondition failed"),
    )


def require_value[T](
    value: T,
    predicate: Predicate[T],
    error: Exception | None = None,
) -> T:
    """
    Validates a value-based precondition.
    """
    return guard_value(
        value,
        predicate,
        error or PreconditionError("Precondition failed"),
    )


def ensure(
    condition: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates a postcondition after an operation.
    """
    return guard(
        condition,
        error or PostconditionError("Postcondition failed"),
    )


def ensure_value[T](
    value: T,
    predicate: Predicate[T],
    error: Exception | None = None,
) -> T:
    """
    Validates a value-based postcondition.
    """
    return guard_value(
        value,
        predicate,
        error or PostconditionError("Postcondition failed"),
    )


def invariant(
    condition: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates a condition that must always remain true.
    """
    return guard(
        condition,
        error or InvariantError("Invariant violated"),
    )


def invariant_value[T](
    value: T,
    predicate: Predicate[T],
    error: Exception | None = None,
) -> T:
    """
    Validates a value-based invariant.
    """
    return guard_value(
        value,
        predicate,
        error or InvariantError("Invariant violated"),
    )


def assert_that(
    condition: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates an internal programming assumption.
    """
    return guard(
        condition,
        error or AssertionGuardError("Assertion failed"),
    )


def assert_value[T](
    value: T,
    predicate: Predicate[T],
    error: Exception | None = None,
) -> T:
    """
    Validates a value-based internal programming assumption.
    """
    return guard_value(
        value,
        predicate,
        error or AssertionGuardError("Assertion failed"),
    )

def assert_at_least_one(
    first_value: bool,
    second_value: bool,
    error: Exception | None = None,
) -> bool:
    """
    Validates that at least one of the provided conditions is true.
    """

    return guard(
        first_value or second_value,
        error or AssertionGuardError("At least one condition must be true"),
    )