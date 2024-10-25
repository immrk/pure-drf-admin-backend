from rest_framework.response import Response
from rest_framework import status


class CustomResponse(Response):
    def __init__(self, success=True, data=None, msg=None, status=status.HTTP_200_OK, template_name=None, headers=None, exception=False, content_type=None, page=1, limit=1, total=1):
        if not data:
            total = 0
        std_data = {"success": success, "data": data, "msg": msg, "page": page, "limit": limit, "total": total}
        super().__init__(std_data, status, template_name, headers, exception, content_type)
