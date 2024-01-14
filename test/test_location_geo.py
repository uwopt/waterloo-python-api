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

from openapi_client.models.location_geo import LocationGeo

class TestLocationGeo(unittest.TestCase):
    """LocationGeo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocationGeo:
        """Test LocationGeo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocationGeo`
        """
        model = LocationGeo()
        if include_optional:
            return LocationGeo(
                type = '',
                features = [
                    openapi_client.models.feature.Feature(
                        type = '', 
                        properties = openapi_client.models.location.Location(
                            building_id = '', 
                            building_code = '', 
                            parent_building_code = '', 
                            building_name = '', 
                            alternate_building_names = [
                                ''
                                ], 
                            latitude = 1.337, 
                            longitude = 1.337, ), 
                        geometry = openapi_client.models.geometry.Geometry(
                            type = '', 
                            coordinates = [
                                1.337
                                ], ), )
                    ]
            )
        else:
            return LocationGeo(
        )
        """

    def testLocationGeo(self):
        """Test LocationGeo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
