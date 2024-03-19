from utils import get_db_url, encrypt_db, decrypt_db, overwrite_file_with_random_data
import os

if __name__ == '__main__':
    # check that the db file exists
    db_url = get_db_url()
    encrypted_db_file = db_url[10:] + ".enc"
    print("DB File:", encrypted_db_file)

    if not os.path.exists(encrypted_db_file):
        print(f"DB file does not exist: {encrypted_db_file}")
        exit(1)

    # encrypt the db
    decrypt_db()




    # delete the original db
    os.remove(encrypted_db_file)