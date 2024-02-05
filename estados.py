import pickle

# Clase que representa el estado del programa
class Estado:
    def __init__(self):
        self.counter = 0
        self.message = ""

# Función para guardar el estado del programa
def salvar(state, file):
    with open(file, 'wb') as f:
        pickle.dump(state, f)

# Función para cargar el estado del programa
def cargar(file):
    with open(file, 'rb') as f:
        state = pickle.load(f)
    return state

# Función principal
def main():
    state_file = "program_state.pkl"

    # Intentar cargar el estado del programa desde el archivo
    try:
        state = cargar(state_file)
        print("Estado cargado exitosamente.")
    except FileNotFoundError:
        # Si el archivo no existe, crear un nuevo estado
        state = Estado()
        print("No se encontró un estado previo. Se creará un nuevo estado.")

    # Imprime el contenido del estado cargado
    print("En el archivo se encuentra lo siguiente: \n")
    print(state.counter)
    print(state.message)

    change=int(input("Desea modificar el contenido del estado? 1=sí / 0=no \n"))

    # Modifica el contenido del estado en caso de quererlo
    if(change == 1):
        state.counter = int(input("Digite un numero \n"))
        state.message = input("Agregue un mensaje... \n")
        salvar(state, state_file)
        print("Estado del programa guardado.")


if __name__ == "__main__":
    main()