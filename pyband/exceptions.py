class PybandError(Exception):
    pass


class ValueTooLargeError(PybandError):
    pass


class EmptyMsgError(PybandError):
    pass


class NotFoundError(PybandError):
    pass


class UndefinedError(PybandError):
    pass


class DecodeError(PybandError):
    pass


class ConvertError(PybandError):
    pass


class SchemaError(PybandError):
    pass
