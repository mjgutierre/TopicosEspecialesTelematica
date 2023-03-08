from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrderResponse(_message.Message):
    __slots__ = ["quantity", "status_code", "title"]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    status_code: int
    title: str
    def __init__(self, status_code: _Optional[int] = ..., title: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class ProductOrder(_message.Message):
    __slots__ = ["id_Product", "quantity", "title"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id_Product: int
    quantity: int
    title: str
    def __init__(self, id_Product: _Optional[int] = ..., title: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...
