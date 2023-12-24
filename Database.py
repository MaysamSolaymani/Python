import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.execute('create table test ( id int )')
    db.commit()
    db.execute('insert into test select 1')
    db.commit()
    st = db.execute('select * from test').fetchall()
    db.commit()
    print(st)


if __name__ == '__main__': main()