import json
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from cld3_neon_plugin import *


class LangDetectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.detector = Pycld3Detector()

    def test_detect(self):
        lang = self.detector.detect("hello young guy")
        self.assertEqual(lang, "en")

    def test_detector_valid_en(self):
        lang = self.detector.cld3_detect("hello young guy")
        self.assertEqual(lang, "en")

    def test_detect_probs(self):
        scores = self.detector.detect_probs("ll trademark and other rights reserved by their respective owners")
        self.assertEqual(list(scores.keys())[0], 'en')
        self.assertIsInstance(list(scores.values())[0], float)

