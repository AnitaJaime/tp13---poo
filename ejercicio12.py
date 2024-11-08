import tkinter as tk

class VentanaEconomia:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Economía")
        self.root.geometry("400x600") 
        self.root.resizable(False, False) 
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)
        self.crear_botones()
        
    def crear_botones(self):
        temas = [
            "Producto Bruto Interno - PBI",
            "Desempleo",
            "Inflación",
            "Interés Compuesto",
            "Demanda",
            "Oferta",
            "Equilibrio de Mercado",
            "Deuda Pública",
            "Amortización de Préstamos",
            "Índice de Balanza de Pagos",
            "Costo de Oportunidad"
        ]
        
        for i, tema in enumerate(temas):
            color_fondo = "#99ccff" 
            boton = tk.Button(
                self.frame, 
                text=tema, 
                font=("Helvetica", 12), 
                width=25, 
                bg=color_fondo
            )
            boton.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
        boton_salir = tk.Button(
            self.frame,
            text="Salir",
            font=("Helvetica", 12),
            width=25,
            bg="#ff6666",
            command=self.root.quit
        )
        boton_salir.grid(row=len(temas), column=0, padx=10, pady=15, sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaEconomia(root)
    root.mainloop()