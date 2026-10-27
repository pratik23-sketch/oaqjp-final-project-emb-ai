
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_empty_input(self):
        self.assertIsNone(emotion_detector(""))

    def test_whitespace_input(self):
        self.assertIsNone(emotion_detector("   "))


if __name__ == "__main__":
    unittest.main()
