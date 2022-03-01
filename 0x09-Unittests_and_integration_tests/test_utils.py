#!/usr/bin/env python3
"""Test Utils
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import MagicMock, Mock, patch
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap - class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """test_access_nested_map - test method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """test_access_nested_map_exception - test method"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """TestGetJson - class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, expected: MagicMock) -> None:
        """test_get_json - test method"""
        self.assertEqual(get_json(test_url), expected(test_payload).json())
