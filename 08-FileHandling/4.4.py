def display_in_chunks(filename, first_n=5):
    try:
        with open(filename, 'r') as file:
            # 1) Wydrukuj pierwsze first_n linii od razu
            for _ in range(first_n):
                line = file.readline()
                if not line:
                    print("Koniec pliku.")
                    return
                print(line, end="")   # end="" usuwa dodatkowy pusty wiersz

            # 2) Dalej: jedna linia na Enter
            for line in file:
                input("Press Enter key...")
                print(line, end="")

            print("\nKoniec pliku.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Wywołanie:
display_in_chunks('it_company.csv')