# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.locations_api import LocationsApi


class TestLocationsApi(unittest.TestCase):
    """LocationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LocationsApi()

    def tearDown(self) -> None:
        pass

    def test_v3_locations_geojson_get(self) -> None:
        """Test case for v3_locations_geojson_get

        Get all building location data as GEO JSON
        """
        pass

    def test_v3_locations_get(self) -> None:
        """Test case for v3_locations_get

        Get all building location data
        """
        pass

    def test_v3_locations_location_code_geojson_get(self) -> None:
        """Test case for v3_locations_location_code_geojson_get

        Gets building by matched building code, case insensitive, as GEO JSON
        """
        pass

    def test_v3_locations_location_code_get(self) -> None:
        """Test case for v3_locations_location_code_get

        Gets building by matched building code, case insensitive
        """
        pass

    def test_v3_locations_search_location_name_geojson_get(self) -> None:
        """Test case for v3_locations_search_location_name_geojson_get

        Gets buildings by matched building name, contains, case insensitive, as GEO JSON
        """
        pass

    def test_v3_locations_search_location_name_get(self) -> None:
        """Test case for v3_locations_search_location_name_get

        Gets buildings by matched building name, contains, case insensitive
        """
        pass


if __name__ == '__main__':
    unittest.main()
