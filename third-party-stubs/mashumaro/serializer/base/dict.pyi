from typing import Any, Mapping

class DataClassDictMixin:
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    def after_to_dict(self, dct: Any, omit_none: bool=...) -> Any: ...
    @classmethod
    def before_from_dict(cls: Any, d: Mapping) -> Any: ...
    def _to_dict( self, use_bytes: bool = False, use_enum: bool = False, use_datetime: bool = False, omit_none:bool = False) -> dict: ...
    @classmethod
    def _from_dict( cls, d: Mapping, use_bytes: bool = False, use_enum: bool = False, use_datetime: bool = False) -> 'DataClassDictMixin': ...
