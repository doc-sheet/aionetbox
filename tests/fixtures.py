from unittest.mock import AsyncMock
from requests import Response

class ResponseMock(Response):

    json = AsyncMock(return_value={})
    raise_for_status = AsyncMock()
    status = 200
    ok = True
    content_type = '*/*'


class SessionMock(AsyncMock):

    request = AsyncMock(return_value=ResponseMock())
    close = AsyncMock()
