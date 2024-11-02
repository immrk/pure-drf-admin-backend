from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from utils.request_util import get_request_user, get_request_ip, get_request_data, get_request_path, get_os,get_browser, get_verbose_name
import json
from django.contrib.auth.models import AnonymousUser, User
from apps.monitor.models import OperationLog
from uuid import UUID



class ApiLoggingMiddleware(MiddlewareMixin):
    """
    用于记录API访问日志中间件
    """

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.enable = getattr(settings, 'API_LOG_ENABLE', None) or False
        self.methods = getattr(settings, 'API_LOG_METHODS', None) or set()
        self.request_modular = ""

    @classmethod
    def __handle_request(cls, request):
        request.request_ip = get_request_ip(request)
        request.request_data = get_request_data(request)
        request.request_path = get_request_path(request)

    def __handle_response(self, request, response):
        # request_data,request_ip由PermissionInterfaceMiddleware中间件中添加的属性
        body = getattr(request, 'request_data', {})
        # 请求含有password则用*替换掉(暂时先用于所有接口的password请求参数)
        if isinstance(body, dict) and body.get('password', ''):
            body['password'] = '*' * len(body['password'])
        if isinstance(body, dict) and body.get('oldPassword', '') and body.get('newPassword', '') and body.get('newPassword2', ''):
            body['oldPassword'] = '*' * len(body['oldPassword'])
            body['newPassword'] = '*' * len(body['newPassword'])
            body['newPassword2'] = '*' * len(body['newPassword2'])
        if not hasattr(response, 'data') or not isinstance(response.data, dict):
            response.data = {}
        try:
            if not response.data and response.content:
                content = json.loads(response.content.decode())
                response.data = content if isinstance(content, dict) else {}
        except Exception:
            return
        user = get_request_user(request)
        info = {
            'request_ip': getattr(request, 'request_ip', 'unknown'),
            'creator': user if not isinstance(user, AnonymousUser) else None,
            'request_method': request.method,
            'request_path': request.request_path,
            'request_body': self.prepare_json_data(body),
            'response_code': response.status_code,
            'request_os': get_os(request),
            'request_browser': get_browser(request),
            'request_msg': request.session.get('request_msg'),
            'status': response.data.get('success', False) if isinstance(response.data, dict) else False,
            'json_result': self.prepare_json_data(response.data) if response.data else {},
        }
        temp_request_modular = ""
        if not self.request_modular and settings.API_MODEL_MAP.get(request.request_path, None):
            temp_request_modular = settings.API_MODEL_MAP[request.request_path]
        else:
            temp_request_modular = self.request_modular

        operation_log = OperationLog.objects.create(request_modular=temp_request_modular,request_ip=info['request_ip'],creator=info['creator'],request_method=info['request_method'],request_path=info['request_path'],request_body=info['request_body'],response_code=info['response_code'],request_os=info['request_os'],request_browser=info['request_browser'],request_msg=info['request_msg'],status=info['status'],json_result=info['json_result'])

        self.request_modular = ""

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(view_func, 'cls') and hasattr(view_func.cls, 'queryset'):
            if self.enable:
                if self.methods == 'ALL' or request.method in self.methods:
                    self.request_modular = get_verbose_name(view_func.cls.queryset)

        return None
    def process_request(self, request):
        self.__handle_request(request)

    def prepare_json_data(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, UUID):
                    data[key] = str(value)  # 将 UUID 转换为字符串
                elif isinstance(value, dict):
                    self.prepare_json_data(value)  # 递归处理嵌套字典
                elif isinstance(value, list):
                    for i in range(len(value)):
                        if isinstance(value[i], UUID):
                            value[i] = str(value[i])  # 将 UUID 转换为字符串
                        elif isinstance(value[i], dict):
                            self.prepare_json_data(value[i])  # 递归处理嵌套字典

        return data

    def process_response(self, request, response):
        """
        主要请求处理完之后记录
        :param request:
        :param response:
        :return:
        """
        if self.enable:
            if self.methods == 'ALL' or request.method in self.methods:
                self.__handle_response(request, response)

        return response