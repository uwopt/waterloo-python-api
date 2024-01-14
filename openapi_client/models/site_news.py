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

class SiteNews(BaseModel):
    """
    Model representing News data associated to a Site in the WCMS
    """ # noqa: E501
    site_id: Optional[StrictInt] = Field(default=None, description="Unique, numeric site ID of the Site this news originates from", alias="siteId")
    unique_key: Optional[StrictStr] = Field(default=None, description="Unique Id of this news item", alias="uniqueKey")
    title: Optional[StrictStr] = Field(default=None, description="Title of the news item")
    posted_date: Optional[datetime] = Field(default=None, description="Content created or posted date", alias="postedDate")
    updated_date: Optional[datetime] = Field(default=None, description="Content updated date", alias="updatedDate")
    item_uri: Optional[StrictStr] = Field(default=None, description="URI to the news item in WCMS", alias="itemUri")
    audience: Optional[StrictStr] = Field(default=None, description="Intended audience tag(s)")
    content: Optional[StrictStr] = Field(default=None, description="News item content, often with HTML markup")
    __properties: ClassVar[List[str]] = ["siteId", "uniqueKey", "title", "postedDate", "updatedDate", "itemUri", "audience", "content"]

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
        """Create an instance of SiteNews from a JSON string"""
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
        # set to None if unique_key (nullable) is None
        # and model_fields_set contains the field
        if self.unique_key is None and "unique_key" in self.model_fields_set:
            _dict['uniqueKey'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if posted_date (nullable) is None
        # and model_fields_set contains the field
        if self.posted_date is None and "posted_date" in self.model_fields_set:
            _dict['postedDate'] = None

        # set to None if updated_date (nullable) is None
        # and model_fields_set contains the field
        if self.updated_date is None and "updated_date" in self.model_fields_set:
            _dict['updatedDate'] = None

        # set to None if item_uri (nullable) is None
        # and model_fields_set contains the field
        if self.item_uri is None and "item_uri" in self.model_fields_set:
            _dict['itemUri'] = None

        # set to None if audience (nullable) is None
        # and model_fields_set contains the field
        if self.audience is None and "audience" in self.model_fields_set:
            _dict['audience'] = None

        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SiteNews from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "siteId": obj.get("siteId"),
            "uniqueKey": obj.get("uniqueKey"),
            "title": obj.get("title"),
            "postedDate": obj.get("postedDate"),
            "updatedDate": obj.get("updatedDate"),
            "itemUri": obj.get("itemUri"),
            "audience": obj.get("audience"),
            "content": obj.get("content")
        })
        return _obj


