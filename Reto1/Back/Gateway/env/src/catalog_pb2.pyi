from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["id_Product", "price", "title"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id_Product: int
    price: float
    title: str
    def __init__(self, id_Product: _Optional[int] = ..., title: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["price", "status_code", "title"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    price: float
    status_code: int
    title: str
    def __init__(self, status_code: _Optional[int] = ..., title: _Optional[str] = ..., price: _Optional[float] = ...) -> None: ...
