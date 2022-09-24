from abc import abstractmethod

from betterproto import Message, Casing


class BaseMessageWrapper(Message):
    @property
    @abstractmethod
    def type_url(self):
        return ""

    @property
    @abstractmethod
    def legacy_url(self):
        return ""

    def to_data(self):
        return {"@type": self.type_url} | self.to_dict(include_default_values=True)

    def to_legacy_codec(self):
        return {"type": self.legacy_url, "value": self.to_dict(include_default_values=True, casing=Casing.SNAKE)}
