#!/usr/bin/env python3
"""
Tests for the Discord AI Bot components.
"""

import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.providers import ProviderType, ModelInfo
from src.personas import get_persona_prompt, is_jailbreak_persona, is_admin_user


class TestPersonas(unittest.TestCase):
    """Test cases for persona management."""
    
    def test_standard_persona_exists(self):
        """Test that standard persona exists and returns correct prompt."""
        prompt = get_persona_prompt("standard")
        self.assertIsInstance(prompt, str)
        self.assertTrue(len(prompt) > 0)
    
    def test_jailbreak_persona_detection(self):
        """Test detection of jailbreak personas."""
        self.assertTrue(is_jailbreak_persona("jailbreak-v1"))
        self.assertTrue(is_jailbreak_persona("jailbreak-v2"))
        self.assertFalse(is_jailbreak_persona("standard"))
        self.assertFalse(is_jailbreak_persona("creative"))
    
    def test_admin_user_check(self):
        """Test admin user validation."""
        # Without admin users configured, no one should be admin
        self.assertFalse(is_admin_user("123456789"))
        self.assertFalse(is_admin_user(None))


class TestProviders(unittest.TestCase):
    """Test cases for provider management."""
    
    def test_provider_type_enum(self):
        """Test that ProviderType enum has correct values."""
        self.assertEqual(ProviderType.FREE.value, "free")
        self.assertEqual(ProviderType.OPENAI.value, "openai")
        self.assertEqual(ProviderType.CLAUDE.value, "claude")
        self.assertEqual(ProviderType.GEMINI.value, "gemini")
        self.assertEqual(ProviderType.GROK.value, "grok")


class TestModelInfo(unittest.TestCase):
    """Test cases for ModelInfo dataclass."""
    
    def test_model_info_creation(self):
        """Test creation of ModelInfo objects."""
        model = ModelInfo(
            name="test-model",
            provider=ProviderType.FREE,
            description="Test model",
            supports_vision=False,
            supports_image_generation=False
        )
        
        self.assertEqual(model.name, "test-model")
        self.assertEqual(model.provider, ProviderType.FREE)
        self.assertEqual(model.description, "Test model")
        self.assertFalse(model.supports_vision)
        self.assertFalse(model.supports_image_generation)


if __name__ == '__main__':
    unittest.main()