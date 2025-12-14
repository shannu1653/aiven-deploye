import pymysql

pymysql.install_as_MySQLdb()

# 🔧 FIX Django version check
pymysql.version_info = (2, 2, 4, "final", 0)
