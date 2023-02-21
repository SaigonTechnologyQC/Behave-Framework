import copy
from typing import Any


def set_authorization_header_token(context, token) -> None:
    """
    == Description ==
    Set header field with value
    == Arguments ==
    *${token}:* (string) (required) the access token
    """
    set_header(context, "Authorization", 'Bearer {0}'.format(token))


def set_header(context, header_key, header_value) -> None:
    """
    == Description ==
    Set header field with value
    == Arguments ==
    *${header_key}:* (string) (required) the header field
    *${header_value}:* (string) (required) the data value
    """
    headers = copy.copy(context.headers)
    for key in headers.keys():
        context.headers[str(header_key).encode('ascii')] = str(header_value).encode('ascii')

