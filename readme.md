# drf for prue-admin-thin(for drf)

已使用技术：python 3.12.1 // django // drf // sqlite // redis // docker

## 1.项目初始化

### 1.1 安装依赖：

`pip install -r requirements.txt`

更新依赖文件：`pip freeze > requirements.txt`

### 1.2 Redis缓存

项目使用redis提供服务端缓存服务(默认缓存路径为本地redis服务 `redis://127.0.0.1:6379/1`)

本地开发需先启动redis服务（也可不指定配置文件）：

windows：

[redis windows github](https://github.com/tporadowski/redis/releases) 下载解压到任意位置

命令行到达解压路径后，运行 `redis-server.exe redis.windows.conf`；

macos：

通过homebrew安装即可 `brew install redis `

前往安装路径

`./redis-server ../redis.conf`；

## 1.3 初始化数据库

使用已有的迁移文件进行迁移即可

`python manage.py migrate`

由于sqllite在删除数据后并不会释放空间，会导致数据文件不断增大，故需要不定时使用

`VACUUM`

指令，释放占用空间，避免文件过大
