import pytest
from url_normalaizer import normalize_image_url


def test_normalize_image_url():
    assert normalize_image_url('https://http.cat/200.jpg', 'example.com') == 'https://http.cat/200.jpg'

    assert normalize_image_url('//http.cat/200.jpg', 'example.com') == 'http://http.cat/200.jpg'

    assert normalize_image_url('/200.jpg', 'example.com') == 'http://example.com/200.jpg'

    assert normalize_image_url('https://example.com/200.jpg', 'example.com') == 'https://example.com/200.jpg'


if __name__ == '__main__':
    pytest.main()
