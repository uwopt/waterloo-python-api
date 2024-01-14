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
from pydantic import BaseModel, StrictStr
from openapi_client.models.locpick import Locpick
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OutletLocation(BaseModel):
    """
    OutletLocation
    """ # noqa: E501
    lid: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    additional: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    province: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    latitude: Optional[StrictStr] = None
    longitude: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    is_primary: Optional[StrictStr] = None
    locpick: Optional[Locpick] = None
    province_name: Optional[StrictStr] = None
    country_name: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["lid", "name", "street", "additional", "city", "province", "postal_code", "country", "latitude", "longitude", "source", "is_primary", "locpick", "province_name", "country_name"]

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
        """Create an instance of OutletLocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of locpick
        if self.locpick:
            _dict['locpick'] = self.locpick.to_dict()
        # set to None if lid (nullable) is None
        # and model_fields_set contains the field
        if self.lid is None and "lid" in self.model_fields_set:
            _dict['lid'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if street (nullable) is None
        # and model_fields_set contains the field
        if self.street is None and "street" in self.model_fields_set:
            _dict['street'] = None

        # set to None if additional (nullable) is None
        # and model_fields_set contains the field
        if self.additional is None and "additional" in self.model_fields_set:
            _dict['additional'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if province (nullable) is None
        # and model_fields_set contains the field
        if self.province is None and "province" in self.model_fields_set:
            _dict['province'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postal_code'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if is_primary (nullable) is None
        # and model_fields_set contains the field
        if self.is_primary is None and "is_primary" in self.model_fields_set:
            _dict['is_primary'] = None

        # set to None if province_name (nullable) is None
        # and model_fields_set contains the field
        if self.province_name is None and "province_name" in self.model_fields_set:
            _dict['province_name'] = None

        # set to None if country_name (nullable) is None
        # and model_fields_set contains the field
        if self.country_name is None and "country_name" in self.model_fields_set:
            _dict['country_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OutletLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lid": obj.get("lid"),
            "name": obj.get("name"),
            "street": obj.get("street"),
            "additional": obj.get("additional"),
            "city": obj.get("city"),
            "province": obj.get("province"),
            "postal_code": obj.get("postal_code"),
            "country": obj.get("country"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "source": obj.get("source"),
            "is_primary": obj.get("is_primary"),
            "locpick": Locpick.from_dict(obj.get("locpick")) if obj.get("locpick") is not None else None,
            "province_name": obj.get("province_name"),
            "country_name": obj.get("country_name")
        })
        return _obj

