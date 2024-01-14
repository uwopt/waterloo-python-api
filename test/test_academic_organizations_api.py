# coding: utf-8

"""
    Waterloo OpenData API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.academic_organizations_api import AcademicOrganizationsApi


class TestAcademicOrganizationsApi(unittest.TestCase):
    """AcademicOrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AcademicOrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_v3_academic_organizations_get(self) -> None:
        """Test case for v3_academic_organizations_get

        Gets all Academic Organization data
        """
        pass

    def test_v3_academic_organizations_organization_code_get(self) -> None:
        """Test case for v3_academic_organizations_organization_code_get

        Gets Academic Organization data for a specific entry by the Organization code
        """
        pass


if __name__ == '__main__':
    unittest.main()