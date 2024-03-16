from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Record(_message.Message):
    __slots__ = ("timestamp", "stream", "length", "word_size", "words")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    WORD_SIZE_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    stream: int
    length: int
    word_size: int
    words: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        timestamp: _Optional[int] = ...,
        stream: _Optional[int] = ...,
        length: _Optional[int] = ...,
        word_size: _Optional[int] = ...,
        words: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class File(_message.Message):
    __slots__ = ("records",)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[Record]
    def __init__(
        self, records: _Optional[_Iterable[_Union[Record, _Mapping]]] = ..., **kwargs
    ) -> None: ...
