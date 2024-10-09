import tkinter as tk
import cmath

# Inicjalizacja globalnej zmiennej do wyświetlania instrukcji
initial_instruction = "Enter an equation of the type:\n ax^2 + bx + c"


def validate_input(input_value):
    """Funkcja walidująca dane wejściowe."""
    if input_value == "":
        return True

    if input_value.count('-') > 1:
        return False

    if input_value[0] == '-':
        if len(input_value) > 1 and input_value[1:].replace('.', '', 1).isdigit():
            return True
        elif len(input_value) == 1:
            return True
    else:
        if input_value.replace('.', '', 1).isdigit():
            return True

    return False


def create_input_field(parent, validate_command, variable_name):
    """Funkcja tworząca pole do wprowadzania zmiennej."""
    frame = tk.Frame(parent, bg='white', height=100)  # Usunięta ramka
    frame.pack(fill=tk.X, padx=10, pady=5)

    label_frame = tk.Frame(frame, bg='white')
    label_frame.pack(side=tk.LEFT, expand=True, fill=tk.Y)

    entry_frame = tk.Frame(frame, bg='white')
    entry_frame.pack(side=tk.RIGHT, expand=True, fill=tk.Y)

    label = tk.Label(label_frame, text=f"{variable_name}:", bg='white', font=('Arial', 30))
    label.pack(pady=(15, 0))

    entry = tk.Entry(entry_frame, font=('Arial', 20), validate='key',
                     validatecommand=(validate_command, '%P'))
    entry.pack(pady=20, padx=10)

    return entry


def display_instruction(parent):
    """Funkcja wyświetlająca instrukcję."""
    frame = tk.Frame(parent, bg='white', height=100)
    frame.pack(fill=tk.X, padx=10, pady=5)
    frame.pack_propagate(False)

    instruction_label = tk.Label(frame, text=initial_instruction, bg='white', font=('Arial', 18))  # Czcionka 18
    instruction_label.pack(pady=5)

    return instruction_label  # Zwracamy etykietę instrukcji


def calculate_and_reset(entry_a, entry_b, entry_c, instruction_label):
    """Funkcja odpowiedzialna za obliczenia i resetowanie pól."""
    frame = tk.Frame(root, bg='white', height=100)
    frame.pack(fill=tk.X, padx=10, pady=5)
    frame.pack_propagate(False)

    def calculate():
        """Funkcja obliczająca rozwiązania równania kwadratowego."""
        global initial_instruction  # Używamy globalnej zmiennej

        # Sprawdzanie, czy któreś pole jest puste
        if entry_a.get() == "" or entry_b.get() == "" or entry_c.get() == "":
            instruction_label.config(text="All fields must be filled in!")  # Wyświetlamy komunikat
            return  # Zatrzymujemy dalsze wykonywanie funkcji

        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0 and b != 0 and c != 0:
            outcome = f"Linear equation. x = {-c/b}"
        elif a == 0 and b == 0 and c != 0:
            outcome = "No solutions. Contradictory equation"
        elif a == 0 and b == 0 and c == 0:
            outcome = "Identity equation 0 = 0"

        else:
            delta = pow(b, 2) - 4 * a * c
            sqrt_delta = cmath.sqrt(delta)
            x1 = (-b - sqrt_delta) / (2 * a)
            x2 = (-b + sqrt_delta) / (2 * a)

            if delta == 0:
                outcome = f"One real solution:\n x0 = {round(x1.real, 3)}"
            elif delta > 0:
                outcome = f"Two real solutions:\n x1 = {round(x1.real, 3)}, x2 = {round(x2.real, 3)}"
            else:
                rounded_x1 = complex(round(x1.real, 3), round(x1.imag, 3))
                rounded_x2 = complex(round(x2.real, 3), round(x2.imag, 3))
                outcome = f"Two complex solutions:\n x1 = {rounded_x1}, x2 = {rounded_x2}"

        initial_instruction = outcome  # Ustawiamy globalną zmienną na wynik
        instruction_label.config(text=initial_instruction)  # Wyświetlamy wynik w etykiecie

    def reset():
        """Funkcja resetująca pola i instrukcję."""
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        global initial_instruction
        initial_instruction = "Enter an equation of the type:\n ax^2 + bx + c"  # Resetujemy zmienną
        instruction_label.config(text=initial_instruction)  # Resetujemy etykietę

    # Ustawienia przycisków
    button_frame = tk.Frame(frame, bg='white')
    button_frame.pack(pady=(20, 20))  # Ustawienia marginesu pionowego

    reset_button = tk.Button(button_frame, text="Reset", command=reset, bg='light grey', width=15, height=2)
    reset_button.pack(side=tk.LEFT, padx=(10, 5), pady=(0, 0))  # Ustawiony odstęp pionowy

    calc_button = tk.Button(button_frame, text="Calculate", command=calculate, bg='light grey', width=15, height=2)
    calc_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 0))  # Ustawiony odstęp pionowy


def setup_window():
    """Funkcja konfiguracyjna okna aplikacji."""
    global root
    root = tk.Tk()
    root.title("Quadratic equations calculator")
    root.geometry("800x500")  # Zwiększamy rozmiar okna
    root.configure(bg='lightblue')
    root.resizable(False, False)

    validate_command = root.register(validate_input)

    instruction_label = display_instruction(root)  # Zapisujemy etykietę instrukcji
    entry_a = create_input_field(root, validate_command, 'a')
    entry_b = create_input_field(root, validate_command, 'b')
    entry_c = create_input_field(root, validate_command, 'c')
    calculate_and_reset(entry_a, entry_b, entry_c, instruction_label)  # Przekazujemy etykietę instrukcji

    root.mainloop()


def main():
    """Funkcja główna uruchamiająca aplikację."""
    setup_window()


if __name__ == "__main__":
    main()
