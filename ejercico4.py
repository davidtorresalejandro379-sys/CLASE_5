""" Este sistema va atratar sobre la gestion de una lista de invitados """
invitados = ["Daniel", "Pablo", "Yoni"]

def mostrar_menu():
    print("Bienvenidos al gestor de invitados")
    print("seleccione una opcion del menu")
    print("opcion 1 ver la lista completa")
    print("opcion 2 agregar invitados")
    print("opcion 3 eliminar invitados")
    print("opcion 4 salir")

def ver_lista_completa():
    if len(invitados) == 0:
        print("la lista esta vacia")
    else: 
        for invitado in invitados:
            print(invitado)

def agregar_invitados(nombre):
    invitados.append(nombre)
    return "se agrego correctamente"

def eliminar_invitados():
    invitados.pop()
    return "se elimino el ultimo correctamente"

if __name__ == "__main__":
    opcion = 0
    while (opcion != "4"):
        mostrar_menu()
        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            print("la lista de invitados es: ")
            ver_lista_completa()
        elif opcion == "2":
            nombre = input("ingrese el nombre del invitado: ")
            resultado = agregar_invitados(nombre)
            print(resultado)
        
        elif opcion == "3":
            resultado = eliminar_invitados()
            print(resultado)
        else:
            print("hasta luego")
            





    
