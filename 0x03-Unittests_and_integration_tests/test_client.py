#!/usr/bin/env python3
"""  write the second unittest for client
    """

import unittest
from unittest.mock import DEFAULT, MagicMock, PropertyMock, patch
from typing import Mapping, Sequence
from client import GithubOrgClient, get_json
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """ class for githuborgclient class and whole client file """
    @parameterized.expand([["google"], ["abc"]])
    @patch.object(GithubOrgClient, "org")
    def test_org(self, org_T, mock):
        """ function to test GithuborgClient"""
        GithubOrgClient.org(org_T)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """ testing _public_repos_url method """
        with patch("test_client.GithubOrgClient.org",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "google-ish"}) as m:
            access = GithubOrgClient("google-ish")
            test = access._public_repos_url
            m.assert_called_once()
            self.assertEqual(test, m.return_value["repos_url"])

# what the actual fuck is public repo why did it work
    @patch("test_client.get_json", return_value={"payload": True})
    def test_public_repos(self, mock_get_json):
        """ testing public repos """
        with patch("test_client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "google-ish"}) as m:
            access = GithubOrgClient("google-ish")
            test = access._public_repos_url
            m.assert_called_once()

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False]
    ])
    def test_has_license(self, repo, license_key, expected):
        """ testing has_license """
        test = GithubOrgClient("Google")
        self.assertEqual(test.has_license(repo, license_key), expected)
