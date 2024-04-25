import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive("example", "zip", root_dir="my_folder")


# Створення TAR.GZ архіву
shutil.make_archive("example", "gztar", root_dir="my_folder")


# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive("example.zip", "destination_folder")
