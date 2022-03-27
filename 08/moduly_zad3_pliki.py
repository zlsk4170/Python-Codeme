# Stwórz moduł, który zajmuje się jedynie otwieraniem plików
# - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.

import module_files


def main():
    module_files.save_file()

if __name__ == '__main__':
    main()