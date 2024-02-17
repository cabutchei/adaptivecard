from typing import Protocol, Sequence, Iterator, TypeVar, Any, SupportsIndex, overload, runtime_checkable


_T_co = TypeVar("_T_co", covariant=True)

@runtime_checkable
class SequenceNotStr(Protocol[_T_co]):
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> _T_co:
        ...

    @overload
    def __getitem__(self, index: slice, /) -> Sequence[_T_co]:
        ...

    def __contains__(self, value: object, /) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __iter__(self) -> Iterator[_T_co]:
        ...

    def index(self, value: Any, start: int = ..., stop: int = ..., /) -> int:
        ...

    def count(self, value: Any, /) -> int:
        ...

    def __reversed__(self) -> Iterator[_T_co]:
        ...

ListLike = SequenceNotStr