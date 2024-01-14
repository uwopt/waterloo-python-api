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

class ClassSchedule(BaseModel):
    """
    Data describing scheduling and availability data for a Class
    """ # noqa: E501
    course_id: Optional[StrictStr] = Field(default=None, description="Course identifier number, not unique", alias="courseId")
    course_offer_number: Optional[StrictInt] = Field(default=None, description="Course offer number identifier for this class", alias="courseOfferNumber")
    session_code: Optional[StrictStr] = Field(default=None, description="Session code number for this class", alias="sessionCode")
    class_section: Optional[StrictInt] = Field(default=None, description="Number identifying the section of this class", alias="classSection")
    term_code: Optional[StrictStr] = Field(default=None, description="Waterloo academic term code", alias="termCode")
    class_meeting_number: Optional[StrictInt] = Field(default=None, description="Identifier for the class meeting this schedule data relates to", alias="classMeetingNumber")
    schedule_start_date: Optional[datetime] = Field(default=None, description="The date this schedule begins", alias="scheduleStartDate")
    schedule_end_date: Optional[datetime] = Field(default=None, description="The date this schedule ends", alias="scheduleEndDate")
    class_meeting_start_time: Optional[datetime] = Field(default=None, description="The start time of this class", alias="classMeetingStartTime")
    class_meeting_end_time: Optional[datetime] = Field(default=None, description="The end time of this class", alias="classMeetingEndTime")
    class_meeting_day_pattern_code: Optional[StrictStr] = Field(default=None, description="A code representing the days the class schedule takes place during the week", alias="classMeetingDayPatternCode")
    class_meeting_week_pattern_code: Optional[StrictStr] = Field(default=None, description="A Y|N per day representation of the class schedule taking place during the week", alias="classMeetingWeekPatternCode")
    location_name: Optional[StrictStr] = Field(default=None, description="REMOVED for privacy. Building and room name for the location of this class schedule", alias="locationName")
    __properties: ClassVar[List[str]] = ["courseId", "courseOfferNumber", "sessionCode", "classSection", "termCode", "classMeetingNumber", "scheduleStartDate", "scheduleEndDate", "classMeetingStartTime", "classMeetingEndTime", "classMeetingDayPatternCode", "classMeetingWeekPatternCode", "locationName"]

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
        """Create an instance of ClassSchedule from a JSON string"""
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
        # set to None if course_id (nullable) is None
        # and model_fields_set contains the field
        if self.course_id is None and "course_id" in self.model_fields_set:
            _dict['courseId'] = None

        # set to None if session_code (nullable) is None
        # and model_fields_set contains the field
        if self.session_code is None and "session_code" in self.model_fields_set:
            _dict['sessionCode'] = None

        # set to None if term_code (nullable) is None
        # and model_fields_set contains the field
        if self.term_code is None and "term_code" in self.model_fields_set:
            _dict['termCode'] = None

        # set to None if class_meeting_day_pattern_code (nullable) is None
        # and model_fields_set contains the field
        if self.class_meeting_day_pattern_code is None and "class_meeting_day_pattern_code" in self.model_fields_set:
            _dict['classMeetingDayPatternCode'] = None

        # set to None if class_meeting_week_pattern_code (nullable) is None
        # and model_fields_set contains the field
        if self.class_meeting_week_pattern_code is None and "class_meeting_week_pattern_code" in self.model_fields_set:
            _dict['classMeetingWeekPatternCode'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['locationName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ClassSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "courseId": obj.get("courseId"),
            "courseOfferNumber": obj.get("courseOfferNumber"),
            "sessionCode": obj.get("sessionCode"),
            "classSection": obj.get("classSection"),
            "termCode": obj.get("termCode"),
            "classMeetingNumber": obj.get("classMeetingNumber"),
            "scheduleStartDate": obj.get("scheduleStartDate"),
            "scheduleEndDate": obj.get("scheduleEndDate"),
            "classMeetingStartTime": obj.get("classMeetingStartTime"),
            "classMeetingEndTime": obj.get("classMeetingEndTime"),
            "classMeetingDayPatternCode": obj.get("classMeetingDayPatternCode"),
            "classMeetingWeekPatternCode": obj.get("classMeetingWeekPatternCode"),
            "locationName": obj.get("locationName")
        })
        return _obj

