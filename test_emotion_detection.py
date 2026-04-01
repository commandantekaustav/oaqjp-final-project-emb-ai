import EmotionDetection.emotion_detection_formatted as emo
import unittest

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        test_data = {   
                    "I am glad this happened":	"joy",
                    "I am really mad about this":	"anger",
                    "I feel disgusted just hearing about this":	"disgust",
                    "I am so sad about this":	"sadness",
                    "I am really afraid that this will happen":	"fear"
                }

        for _ in test_data:
            result_ = emo.emotion_detector(_)['dominant_emotion']
            self.assertEqual(result_, test_data[_])

if __name__ == "__main__":
    unittest.main()