from BayesianNetwork import *

cloudy = Node("Cloudy", [True, False])
sprinkler = Node("Sprinkler", [True, False], [cloudy])
rain = Node("Rain", [True, False], [cloudy])
wet_grass = Node("Wet Grass", [True, False], [sprinkler, rain])

cloudy.add_cpt((), {True: 0.5, False: 0.5})

sprinkler.add_cpt((True,), {True: 0.1, False: 0.9})
sprinkler.add_cpt((False,), {True: 0.5, False: 0.5})

rain.add_cpt((True,), {True: 0.8, False: 0.2})
rain.add_cpt((False,), {True: 0.2, False: 0.8})

wet_grass.add_cpt((True, True), {True: 0.99, False: 0.01})
wet_grass.add_cpt((True, False), {True: 0.9, False: 0.1})
wet_grass.add_cpt((False, True), {True: 0.9, False: 0.1})
wet_grass.add_cpt((False, False), {True: 0.0, False: 1.0})

network = BayesianNetwork([cloudy, sprinkler, rain, wet_grass])

# Cálculo de la probabilidad conjunta de un evento

event = {
    "Cloudy": True,
    "Sprinkler": False,
    "Rain": True,
    "Wet Grass": True
}

#Dada una red bayesiana (según sea la definición de su preferencia), devuelve si esta está completamente descrita (boolean)
print("\n¿Está totalmente descrita?: ",network.isFullyDescribed())
#Dada una red bayesiana (según sea la definición de su preferencia), devuelve la representación compacta de la red bayesiana (string)
print(network.compactForm())
#Dada una red bayesiana (según sea la definición de su preferencia), devuelve los factores de la misma (hash maps / diccionarios / key-value)
print(network.elementsNetwork())
#Dada una red bayesiana (según sea la definición de su preferencia), y una consulta (según sea la definición de su preferencia), devuelve el resultado del algoritmo de enumeración sobre dicha red y dicha consulta(float)
joint_prob = network.joint_probability(event)
print("\nLa probabilidad conjunta del evento es: ", joint_prob,"\n")
