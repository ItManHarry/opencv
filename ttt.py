import pymssql
def get_connection():
    connection = pymssql.connect(server='10.40.128.111:1433',
                              user='plc',
                              password='plc',
                              database='inPTLDB')
    return connection
def get_all():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        if cursor:
            print('PTL数据库MS SQLServer连接成功......')
        else:
            print('PTL数据库MS SQLServer连接失败......')
        cursor.execute('''
            select * from master_wagon
        ''')
        for row in cursor:
            print(row)
    except:
        print('Connection error...')
get_all()