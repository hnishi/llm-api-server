# https://fastapi.tiangolo.com/how-to/extending-openapi/
# https://github.com/tiangolo/fastapi/issues/1173#issuecomment-605664503

import json

from fastapi.openapi.utils import get_openapi

from main import app

with open("openapi.json", "w") as f:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        f,
    )
