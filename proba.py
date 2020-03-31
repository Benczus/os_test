from pyhive import hive
  
host_name = "master.hadoop.uni-eszterhazy.hu"
port = 10000
database="retail"
username="senki"

def hiveconnection(host_name, port, database, username):
    conn = hive.Connection(host=host_name, port=port, database=database, username=username)
    cur = conn.cursor()
    cur.execute('SELECT * FROM onlineretail LIMIT 2')
    result = cur.fetchall()
    return result
print(hiveconnection(host_name, port, database, username))

