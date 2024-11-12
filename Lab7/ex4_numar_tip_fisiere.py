import sys
import os

def count_files_by_extension(directory_path):

    if not os.path.isdir(directory_path):
        print(f"Eroare: Directorul specificat '{directory_path}' nu exista!")
        return

    try:

        files = os.listdir(directory_path) # lista cu numele fis

        if not files : # daca e gol
            print(f"Directorul '{directory_path}' este gol.")
            return

        found_files = {} # dictionar cu extensia fisierului si numarul de fisiere cu acea extensie
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path): # verific daca e un fisier (nu director)
                file_extension = os.path.splitext(file)[1]
                if file_extension not in found_files:
                    found_files[file_extension] = 1
                else:
                    found_files[file_extension] += 1

        if found_files:
            print (f"Numarul de fisiere din directorul '{directory_path}' grupate pe extensii:")
            for extension, count in found_files.items():
                print(f"{extension}: {count}")
        else:
            print(f"Nu au fost gasite fisiere in directorul '{directory_path}'.")

    except PermissionError:
        print("Eroare: Nu ai permisiunea sa accesezi acest director.")
    except Exception as e:
        print(f"A aparut o eroare: {e}")


if len(sys.argv) < 2:
    print("Eroare: Specifica calea directorului!")
else :
    directory = sys.argv[1]
    count_files_by_extension(directory)

# python ex4_numar_tip_fisiere.py ./director