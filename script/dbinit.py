import environ
import os
from pathlib import Path
import sqlite3
import re
import pymysql


env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# 检测环境文件是否存在以及DB_ENGINE是否存在
if not os.path.exists(os.path.join(BASE_DIR, ".env")):
    print("环境文件不存在")
    exit()
if not env("DB_ENGINE"):
    print("DB_ENGINE不存在")
    exit()

# 判断数据库类型
DB_ENGINE = env("DB_ENGINE")

if DB_ENGINE == "sqlite3":
    # 判断是否存在db.sqlite3文件
    if not os.path.exists(os.path.join(BASE_DIR, "db.sqlite3")):
        # 创建db.sqlite3文件
        open(os.path.join(BASE_DIR, "db.sqlite3"), "w").close()
    # 若存在，询问是否需要删除并重新初始化
    if os.path.exists(os.path.join(BASE_DIR, "db.sqlite3")):
        if input("是否需要删除并重新初始化数据库？(y/n): ") == "y":
            os.remove(os.path.join(BASE_DIR, "db.sqlite3"))
            open(os.path.join(BASE_DIR, "db.sqlite3"), "w").close()
        else:
            print("数据库初始化失败")
            exit()
    
    # 连接数据库
    connection = sqlite3.connect(os.path.join(BASE_DIR, "db.sqlite3"))
    
    # 读取sql文件夹下的所有sql文件并执行
    sql_dir = os.path.join(BASE_DIR, "script", "sql")
    for file in os.listdir(sql_dir):
        print(f"正在处理：{file}")
        with open(os.path.join(sql_dir, file), "r") as f:
            sql_content = f.read()
        
        # 提取创建表的SQL语句
        create_table_match = re.search(r'CREATE TABLE[^;]*;', sql_content, re.DOTALL | re.IGNORECASE)
        insert_data_match = re.search(r'INSERT INTO[^;]*;', sql_content, re.DOTALL | re.IGNORECASE)
        
        # 执行创建表的SQL
        cursor = connection.cursor()
        try:
            if create_table_match:
                # 替换MySQL特有的语法为SQLite兼容语法
                create_sql = create_table_match.group(0)
                
                # 删除ENGINE相关的语句
                create_sql = re.sub(r'ENGINE=.*?;', ';', create_sql)
                
                # 正确处理SQLite的AUTOINCREMENT语法（应该是PRIMARY KEY AUTOINCREMENT）
                create_sql = create_sql.replace('AUTO_INCREMENT', '')
                create_sql = re.sub(r'`id`\s+bigint\s+NOT\s+NULL\s*,', '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,', create_sql)
                create_sql = re.sub(r'`id`\s+INTEGER\s+NOT\s+NULL\s*,', '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,', create_sql)
                create_sql = re.sub(r'`id`\s+int\s+NOT\s+NULL\s*,', '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,', create_sql)
                
                # 替换一些不兼容的数据类型
                create_sql = create_sql.replace('bigint', 'INTEGER')
                create_sql = create_sql.replace('tinyint(1)', 'BOOLEAN')
                create_sql = create_sql.replace('int', 'INTEGER')
                
                # 移除UNIQUE KEY和KEY语句
                create_sql = re.sub(r',\s*UNIQUE KEY\s+`[^`]+`\s+\([^)]+\)', '', create_sql)
                create_sql = re.sub(r',\s*KEY\s+`[^`]+`\s+\([^)]+\)', '', create_sql)
                
                # 移除CONSTRAINT相关内容
                create_sql = re.sub(r',\s*CONSTRAINT.*?REFERENCES.*?\)', '', create_sql)
                
                # 移除PRIMARY KEY语句（因为我们已经在id字段添加了PRIMARY KEY）
                create_sql = re.sub(r',\s*PRIMARY KEY\s+\(`id`\)', '', create_sql)
                
                print(f"执行创建表：{create_sql[:50]}...")
                cursor.execute(create_sql)
                connection.commit()
            
            if insert_data_match:
                insert_sql = insert_data_match.group(0)
                print(f"执行插入数据：{insert_sql[:50]}...")
                cursor.execute(insert_sql)
                connection.commit()
                
        except sqlite3.Error as e:
            print(f"执行SQL出错：{e}")
            continue
        finally:
            cursor.close()
    
    connection.close()
    print("SQLite数据库初始化完成！")
elif DB_ENGINE == "mysql":
    # 检验env内容是否完整
    if not env("DB_NAME"):
        print("DB_NAME不存在，请在.env文件中配置DB_NAME")
        exit()
    if not env("DB_USER"):
        print("DB_USER不存在，请在.env文件中配置DB_USER")
        exit()
    if not env("DB_PASSWORD"):
        print("DB_PASSWORD不存在，请在.env文件中配置DB_PASSWORD")
        exit()
    if not env("DB_HOST"):
        print("DB_HOST不存在，请在.env文件中配置DB_HOST")
        exit()

    # 连接到MySQL数据库
    try:
        connection = pymysql.connect(
            host=env("DB_HOST"),
            user=env("DB_USER"),
            password=env("DB_PASSWORD"),
            database=env("DB_NAME")
        )
        cursor = connection.cursor()

        # 读取sql文件夹下的所有sql文件并执行
        sql_dir = os.path.join(BASE_DIR, "script", "sql")
        for file in os.listdir(sql_dir):
            print(f"正在处理：{file}")
            with open(os.path.join(sql_dir, file), "r") as f:
                sql_content = f.read()
            
            # 执行SQL语句
            try:
                for statement in sql_content.split(';'):
                    if statement.strip():
                        print(f"执行SQL：{statement[:50]}...")
                        cursor.execute(statement)
                connection.commit()
            except pymysql.MySQLError as e:
                print(f"执行SQL出错：{e}")
                connection.rollback()
                continue

        cursor.close()
        connection.close()
        print("MySQL数据库初始化完成！")

    except pymysql.MySQLError as e:
        print(f"连接MySQL数据库出错：{e}")
        exit()

else:
    print("初始化脚本类型目前只支持sqlite3和mysql, 其余类型请自行执行sql文件(文件夹位置：script/sql)")
    exit()







