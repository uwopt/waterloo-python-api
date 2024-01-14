# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Term(BaseModel):
    """
    An academic Term at Waterloo, a defined period of time that is used by classes and similar
    """ # noqa: E501
    term_code: Optional[StrictStr] = Field(default=None, description="Code that describes this Term", alias="termCode")
    name: Optional[StrictStr] = Field(default=None, description="The Name for this Term, most often the displayed name")
    name_short: Optional[StrictStr] = Field(default=None, description="The short form name for this Term", alias="nameShort")
    term_begin_date: Optional[datetime] = Field(default=None, description="The date and time from which the Term begins, inclusive", alias="termBeginDate")
    term_end_date: Optional[datetime] = Field(default=None, description="The date and time on which the Term ends, inclusive", alias="termEndDate")
    sixty_percent_complete_date: Optional[datetime] = Field(default=None, description="The date and time at which the term is 60% complete, used for standing, withdrawal, and penalties", alias="sixtyPercentCompleteDate")
    associated_academic_year: Optional[StrictInt] = Field(default=None, description="The academic year to which this Term belongs", alias="associatedAcademicYear")
    __properties: ClassVar[List[str]] = ["termCode", "name", "nameShort", "termBeginDate", "termEndDate", "sixtyPercentCompleteDate", "associatedAcademicYear"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Term from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if term_code (nullable) is None
        # and model_fields_set contains the field
        if self.term_code is None and "term_code" in self.model_fields_set:
            _dict['termCode'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if name_short (nullable) is None
        # and model_fields_set contains the field
        if self.name_short is None and "name_short" in self.model_fields_set:
            _dict['nameShort'] = None

        # set to None if sixty_percent_complete_date (nullable) is None
        # and model_fields_set contains the field
        if self.sixty_percent_complete_date is None and "sixty_percent_complete_date" in self.model_fields_set:
            _dict['sixtyPercentCompleteDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Term from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "termCode": obj.get("termCode"),
            "name": obj.get("name"),
            "nameShort": obj.get("nameShort"),
            "termBeginDate": obj.get("termBeginDate"),
            "termEndDate": obj.get("termEndDate"),
            "sixtyPercentCompleteDate": obj.get("sixtyPercentCompleteDate"),
            "associatedAcademicYear": obj.get("associatedAcademicYear")
        })
        return _obj


