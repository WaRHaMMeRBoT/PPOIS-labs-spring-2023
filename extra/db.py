import sqlite3


def get_data(songs):
    db = None

    try:
        db = sqlite3.connect('db/songs.db')
        cursor = db.cursor()

        select_query = " SELECT * from songs where songs=?"
        cursor.execute(select_query, (songs,))

        data = cursor.fetchall()

        for i in data:
            print(i)

        db.close()
        print("Connection closed")
        return data

    except sqlite3.Error as err:
        print(f'Error: "{err}"')

    finally:
        if db:
            db.close()
            print("Connection closed")
