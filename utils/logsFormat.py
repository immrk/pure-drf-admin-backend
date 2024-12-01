# -*- coding: utf-8 -*-
import logging
from typing import Dict, Any
import datetime
from pythonjsonlogger import jsonlogger


class JSONFormatter(jsonlogger.JsonFormatter):
    """
    自定义json日志格式
    record 示例
    {
    'name': 'extra_apps.dashboard.views', 'msg': '健康监测', 'args': (), 'levelname': 'INFO', 'levelno': 20,
    'pathname': 'D:\\code\\hz-platform\\backend\\extra_apps\\dashboard\\views.py', 'filename': 'views.py',
    'module': 'views', 'exc_info': None, 'exc_text': None, 'stack_info': None, 'lineno': 294,
    'funcName': 'get', 'created': 1723710044.306112, 'msecs': 306.11205101013184, 'relativeCreated': 84312.62254714966,
    'thread': 11104, 'threadName': 'Thread-25', 'processName': 'MainProcess', 'process': 18764, 'user': None,
    'message': '健康监测', 'asctime': '2024-08-15 16:20:44'
    }
    """
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]) -> None:
        super(JSONFormatter, self).add_fields(log_record, record, message_dict)
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        if not log_record.get('timestamp'):
            now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if not log_record.get('pathname'):
            log_record['pathname'] = record.pathname
        if not log_record.get('lineno'):
            log_record['lineno'] = record.lineno
        if not log_record.get('lineno'):
            log_record['lineno'] = record.lineno
        if not log_record.get('source'):
            log_record['source'] = 'Django'
        if not log_record.get('type'):
            log_record['type'] = 'Django'

#
# {"message": "健康监测", "user": null, "level": "INFO", "timestamp": "2024-08-16T17:04:05.592080Z", "pathname": "/app/backend/extra_apps/dashboard/views.py", "lineno": 294}
# {"message": "Not Found: /prometheus", "status_code": 404, "request": "<WSGIRequest: GET '/prometheus'>", "level": "WARNING", "timestamp": "2024-08-16T17:04:06.552567Z", "pathname": "/usr/local/python3/lib/python3.11/site-packages/django/utils/log.py", "lineno": 241}
#
# {"source": "uwsgi", "type": "server", "time": "1723799286553687", "message": "WARNING 2024-08-16 17:08:06 /usr/local/python3/lib/python3.11/site-packages/django/utils/log.py - line 241: Not Found: /prometheus"}
# {"source": "uwsgi", "type": "server", "time": "1723799283538357", "message": "INFO 2024-08-16 17:08:03 /app/backend/extra_apps/dashboard/views.py - line 294: \\u5065\\u5eb7\\u76d1\\u6d4b"}
#
# {"source": "uwsgi", "type": "request", "method": "GET", "path": "/api/dashboard/health", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36", "duration_in_ms": 5, "referer": "-", "host": "plhz-dev.nioint.com", "time": -, "remote_ip": "10.171.134.206", "lb_trace_id": "10.171.134.206"}
# {"source": "uwsgi", "type": "request", "method": "GET", "path": "/prometheus", "user_agent": "Prometheus/", "duration_in_ms": 2, "referer": "-", "host": "10.133.50.238:8000", "time": -, "remote_ip": "10.133.60.245", "lb_trace_id": "-"}
