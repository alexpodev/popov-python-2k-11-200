from urllib.parse import urlparse, urlunparse


def normalize_image_url(image_url, current_domain):
    parsed_url = urlparse(image_url)

    if not parsed_url.scheme:
        parsed_url = parsed_url._replace(scheme='http')

    if not parsed_url.netloc:
        parsed_url = parsed_url._replace(netloc=current_domain)

    return urlunparse(parsed_url)