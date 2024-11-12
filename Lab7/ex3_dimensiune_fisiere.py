import os
import sys

def calculate_total_size(directory_path):
    total_size = 0

    if not os.path.isdir(directory_path):
        print(f"Eroare: Directorul specificat '{directory_path}' nu exista!")
        return

    # parcurg toate fisierele
    try:
        for root, dirs, files in os.walk(directory_path): # os.walk() -> pt a pargurge si subdirectoarele
            for file in files:
                file_path = os.path.join(root, file)  # calea completa a fișierului
                try:
                    total_size += os.path.getsize(file_path)
                except OSError as e:
                    print(f"Eroare la accesarea fisierului '{file_path}': {e}")
    except Exception as e:
        print(f"Eroare la parcurgerea directorului '{directory_path}': {e}")
        return

    # afisare dimeniune
    print(f"Dimensiunea totala a fisierelor din directorul '{directory_path}' este: {total_size} bytes")


if len(sys.argv) < 2:
    print("Eroare: Specifica calea directorului!")
else:
    directory = sys.argv[1]
    calculate_total_size(directory)

# python ex3_dimensiune_fisiere.py ./director