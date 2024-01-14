# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.model_class import ModelClass

class TestModelClass(unittest.TestCase):
    """ModelClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelClass:
        """Test ModelClass
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelClass`
        """
        model = ModelClass()
        if include_optional:
            return ModelClass(
                course_id = '',
                course_offer_number = 56,
                session_code = '',
                class_section = 56,
                term_code = '',
                class_number = 56,
                course_component = '',
                associated_class_code = 56,
                max_enrollment_capacity = 56,
                enrolled_students = 56,
                enroll_consent_code = '',
                enroll_consent_description = '',
                drop_consent_code = '',
                drop_consent_description = '',
                schedule_data = [
                    openapi_client.models.class_schedule.ClassSchedule(
                        course_id = '', 
                        course_offer_number = 56, 
                        session_code = '', 
                        class_section = 56, 
                        term_code = '', 
                        class_meeting_number = 56, 
                        schedule_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        schedule_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        class_meeting_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        class_meeting_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        class_meeting_day_pattern_code = '', 
                        class_meeting_week_pattern_code = '', 
                        location_name = '', )
                    ],
                instructor_data = [
                    openapi_client.models.class_instructor.ClassInstructor(
                        course_id = '', 
                        course_offer_number = 56, 
                        session_code = '', 
                        class_section = 56, 
                        term_code = '', 
                        instructor_role_code = '', 
                        instructor_first_name = '', 
                        instructor_last_name = '', 
                        instructor_unique_identifier = '', 
                        class_meeting_number = 56, )
                    ]
            )
        else:
            return ModelClass(
        )
        """

    def testModelClass(self):
        """Test ModelClass"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
