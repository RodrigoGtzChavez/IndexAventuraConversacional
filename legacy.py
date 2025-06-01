player = input("Nombre?: ")

while True:
    print(f"{player} ¡Despiertas de pronto un dia!")
    print("Estas en medio de la oscuridad total.")
    print("A lo lejos vislumbras lo que parece ser la luz de una Estrella")
    
    
                            #''' DESICIÓN INICIAL '''
#LUZ == si:
    decision_luz = input("¿Quieres acercarte a la luz de la Estrella? (si/no): ").lower()
    if decision_luz == "si":
        print("A medida que te acercas cada vez mas a la luz de la Estrella, eres transportado a un lugar.")
        print("Este lugar es la Entrada a lo que parece ser una colonia desierta")
        print("frente a ti estan los arcos para entrar.")
        colonia = input(f"{player} ¿Deseas seguir adelante  y entrar a la colonia desértica?: si/no: ").lower()
    
        

#COLONIA  == si:  avanzas pero falta algo
        if colonia == "si":
            camino_principal = 1
            print("Entras  y un Relampago ///struck....")
            rayo = True
            print("Reconoces una voz dentro de tu ser que vagamente te hace saber como utilizar EL RAYO")
            print("-------------------------------------------------")              
            print("Distintos lugares, situaciones y sucesos se te hacen ver a lo largo que recorres el lugar...")
            print("mientras mas te adentras tus sentidos detectan hostilidad, activa tu estado de Alerta")
            print("UNA RIÑA DE VECINOS COMIENZA A TU LADO!!!, la vocecilla te insta a hacer algo...")
            primer_pelea = input(f"{player} ¿Qué rayo quieres usar? verde/blanco/rojo/: ").lower()
            match primer_pelea:
                case "verde":
                    print("Tu intuición fue buena pero este color resuelve problemas de salud principalmente")
                    print("los vecinos molestos ahora dirigen su atencion hacia ti")
                    print("Tu segundo instinto es tratar de utilizar el rayo blanco, el cual resuelve pácificamente la disputa")
                    print(".... Desafortunadamente no fuiste lo suficientemente rápido y una botella de cristal lanzada a la deriva se rompe en tu nuca")
                    print("Mueres.")
                    break
                case "blanco":
                    print("decision correcta")
                    
                case "rojo":
                    print("El Rojo es un color destructivo, estas llamas solo encienden mas la destrucción y todo se infulge en Ira")
                    print("Los vecinos sacan sus armas y te atacan")
                    print("Haz muerto. Fin del Juego")
                    break
                case _:
                    print("Nulo")
#COLONIA == no: es el camino correcto,te explica como usar el rayo para mas adelante Ganar el juego
                
        elif colonia == "no":
            print("Un hombre de apariencia majestuosa se te acerca y te lleva a dar un paseo.")
            print("A lo largo del paseo, vislumbras una serie de Lugares, acontecimientos y sucesos...")
            print("El te explica que cada rayo se usa para cada situación distinta.")
            print(" - El rayo verde es Verdad y Salud. El Rayo blanco asciende situaciones discordantes")
            
#LUZ == no:            
    if decision_luz == "no":
        print("Permaneces suspendido, flotando en medio de la oscura y vasta nada.")
        print("Una voz te susurra al oido: Es hora de que sepas utilizar el Rayo.")
        desicion_proposito = input(f"{player} Te gustaria inicializar el Propósito? (si/no): ").lower()

#PROPOSITO == "si" te devuelve al camino correcto en la historia, se repite todo el codigo de arriba
        if desicion_proposito == "si":
            print("La luz de una Estrella te transporta a un lugar.")
            print("Este lugar es la Entrada a lo que parece ser una colonia desierta")
            print("frente a ti estan los arcos para entrar.")
            decision_colonia = input(f"{player} ¿Deseas seguir adelante  y entrar a la colonia desértica?").lower()


# desicion_luz == invalidanswer, bucle        
    else:
        print("Opcion Invalida, vuelve a iniciar")
