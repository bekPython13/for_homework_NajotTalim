import psycopg2


db_name = 'shoping'
password = '5760'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(dbname=db_name,
                        password=password,
                        host=host,
                        port=port,
                        user=user)

cur = conn.cursor()

def inser_user():
    u = input('username>')
    # a=int(input('age>'))
    e = input('email>')
    x = (u, e)
    insert_user_query = """ insert into users(username,email)
                                  values (%s,%s);"""
    cur.execute(insert_user_query, x)
    conn.commit()


def get_all():
    select_all_users_query="""select * from users"""
    cur.execute(select_all_users_query)
    row=cur.fetchall()
    print(row)
get_all()