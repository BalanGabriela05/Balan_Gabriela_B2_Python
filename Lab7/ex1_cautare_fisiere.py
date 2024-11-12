import sys # pt a prelua argumentele din linia de comanda
import os # ajuta sa lucram cu directoare si fisierele

def find_files(directory_path, file_extension):

    # verificarea validitații caii directorului
    if not os.path.isdir(directory_path):
        print(f"Eroare: Calea specificata '{directory_path}' nu este un director valid.")
        sys.exit(1)

    # cautarea fisierelor cu extensia specificata
    found_files = []
    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):  # verific extensia
            found_files.append(filename)

    if not found_files:
        print(f"Nu au fost gasite fișiere cu extensia '{file_extension}' in directorul specificat.")
        sys.exit(0)

    # citirea si afisarea continutului fiecarui fisier gasit
    for filename in found_files:
        file_path = os.path.join(directory_path, filename) # construiesc calea completa
        try:
            with open(file_path, 'r') as file: # with open se ocupa de inchiderea fisierului automat -> metoda sigura
                content = file.read()
                print(f"Continutul fisierului '{filename}':\n{content}")
        except Exception as e:
            print(f"Eroare la citirea fisierului '{filename}': {e}")


# preluarea argumentelor din linia de comanda
if len(sys.argv) < 3:
    print("Eroare: Specifica calea directorului si extensia fisierului!")
    sys.exit(1)
else :
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]
    find_files(directory_path, file_extension)


#  python ex1_cautare_fisiere.py ./director .txt