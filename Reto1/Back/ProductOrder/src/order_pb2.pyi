from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrderResponse(_message.Message):
    __slots__ = ["customer_name", "status_code"]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    customer_name: str
    status_code: int
    def __init__(self, status_code: _Optional[int] = ..., customer_name: _Optional[str] = ...) -> None: ...

class ProductOrder(_message.Message):
    __slots__ = ["customer_name", "id_Product", "quantity"]
    CUSTOMER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    customer_name: str
    id_Product: int
    quantity: str
    def __init__(self, id_Product: _Optional[int] = ..., customer_name: _Optional[str] = ..., quantity: _Optional[str] = ...) -> None: ...
