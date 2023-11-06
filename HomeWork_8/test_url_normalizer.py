import pytest
from url_normalaizer import normalize_image_url

@pytest.mark.parametrize(
        "image_url, current_domain, result", 
        [
            ('https://http.cat/200.jpg', 'example.com', 'https://http.cat/200.jpg'),
            ('//http.cat/200.jpg', 'example.com', 'http://http.cat/200.jpg'),
            ('/200.jpg', 'example.com', 'http://example.com/200.jpg'),
            ('https://example.com/200.jpg', 'example.com', 'https://example.com/200.jpg')
        ]
    )
def test_normalize_image_url(image_url, current_domain, result):
    assert normalize_image_url(image_url, current_domain) == result

if __name__ == '__main__':
    pytest.main()
