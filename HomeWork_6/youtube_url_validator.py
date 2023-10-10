import re


def youtube_url_validator(url):
    match = re.fullmatch(
        r"^(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=([a-zA-Z0-9_]+)|youtu\.be\/([a-zA-Z\d_]+))?(?:-Jec.*)?(?:&.*)?$", url)
    return bool(match)
