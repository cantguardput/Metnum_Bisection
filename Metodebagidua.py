import tkinter as tk

class MetodeBagiDuaApp:
    def __init__(self, root):
        self.root = root
        root.title("Metode Bagi 2")

        self.principal_label = tk.Label(root, text="Jumlah Pokok Investasi:")
        self.principal_label.grid(row=0, column=0)

        self.principal_input = tk.Entry(root, width=20)
        self.principal_input.grid(row=0, column=1)

        self.interest_label = tk.Label(root, text="Tingkat Bunga:")
        self.interest_label.grid(row=1, column=0)

        self.interest_input = tk.Entry(root, width=20)
        self.interest_input.grid(row=1, column=1)

        self.years_label = tk.Label(root, text="Jumlah Tahun:")
        self.years_label.grid(row=2, column=0)

        self.years_input = tk.Entry(root, width=20)
        self.years_input.grid(row=2, column=1)

        self.calculate_button = tk.Button(root, text="Hitung Pertumbuhan Investasi", command=self.calculate_growth)
        self.calculate_button.grid(row=3, column=1)

        self.result_area = tk.Text(root, height=5, width=30, wrap=tk.WORD)
        self.result_area.grid(row=4, column=0, columnspan=2)

    def calculate_growth(self):
        try:
            principal_amount = float(self.principal_input.get())
            interest_rate = float(self.interest_input.get())
            years = int(self.years_input.get())

            result_text = "Pertumbuhan investasi setiap tahun:\n"
            for i in range(1, years + 1):
                principal_amount += principal_amount * (interest_rate / 100)
                result_text += f"Tahun {i}: Jumlah investasi = {principal_amount:.2f}\n"

            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, result_text)
        except ValueError:
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, "Masukkan yang tidak valid. Harap masukkan angka untuk semua input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetodeBagiDuaApp(root)
    root.mainloop()
