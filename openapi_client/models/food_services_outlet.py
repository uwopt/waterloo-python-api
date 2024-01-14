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
from openapi_client.models.closed import Closed
from openapi_client.models.cuisine import Cuisine
from openapi_client.models.food_services_outlet_image import FoodServicesOutletImage
from openapi_client.models.food_services_outlet_photo import FoodServicesOutletPhoto
from openapi_client.models.franchise_menu import FranchiseMenu
from openapi_client.models.hours_change import HoursChange
from openapi_client.models.location_link import LocationLink
from openapi_client.models.opening_hour import OpeningHour
from openapi_client.models.outlet_location import OutletLocation
from openapi_client.models.outlet_type import OutletType
from openapi_client.models.payment_accepted import PaymentAccepted
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FoodServicesOutlet(BaseModel):
    """
    FoodServicesOutlet
    """ # noqa: E501
    id: Optional[StrictInt] = None
    var_self: Optional[StrictStr] = Field(default=None, alias="self")
    name: Optional[StrictStr] = None
    image: Optional[List[FoodServicesOutletImage]] = None
    photo: Optional[FoodServicesOutletPhoto] = None
    features: Optional[StrictStr] = None
    outlettype: Optional[List[OutletType]] = None
    outletlocation: Optional[StrictStr] = None
    locationlink: Optional[LocationLink] = None
    description: Optional[StrictStr] = None
    location: Optional[List[OutletLocation]] = None
    summary: Optional[StrictStr] = None
    cuisine: Optional[List[Cuisine]] = None
    openinghours: Optional[List[OpeningHour]] = None
    paymentaccepted: Optional[List[PaymentAccepted]] = None
    closed: Optional[List[Closed]] = None
    hourschange: Optional[List[HoursChange]] = None
    notice: Optional[StrictStr] = None
    franchisemenu: Optional[List[FranchiseMenu]] = None
    sticky: Optional[StrictStr] = None
    created: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "self", "name", "image", "photo", "features", "outlettype", "outletlocation", "locationlink", "description", "location", "summary", "cuisine", "openinghours", "paymentaccepted", "closed", "hourschange", "notice", "franchisemenu", "sticky", "created"]

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
        """Create an instance of FoodServicesOutlet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in image (list)
        _items = []
        if self.image:
            for _item in self.image:
                if _item:
                    _items.append(_item.to_dict())
            _dict['image'] = _items
        # override the default output from pydantic by calling `to_dict()` of photo
        if self.photo:
            _dict['photo'] = self.photo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in outlettype (list)
        _items = []
        if self.outlettype:
            for _item in self.outlettype:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outlettype'] = _items
        # override the default output from pydantic by calling `to_dict()` of locationlink
        if self.locationlink:
            _dict['locationlink'] = self.locationlink.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in location (list)
        _items = []
        if self.location:
            for _item in self.location:
                if _item:
                    _items.append(_item.to_dict())
            _dict['location'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cuisine (list)
        _items = []
        if self.cuisine:
            for _item in self.cuisine:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cuisine'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in openinghours (list)
        _items = []
        if self.openinghours:
            for _item in self.openinghours:
                if _item:
                    _items.append(_item.to_dict())
            _dict['openinghours'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in paymentaccepted (list)
        _items = []
        if self.paymentaccepted:
            for _item in self.paymentaccepted:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paymentaccepted'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in closed (list)
        _items = []
        if self.closed:
            for _item in self.closed:
                if _item:
                    _items.append(_item.to_dict())
            _dict['closed'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hourschange (list)
        _items = []
        if self.hourschange:
            for _item in self.hourschange:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hourschange'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in franchisemenu (list)
        _items = []
        if self.franchisemenu:
            for _item in self.franchisemenu:
                if _item:
                    _items.append(_item.to_dict())
            _dict['franchisemenu'] = _items
        # set to None if var_self (nullable) is None
        # and model_fields_set contains the field
        if self.var_self is None and "var_self" in self.model_fields_set:
            _dict['self'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        # set to None if outlettype (nullable) is None
        # and model_fields_set contains the field
        if self.outlettype is None and "outlettype" in self.model_fields_set:
            _dict['outlettype'] = None

        # set to None if outletlocation (nullable) is None
        # and model_fields_set contains the field
        if self.outletlocation is None and "outletlocation" in self.model_fields_set:
            _dict['outletlocation'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if cuisine (nullable) is None
        # and model_fields_set contains the field
        if self.cuisine is None and "cuisine" in self.model_fields_set:
            _dict['cuisine'] = None

        # set to None if openinghours (nullable) is None
        # and model_fields_set contains the field
        if self.openinghours is None and "openinghours" in self.model_fields_set:
            _dict['openinghours'] = None

        # set to None if paymentaccepted (nullable) is None
        # and model_fields_set contains the field
        if self.paymentaccepted is None and "paymentaccepted" in self.model_fields_set:
            _dict['paymentaccepted'] = None

        # set to None if closed (nullable) is None
        # and model_fields_set contains the field
        if self.closed is None and "closed" in self.model_fields_set:
            _dict['closed'] = None

        # set to None if hourschange (nullable) is None
        # and model_fields_set contains the field
        if self.hourschange is None and "hourschange" in self.model_fields_set:
            _dict['hourschange'] = None

        # set to None if notice (nullable) is None
        # and model_fields_set contains the field
        if self.notice is None and "notice" in self.model_fields_set:
            _dict['notice'] = None

        # set to None if franchisemenu (nullable) is None
        # and model_fields_set contains the field
        if self.franchisemenu is None and "franchisemenu" in self.model_fields_set:
            _dict['franchisemenu'] = None

        # set to None if sticky (nullable) is None
        # and model_fields_set contains the field
        if self.sticky is None and "sticky" in self.model_fields_set:
            _dict['sticky'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FoodServicesOutlet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "self": obj.get("self"),
            "name": obj.get("name"),
            "image": [FoodServicesOutletImage.from_dict(_item) for _item in obj.get("image")] if obj.get("image") is not None else None,
            "photo": FoodServicesOutletPhoto.from_dict(obj.get("photo")) if obj.get("photo") is not None else None,
            "features": obj.get("features"),
            "outlettype": [OutletType.from_dict(_item) for _item in obj.get("outlettype")] if obj.get("outlettype") is not None else None,
            "outletlocation": obj.get("outletlocation"),
            "locationlink": LocationLink.from_dict(obj.get("locationlink")) if obj.get("locationlink") is not None else None,
            "description": obj.get("description"),
            "location": [OutletLocation.from_dict(_item) for _item in obj.get("location")] if obj.get("location") is not None else None,
            "summary": obj.get("summary"),
            "cuisine": [Cuisine.from_dict(_item) for _item in obj.get("cuisine")] if obj.get("cuisine") is not None else None,
            "openinghours": [OpeningHour.from_dict(_item) for _item in obj.get("openinghours")] if obj.get("openinghours") is not None else None,
            "paymentaccepted": [PaymentAccepted.from_dict(_item) for _item in obj.get("paymentaccepted")] if obj.get("paymentaccepted") is not None else None,
            "closed": [Closed.from_dict(_item) for _item in obj.get("closed")] if obj.get("closed") is not None else None,
            "hourschange": [HoursChange.from_dict(_item) for _item in obj.get("hourschange")] if obj.get("hourschange") is not None else None,
            "notice": obj.get("notice"),
            "franchisemenu": [FranchiseMenu.from_dict(_item) for _item in obj.get("franchisemenu")] if obj.get("franchisemenu") is not None else None,
            "sticky": obj.get("sticky"),
            "created": obj.get("created")
        })
        return _obj


