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

from openapi_client.models.en2 import En2

class TestEn2(unittest.TestCase):
    """En2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> En2:
        """Test En2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `En2`
        """
        model = En2()
        if include_optional:
            return En2(
                entity_type = '',
                entity_id = '',
                revision_id = '',
                language = '',
                source = '',
                uid = '',
                status = '',
                translate = '',
                created = '',
                changed = ''
            )
        else:
            return En2(
        )
        """

    def testEn2(self):
        """Test En2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
