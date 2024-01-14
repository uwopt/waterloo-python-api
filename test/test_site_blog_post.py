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

from openapi_client.models.site_blog_post import SiteBlogPost

class TestSiteBlogPost(unittest.TestCase):
    """SiteBlogPost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SiteBlogPost:
        """Test SiteBlogPost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SiteBlogPost`
        """
        model = SiteBlogPost()
        if include_optional:
            return SiteBlogPost(
                site_id = 56,
                unique_key = '',
                title = '',
                posted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                item_uri = '',
                audience = '',
                content = '',
                delegated_author_name = '',
                delegated_author_uri = '',
                publisher_username = ''
            )
        else:
            return SiteBlogPost(
        )
        """

    def testSiteBlogPost(self):
        """Test SiteBlogPost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
