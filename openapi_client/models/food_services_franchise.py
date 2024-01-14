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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.addon import Addon
from openapi_client.models.combo import Combo
from openapi_client.models.individual_item import IndividualItem
from openapi_client.models.logo import Logo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FoodServicesFranchise(BaseModel):
    """
    FoodServicesFranchise
    """ # noqa: E501
    id: Optional[StrictInt] = None
    var_self: Optional[StrictStr] = Field(default=None, alias="self")
    name: Optional[StrictStr] = None
    logo: Optional[Logo] = None
    combos: Optional[List[Combo]] = None
    individualitems: Optional[List[IndividualItem]] = None
    addons: Optional[List[Addon]] = None
    __properties: ClassVar[List[str]] = ["id", "self", "name", "logo", "combos", "individualitems", "addons"]

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
        """Create an instance of FoodServicesFranchise from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in combos (list)
        _items = []
        if self.combos:
            for _item in self.combos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['combos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in individualitems (list)
        _items = []
        if self.individualitems:
            for _item in self.individualitems:
                if _item:
                    _items.append(_item.to_dict())
            _dict['individualitems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addons (list)
        _items = []
        if self.addons:
            for _item in self.addons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addons'] = _items
        # set to None if var_self (nullable) is None
        # and model_fields_set contains the field
        if self.var_self is None and "var_self" in self.model_fields_set:
            _dict['self'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if combos (nullable) is None
        # and model_fields_set contains the field
        if self.combos is None and "combos" in self.model_fields_set:
            _dict['combos'] = None

        # set to None if individualitems (nullable) is None
        # and model_fields_set contains the field
        if self.individualitems is None and "individualitems" in self.model_fields_set:
            _dict['individualitems'] = None

        # set to None if addons (nullable) is None
        # and model_fields_set contains the field
        if self.addons is None and "addons" in self.model_fields_set:
            _dict['addons'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FoodServicesFranchise from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "self": obj.get("self"),
            "name": obj.get("name"),
            "logo": Logo.from_dict(obj.get("logo")) if obj.get("logo") is not None else None,
            "combos": [Combo.from_dict(_item) for _item in obj.get("combos")] if obj.get("combos") is not None else None,
            "individualitems": [IndividualItem.from_dict(_item) for _item in obj.get("individualitems")] if obj.get("individualitems") is not None else None,
            "addons": [Addon.from_dict(_item) for _item in obj.get("addons")] if obj.get("addons") is not None else None
        })
        return _obj

