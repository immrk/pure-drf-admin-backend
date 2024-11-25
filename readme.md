# drf for prue-admin-thin(puredrf)

## 标准化的DRF(django-restful-framework)RBAC后端项目 为Pure Admin前端开源框架构建

## 该后端项目完全适配于前端项目[immrk/pure-admin-thin](https://github.com/immrk/pure-admin-thin)；该前端项目为[pure admin(thin)](https://github.com/pure-admin/pure-admin-thin)官方项目的fork项目并同步更新，并针对drf后端特性与RBAC需求进行了适配性修改

* 语言环境: python 3.12.1
* 技术框架：django(drf)
* 数据库:  sqlite | mysql
* 缓存数据：redis(option可选项)
* 部署方法：docker
* 自动部署：git actions

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

## 1.3 初始化数据库与数据

### 1.3.1 SQLite数据库

1. 在.env文件中设置`DB_ENGINE`为`sqlite3`, 切换至sqlite数据库引擎
2. 使用已有的迁移文件进行迁移即可`python manage.py migrate`
3. 注意：由于sqllite在删除数据后并不会释放空间，会导致数据文件不断增大，故需要不定时使用`VACUUM指令，释放占用空间，避免文件过大

### 1.3.2 Mysql数据库

1. 在.env文件中设置`DB_ENGINE`为`mysql`, 切换至mysql数据库引擎, 并设置好数据库参数
2. 使用已有的迁移文件进行迁移即可`python manage.py migrate`
3. 将sqlite内数据作为初始化数据导入mysql数据库
   1. 将初始数据生成为json数据 `python manage.py dumpdata > data.json`
   2. 将初始数据导入mysql数据库`python manage.py loaddata ./data.json` 注意：若设置了redis缓存，则需要启动redis服务，否则将报错

## 2.docker部署

环境准备：需要安装 docker、docker compose

注意：若镜像打包系统架构与实际部署架构不一致，则需要采用相同架构系统重新打包或者安装`QEMU`进行架构模拟，否则镜像无法运行 安装命令：`apt install qemu-user-static`

### 2.1 在服务器创建目录存放映射文件与compose文件

docker-compose文件夹内的volums配置项均为映射文件（已经在.dockerignore内进行了过滤，docker内部不包含上述文件）

* 若为相对路径，则需要将compose文件存放在相同目录内；在compose文件所在目录内，使用`docker-compose up -d`即可创建容器并启动 -d 表示后台运行
* 若为绝对路径，可统一管理compose文件，并使用`docker-compose -f your-compose-file.yml up -d`来指定配置文件启动对应的一群docker镜像；

其余指令：

`docker-compose down`: 停止并删除容器

`docker-compose stop`: 仅停止容器，不会删除容器
