from dataclasses import dataclass


@dataclass
class ReferencePriceUpdated(object):
    base: int
    quote: int


@dataclass
class ReferencePrice(object):
    pair: str
    rate: float
    updated_at: ReferencePriceUpdated
