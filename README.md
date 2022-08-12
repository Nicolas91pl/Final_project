# Final_project
Project końcowy kursu

# General info
Aplikacja Restowa, której celem jest ułatwienie zarządzania i wyceny uług. Aktualna wersja jest skonfigurowana pod prowadzenie usług koncesjonowanych i obrotu materiałami niebezpiecznymi.
Z racji potrzeby ograniczenia dostępu do aplikacji, brak jest w niej zewnętrznego systemu rejestracji. Należy stworzyć konto admina i tyliko admin zarządza użytkownikami.

# Technologies
Django, Django Rest Fremwork, PosgreSQL

# Instruction
Struktura bazy danych składa się z 5 modeli. Rodzajów Prac (Work_Types), wydatków (Expanses), clientów (Customers), pozwoleń(Licences) i zamówień(Orders).
Relacje między tabelami zachodzą między Licences i Customers (Wiele do Jednego), Customers (jeden do wielu) do Orders (wiele do wielu) Work_Type.
Aplikacja po otrzymaniu poprawnych danych od zalogowanego użytkownika zapisuje je w bazie danych. Wyjątkiem są dwie sytuacje. Pełen CRUD w Work_type oraz Expanses ma tylko admin. Drugi przypadek, to aktualizacja danych w Orders. Funkcja aktualizacji dowolnego elementu wywołuje automatycznie przeliczenie ceny zamówienia.
