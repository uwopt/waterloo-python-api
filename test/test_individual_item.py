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

from openapi_client.models.individual_item import IndividualItem

class TestIndividualItem(unittest.TestCase):
    """IndividualItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IndividualItem:
        """Test IndividualItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IndividualItem`
        """
        model = IndividualItem()
        if include_optional:
            return IndividualItem(
                name = '',
                photo = openapi_client.models.individual_item_photo.IndividualItemPhoto(
                    id = '', 
                    url = '', 
                    filemime = '', 
                    filesize = '', 
                    width = '', 
                    height = '', 
                    alt = '', 
                    title = '', ),
                price = '',
                calories = None
            )
        else:
            return IndividualItem(
        )
        """

    def testIndividualItem(self):
        """Test IndividualItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()