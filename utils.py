import sys
import os

# load an encrypted database
def get_db_url():
    password = os.getenv("DB_PASSWORD", "")
    if password == "":
        print("DB_PASSWORD environment variable not set")
        sys.exit(1)

    # get the path of the file
    # Get the path of the main Python file
    main_file_path = os.path.abspath(__file__)  # Absolute path of the main Python file

    # Define the relative path of the file you want
    relative_file_path = "bcl_encrypted.db"

    # Combine the paths to get the absolute path of the file
    absolute_file_path = os.path.join(os.path.dirname(main_file_path), relative_file_path)

    db_uri = 'sqlite+pysqlcipher://:%s@/%s?cipher=aes-256-cfb&kdf_iter=64000' % (password, absolute_file_path)
    return db_uri