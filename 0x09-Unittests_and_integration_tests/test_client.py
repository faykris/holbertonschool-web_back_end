#!/usr/bin/env python3
"""A github org client - Test
"""
import unittest
from unittest.mock import patch, PropertyMock
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
        """test_org"""
        gh_client = GithubOrgClient(org_name)
        gh_client.org()
        m_json.assert_called_once()

    @parameterized.expand([
        ("url", {'repos_url': 'http://www.example.com'})
    ])
    def test_public_repos_url(self, name, expected):
        """test_public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=expected)
                   ):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, expected.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, t_mock):
        """test_public_repos"""
        return_value = [{'name': 'google'}, {'name': 'abc'}]
        t_mock.return_value = return_value
        with patch('client.GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=return_value)
                   ) as m_public:
            response = GithubOrgClient('example')
            self.assertEqual(response.public_repos(), ['google', 'abc'])
            t_mock.assert_called_once()
            m_public.assert_called_once()
