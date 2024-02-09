import unittest

from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getRatio_returnsPriceADividedByPriceB(self):
        prices_list = [
            {'price_a': 20.53, 'price_b': 50.94},
            {'price_a': 123.4, 'price_b': 50.94},
            {'price_a': 0, 'price_b': 50.94},
        ]

        for prices in prices_list:
            self.assertEqual(prices['price_a'] / prices['price_b'], getRatio(prices['price_a'], prices['price_b']))

    def test_getRatio_doesNotThrowErrorIfBIsZeroAndReturnsNull(self):
        self.assertIsNone(getRatio(234098, 0))


if __name__ == '__main__':
    unittest.main()
