import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'JDt5KHrK')
db_address = os.environ.get("MYSQL_ADDRESS", 'sh-cynosdbmysql-grp-a35b490a.sql.tencentcdb.com:24102')
