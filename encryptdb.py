from utils import get_db_url, encrypt_db, decrypt_db, overwrite_file_with_random_data
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

    # overwrite the original decrypted db with random data
    overwrite_file_with_random_data(db_url[10:])

    # delete the original db
    os.remove(db_url[10:])
    