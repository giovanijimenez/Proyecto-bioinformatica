#Estoy experimentando con VSCode instalado en windows pero accediendo desde WSL. 
""" la idea de este archivo es crear un codigo que pueda analizar secuencias del gen 
HBB para encontrar la alteracion que provoca la anemia falciforme. Se elige esta enfermedad por ser 
provocada solo por el cambio en una base nitrogenada""" 
# Código generado con asistencia de Claude (Anthropic) y revisado por Hector Armando Garza Balderas utilizando material proporcionado en el Curso de Programación en Python - PER 15903 - Octubre 2025 de UNIR

# Fragmentos de referencia (región del codón 6 del gen HBB)
# Estos son fragmentos cortos reales de la región del exón 1 de HBB.
FRAGMENTO_NORMAL = "CCTGAGGAG"    # ...codón 6 = GAG (normal)
FRAGMENTO_MUTADO = "CCTGTGGAG"   # ...codón 6 = GTG (mutado, causa la enfermedad)


def leer_fasta(ruta_archivo):
    """
    Lee un archivo FASTA muy simple (una sola secuencia) y devuelve
    la secuencia de nucleótidos como un solo string, en mayúsculas.
    """
    secuencia = ""
    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            # Las líneas de encabezado en FASTA empiezan con ">"
            if linea.startswith(">") or linea == "":
                continue
            secuencia += linea.upper()
    return secuencia


def analizar_mutacion(secuencia):
    """
    Busca en la secuencia el fragmento normal o el fragmento mutado.
    Devuelve un mensaje indicando el resultado.
    """
    if FRAGMENTO_MUTADO in secuencia:
        return "🔴 Esta secuencia PRESENTA la mutación de anemia falciforme (GAG -> GTG)."
    elif FRAGMENTO_NORMAL in secuencia:
        return "🟢 Esta secuencia NO tiene la enfermedad (codón 6 normal: GAG)."
    else:
        return "⚠️ No se encontró la región del codón 6 en esta secuencia. Verifica que sea la región correcta del gen HBB."


def analizar_archivo(ruta_archivo):
    """Lee un archivo FASTA y muestra el resultado del análisis."""
    print(f"\nAnalizando archivo: {ruta_archivo}")
    secuencia = leer_fasta(ruta_archivo)
    print(f"Longitud de la secuencia leída: {len(secuencia)} bases")
    resultado = analizar_mutacion(secuencia)
    print(resultado)
    return resultado


def main():
    print("=== Analizador de mutación HBB (Anemia Falciforme) ===")
    print("Este programa analiza una secuencia FASTA del gen HBB")
    print("y determina si presenta la mutación causante de la enfermedad.\n")

    ruta = input("Ruta del archivo FASTA a analizar: ").strip()

    print("\n--- RESULTADO ---")
    analizar_archivo(ruta)

if __name__ == "__main__":
    main()

