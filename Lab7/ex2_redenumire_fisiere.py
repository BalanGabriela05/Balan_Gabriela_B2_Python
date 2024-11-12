import os
import sys


def rename_files_in_directory(directory_path):
    # verific daca calea specificata este un director valid
    if not os.path.isdir(directory_path):
        print(f"Eroare: Directorul specificat '{directory_path}' nu exista!")
        return

    # lista de fișiere
    # .listdir() -> lista cu numele fisierelor
    # .isfile() -> verifica daca un path este un fisier
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except Exception as e:
        print(f"Eroare la listarea fisierelor din directorul '{directory_path}': {e}")
        return

    # redenumire fisiere
    for index, filename in enumerate(files, start=1): # enumerate() -> returneaza un tuplu cu indexul si valoarea
        file_extension = os.path.splitext(filename)[1]
        new_name = f"file{index}{file_extension}"

        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name)

        try:
            os.rename(old_file_path, new_file_path)
            print(f"Fisierul '{filename}' a fost redenumit in '{new_name}'")
        except Exception as e:
            print(f"Eroare la redenumirea fisierului '{filename}': {e}")



if len(sys.argv) < 2:
    print("Eroare: Specifica calea directorului!")
else:
    directory = sys.argv[1]
    rename_files_in_directory(directory)

# python ex2_redenumire_fisiere.py ./director