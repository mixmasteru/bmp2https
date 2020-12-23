import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        event = {'pathParameters': {'bucket': 'bmp2https', 'bmpid': '1'}}
        result = index.handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'image/bmp')
        # self.assertIn('Hello World', result['body'])

    def atest_response(self):
        print("testing response.")

        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'image/bmp')
        # self.assertIn('Hello World', result['body'])


if __name__ == '__main__':
    unittest.main()
