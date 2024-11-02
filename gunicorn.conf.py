# gunicorn.conf.py

# 并发工作进程数
workers = 4
# 每个工作进程的线程数
threads = 2
# 绑定的地址和端口
bind = "0.0.0.0:8000"
# 超时时间
timeout = 120
