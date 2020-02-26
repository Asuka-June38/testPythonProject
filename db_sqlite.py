import sqlite3


def get_some_data():
    data = "that is base data \n"
    data_list = []
    conn = sqlite3.connect('test_database.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fruits WHERE Quantity > 4')
    for row in cursor.fetchall():
        row_str = str(row) + "\n"
        data = data + row_str
    cursor.close()
    conn.close()
    return data
