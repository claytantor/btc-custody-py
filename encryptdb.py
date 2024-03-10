from utils import get_db_url, encrypt_db, decrypt_db
import os

if __name__ == '__main__':
    # check that the db file exists
    db_url = get_db_url()
    print("DB URL:", db_url)
    if not os.path.exists(db_url[10:]):
        print("DB file does not exist")
        exit(1)

    # encrypt the db
    encrypt_db()

    # delete the original db
    os.remove(db_url[10:])
    