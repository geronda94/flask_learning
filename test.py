from fl_site import DATABASE, connect_db, get_db, FDataBase


db = get_db()
dbase = FDataBase(db)
print(dbase.getMenu())


