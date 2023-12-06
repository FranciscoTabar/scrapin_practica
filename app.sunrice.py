import requests
############# defino los parametros ###############
latitud= -24.5
longitud=-65.5
fecha= "1984-11-26"

############# hago el pedido y lo guardo en una variable ################
respuesta_sunset= requests.get(f"https://api.sunrise-sunset.org/json?lay={latitud}&lng={longitud}&date={fecha}")
datos_sunset=respuesta_sunset.json()

############# imprio los datos que solicite ##############
print(datos_sunset)

################## puedo ver el tipo de dato ##################
type(datos_sunset)

############ como es un diccionario puedo ver su key ################
datos_sunset.keys()

############# puedo ver el estado del pedido #############
sunset_status = datos_sunset["status"]
print(f"status.{sunset_status}")

##### resultado ##########
datos_sunset["results"]

############### puedo ver el contenido por lo que es un diccionario de python############
sunset= datos_sunset["results"]["sunset"]
print(f"El {fecha} el sol se oculto a las {sunset}(UTC-3)")

############## iterar sobre sus claves ############
print("iterando data_sunset['results']:")
for elemento in datos_sunset["results"]:
    print (elemento)

