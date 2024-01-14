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

from openapi_client.models.class_instructor import ClassInstructor

class TestClassInstructor(unittest.TestCase):
    """ClassInstructor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClassInstructor:
        """Test ClassInstructor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClassInstructor`
        """
        model = ClassInstructor()
        if include_optional:
            return ClassInstructor(
                course_id = '',
                course_offer_number = 56,
                session_code = '',
                class_section = 56,
                term_code = '',
                instructor_role_code = '',
                instructor_first_name = '',
                instructor_last_name = '',
                instructor_unique_identifier = '',
                class_meeting_number = 56
            )
        else:
            return ClassInstructor(
        )
        """

    def testClassInstructor(self):
        """Test ClassInstructor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
