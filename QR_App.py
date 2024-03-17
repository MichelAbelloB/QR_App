import qrcode
import tkinter as tk
from tkinter import filedialog

class GeneradorQRApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Código QR")

        self.texto_entry = tk.Entry(self, width=40)
        self.texto_entry.pack(pady=10)

        self.generar_button = tk.Button(self, text="Generar Código QR", command=self.generar_qr)
        self.generar_button.pack()

    def generar_qr(self):
        texto = self.texto_entry.get()
        if texto:
            nombre_archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivo PNG", "*.png")])
            if nombre_archivo:
                generar_codigo_qr(texto, nombre_archivo)
                tk.messagebox.showinfo("Éxito", f"Código QR generado exitosamente como {nombre_archivo}")
        else:
            tk.messagebox.showwarning("Advertencia", "Por favor ingresa un texto para generar el código QR.")

def generar_codigo_qr(texto, nombre_archivo):
    codigo_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    codigo_qr.add_data(texto)
    codigo_qr.make(fit=True)
    
    imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")
    
    imagen_qr.save(nombre_archivo)

if __name__ == "__main__":
    app = GeneradorQRApp()
    app.mainloop()
