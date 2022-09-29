from pyclbr import Function
EXPECTED_BAKE_TIME= 40 #minutos que tarda en hornearse la lasaña
PREPARATION_TIME= 2 #minutos que tarda cada capa en hacerse
def bake_time_remaining(elapsed_bake_time):      #el tiempo que le queda para terminar de hornear
    return (EXPECTED_BAKE_TIME - elapsed_bake_time) #resta el tiempo que tarda en hornear y el que lleva
def preparation_time_in_minutes (number_of_layers): #
    return number_of_layers * PREPARATION_TIME
def elapsed_time_in_minutes (number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
