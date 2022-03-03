#!/usr/bin/env python3
"""A github org client - Test
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient, get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient - class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, m_json):
        """ Test method returns correct output """
        gh_client = GithubOrgClient(org_name)
        gh_client.org()
        m_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(
                org_name))
