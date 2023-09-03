                        #//////////////////////////////////////#
                        #                                      #
                        ###      CALCULADORA DE DIVISAS    ###    
                        #                                      #
                        #//////////////////////////////////////#



                                              #CALCULADORA DE DIVISAS v0.2.1
"""
Esta aplicación multiplataforma (Windows, Linux, Mac) convierte una cantidad de una moneda en codigo ISO, por ejemplo EUR (euros), en el valor correspondiente en otra divisa, por ejemplo USD (dolares americanos), y opera mediante interfaz alfanumérica en el terminal del sistema operativo :
"""
# ©2023 Calculadora de divisas de Juan Fuente

"""Novedades de la versión 0.2.1
- Integración de un segundo calculo para mostrar al usuario el valor de una unidad de una divisa respecto a su moneda
- Se añade .env para guardar la clave de la API
"""

#Listado de funciones: comprobar_cantidad_moneda (recoge la cantidad de moneda a convertir y evalua la calidad de los datos), comprobar_divisa(recoge las monedas introducidas por el usuario, asegura la calidad de los datos y devuelve separados el nombre y el valor de la moneda. Se usa tanto para obtener la moneda como la divisa.)

""" Datos sobre la API que proporciona los valores de cambios:
Open Exchange Rates: Ofrece una API gratuita y de pago para obtener tasas de cambio en tiempo real. Limitada a 250 llamadas gratuitas. https://exchangeratesapi.io/.
"""


                        #BLOQUE DE IMPORTACIONES
import requests #se necesita requests instalado con pip para hacer llamada a la API de conversion
from decouple import config #importacion para mantener las claves seguras

                        #BLOQUE DE CAPTURA DE DATOS MEDIANTE API
api_key = config("API_KEY")      
url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}" #url que sirve los datos

json_divisas = requests.get(url) #se realiza la llamada a los datos de la url de la api
divisas = json_divisas.json() #se guardan los datos de las conversiones en un archivo json
"""
s -- Se descomenta y se comenta la request a la API para no gastar las llamadas mensuales mientras se hacen pruebas de desarrollo.#DICCIONARIO CON EL LISTADO DE DIVISAS PARA PRUEBAS Y NO GASTAR LAS LLAMADAS A LA API, que tiene llamadas limitadas mensuale
#Para utiliarlo descomentarlo y comentar las 4 lineas anteriores referentes a la llamada a la Api y guardar los datos recibidos

divisas = {'success': True, 'timestamp': 1686316503, 'base': 'EUR', 'date': '2023-06-09', 'rates': {'AED': 3.954746, 'AFN': 92.174953, 'ALL': 105.694703, 'AMD': 
415.806427, 'ANG': 1.939294, 'AOA': 659.488358, 'ARS': 263.747758, 'AUD': 1.59867, 'AWG': 1.938089, 'AZN': 1.88214, 'BAM': 1.955693, 'BBD': 2.172681, 'BDT': 116.493621, 'BGN': 1.955821, 'BHD': 0.405957, 'BIF': 3038.061864, 'BMD': 1.076716, 'BND': 1.446334, 'BOB': 7.435627, 'BRL': 5.278811, 'BSD': 1.076041, 'BTC': 4.0336908e-05, 'BTN': 88.728254, 'BWP': 14.483341, 'BYN': 2.716051, 'BYR': 21103.634453, 'BZD': 2.168981, 'CAD': 1.437653, 'CDF': 2549.663112, 'CHF': 0.970111, 'CLF': 0.030721, 'CLP': 847.688109, 'CNY': 7.677631, 'COP': 4483.725551, 'CRC': 579.270972, 'CUC': 1.076716, 'CUP': 28.532975, 'CVE': 110.263962, 'CZK': 23.674778, 'DJF': 191.591289, 'DKK': 7.450519, 'DOP': 59.03759, 'DZD': 146.73382, 'EGP': 33.330928, 'ERN': 16.150741, 'ETB': 58.536867, 'EUR': 1, 'FJD': 2.391708, 'FKP': 0.858216, 'GBP': 0.85628, 'GEL': 2.81017, 'GGP': 0.858216, 'GHS': 12.159391, 'GIP': 0.858216, 'GMD': 64.011362, 'GNF': 9252.493372, 'GTQ': 8.425539, 'GYD': 227.588595, 'HKD': 8.440086, 'HNL': 26.47955, 'HRK': 7.477083, 'HTG': 150.111781, 'HUF': 368.211064, 'IDR': 15990.902156, 'ILS': 3.87066, 'IMP': 0.858216, 'INR': 88.775781, 'IQD': 1409.622815, 'IRR': 45491.252933, 'ISK': 149.491477, 'JEP': 0.858216, 'JMD': 166.643197, 'JOD': 0.76382, 'JPY': 149.893406, 'KES': 149.802942, 'KGS': 94.298361, 'KHR': 4442.818624, 'KMF': 491.897857, 'KPW': 969.07606, 'KRW': 
1389.512698, 'KWD': 0.33081, 'KYD': 0.896759, 'KZT': 480.370389, 'LAK': 19547.020458, 'LBP': 16151.7906, 'LKR': 319.612499, 'LRD': 184.388113, 'LSL': 20.489417, 'LTL': 3.179263, 'LVL': 0.651295, 'LYD': 5.197715, 'MAD': 10.843357, 'MDL': 19.192038, 'MGA': 4761.761378, 'MKD': 61.516632, 'MMK': 2259.797251, 'MNT': 3732.624381, 'MOP': 8.689965, 'MRO': 384.387442, 'MUR': 48.829441, 'MVR': 16.538239, 'MWK': 1104.544649, 'MXN': 18.64355, 'MYR': 4.967996, 'MZN': 68.102228, 'NAD': 20.285057, 'NGN': 497.818133, 'NIO': 39.357845, 'NOK': 11.625658, 'NPR': 141.966204, 'NZD': 1.756975, 'OMR': 0.414517, 'PAB': 1.076041, 'PEN': 3.932639, 'PGK': 3.818844, 'PHP': 60.331661, 'PKR': 308.835292, 'PLN': 4.451559, 'PYG': 7795.681745, 'QAR': 3.920432, 'RON': 4.956133, 
'RSD': 117.227447, 'RUB': 88.76767, 'RWF': 1220.944486, 'SAR': 4.038179, 'SBD': 8.992057, 'SCR': 14.158592, 'SDG': 646.503877, 'SEK': 11.663053, 'SGD': 1.446272, 'SHP': 1.310094, 'SLE': 24.323726, 'SLL': 21265.141813, 'SOS': 613.198711, 'SRD': 40.425316, 'STD': 22285.84822, 'SVC': 9.415484, 'SYP': 2705.350153, 'SZL': 20.174895, 'THB': 37.231225, 'TJS': 11.75622, 'TMT': 3.768506, 'TND': 3.340513, 'TOP': 2.541375, 'TRY': 25.160808, 'TTD': 7.291635, 'TWD': 33.0975, 'TZS': 2557.200547, 'UAH': 39.741278, 'UGX': 4002.780824, 'USD': 1.076716, 'UYU': 41.937704, 'UZS': 12293.326869, 'VEF': 2871018.449141, 
'VES': 29.958053, 'VND': 25281.292702, 'VUV': 128.704654, 'WST': 2.960564, 'XAF': 655.927176, 'XAG': 0.044423, 'XAU': 0.000548, 'XCD': 2.909879, 'XDR': 0.808956, 'XOF': 655.921085, 'XPF': 119.65572, 'YER': 269.506834, 'ZAR': 20.148437, 'ZMK': 9691.734826, 'ZMW': 21.655915, 'ZWL': 346.702127}}
"""
keys = list(divisas['rates'].keys()) #se cogen los nombres de las divisas y se meten en una lista donde poder comparar si están las elegidas por el usuario

#diccionario de divisas ordenadas alfabeticamente por su nombre en castellano
diccionario_currencies = {
    'Afgani afgano': 'AFN',
    'Baht tailandés': 'THB',
    'Balboa panameño': 'PAB',
    'Birr etíope': 'ETB',
    'Bitcoin': 'BTC',
    'Boliviano boliviano': 'BOB',
    'Cedi ghanés': 'GHS',
    'Chelín keniano': 'KES',
    'Chelín somalí': 'SOS',
    'Colon costarricense': 'CRC',
    'Colón salvadoreño': 'SVC',
    'Corona checa': 'CZK',
    'Corona danesa': 'DKK',
    'Corona islandesa': 'ISK',
    'Corona noruega': 'NOK',
    'Corona sueca': 'SEK',
    'Dalasi gambiano': 'GMD',
    'Denar macedonio': 'MKD',
    'Dinar argelino': 'DZD',
    'Dinar bahreiní': 'BHD',
    'Dinar iraquí': 'IQD',
    'Dinar jordano': 'JOD',
    'Dinar kuwaití': 'KWD',
    'Dinar libio': 'LYD',
    'Dinar serbio': 'RSD',
    'Dinar tunecino': 'TND',
    'Dólar americano': 'USD',
    'Dólar australiano': 'AUD',
    'Dólar beliceño': 'BZD',
    'Dólar canadiense': 'CAD',
    'Dólar de Barbados': 'BBD',
    'Dólar de Bermudas': 'BMD',
    'Dólar de Brunéi': 'BND',
    'Dólar de Fiyi': 'FJD',
    'Dólar de Hong Kong': 'HKD',
    'Dólar de las Islas Salomón': 'SBD',
    'Dólar de las Bahamas': 'BSD',
    'Dólar de Nueva Zelanda': 'NZD',
    'Dólar de Singapur': 'SGD',
    'Dólar guyanés': 'GYD',
    'Dólar jamaiquino': 'JMD',
    'Dólar liberiano': 'LRD',
    'Dólar namibio': 'NAD',
    'Dólar surinamés': 'SRD',
    'Dólar trinitense': 'TTD',
    'Dong vietnamita': 'VND',
    'Escudo caboverdiano': 'CVE',
    'Euro': 'EUR',
    'Florín de Aruba': 'AWG',
    'Florín de las Antillas Neerlandesas': 'ANG',
    'Franco burundés': 'BIF',
    'Franco CFA de África Central': 'XAF',
    'Franco CFA de África Occidental': 'XOF',
    'Franco CFP': 'XPF',
    'Franco comorense': 'KMF',
    'Franco congoleño': 'CDF',
    'Franco guineano': 'GNF',
    'Gourde haitiano': 'HTG',
    'Guaraní paraguayo': 'PYG',
    'Hryvnia ucraniano': 'UAH',
    'Kip laosiano': 'LAK',
    'Kuna croata': 'HRK',
    'Kwacha malauí': 'MWK',
    'Kwacha zambiano': 'ZMW',
    'Kwanza angoleño': 'AOA',
    'Kyat birmano': 'MMK',
    'Lari georgiano': 'GEL',
    'Lek albanés': 'ALL',
    'Lempira hondureño': 'HNL',
    'Leone sierraleonés': 'SLL',
    'Lev búlgaro': 'BGN',
    'Libra egipcia': 'EGP',
    'Libra esterlina': 'GBP',
    'Libra sudanesa': 'SDG',
    'Libra siria': 'SYP',
    'Libra sursudanesa': 'SSP',
    'Lilangeni suazi': 'SZL',
    'Loti lesothense': 'LSL',
    'Manat azerbaiyano': 'AZN',
    'Metical mozambiqueño': 'MZN',
    'Naira nigeriano': 'NGN',
    'Nakfa eritreo': 'ERN',
    'Ngultrum butanés': 'BTN',
    'Ouguiya mauritano': 'MRU',
    'Pataca de Macao': 'MOP',
    'Peso argentino': 'ARS',
    'Peso chileno': 'CLP',
    'Peso colombiano': 'COP',
    'Peso cubano': 'CUP',
    'Peso dominicano': 'DOP',
    'Peso filipino': 'PHP',
    'Peso mexicano': 'MXN',
    'Peso uruguayo': 'UYU',
    'Pula botsuano': 'BWP',
    'Qatar Rial catarí': 'QAR',
    'Quetzal guatemalteco': 'GTQ',
    'Rand sudafricano': 'ZAR',
    'Real brasileño': 'BRL',
    'Renminbi chino': 'CNY',
    'Rial iraní': 'IRR',
    'Rial omaní': 'OMR',
    'Riel camboyano': 'KHR',
    'Ringgit malayo': 'MYR',
    'Rublo bielorruso': 'BYN',
    'Rublo ruso': 'RUB',
    'Rufiyaa maldiva': 'MVR',
    'Rupia de las Seychelles': 'SCR',
    'Rupia india': 'INR',
    'Rupia indonesia': 'IDR',
    'Rupia mauriciana': 'MUR',
    'Rupia nepalesa': 'NPR',
    'Rupia pakistaní': 'PKR',
    'Ryazan ruso': 'AMD',
    'Taka bangladesí': 'BDT',
    'Tenge kazajo': 'KZT',
    'Tugrik mongol': 'MNT',
    'Vatu vanuatuense': 'VUV',
    'Won norcoreano': 'KPW',
    'Won surcoreano': 'KRW',
    'Yen japonés': 'JPY',
    'Yuan chino': 'CNY',
    'Zloty polaco': 'PLN'
}



        #/////////////////////////#
        #// ##   FUNCIONES   ## //#         
        #/////////////////////////#

#Listado de funciones: comprobar_cantidad_moneda (recoge la cantidad de moneda a convertir y evalua la calidad de los datos), comprobar_divisa(recoge las monedas introducidas por el usuario, asegura la calidad de los datos y devuelve separados el nombre y el valor de la moneda. Se usa tanto para obtener la moneda como la divisa.)

#funcion para obtener el dato de cantidad correcto
def comprobar_cantidad_moneda(cantidad_moneda): 
    moneda_correcta = False #variable de control para el bucle
    while not moneda_correcta: #el bucle se ejecuta siempre que la variable sea true
        cantidad_moneda_auxiliar = cantidad_moneda.replace(",", "").replace(".", "")#se eliminan posibles punto o coma para comprobar que sean solo digitos y por lo tanto pueda convertirse a un numero
        try: #iniciamos un try para poder capturar posibles errores
            if cantidad_moneda_auxiliar.isnumeric(): #se comprueba que la variable sea numerica
                cantidad_moneda = float(cantidad_moneda.replace(",", ".")) #se asigna a la variable un numero float valido, con un punto si lo tuviese
                moneda_correcta = True #se convierte la variable a true para cerrar el bucle
            else:
                raise ValueError #se lanza una excepcion si no se ha introducido un numero
        except ValueError:
            print()
            cantidad_moneda = input("Por favor, utilice valores numericos. Introduzca la cantidad nuevamente: ") #Se solicita de nuevo el dato tras notificar el error en la introduccion
            print()
    return cantidad_moneda #se devuelve el valor correcto

#funcion para obtener tanto la moneda como la divisa
def comprobar_divisa():
    divisa_usuario = "" 
    divisa_correcta = False #variable de control para el bucle
    while not divisa_correcta: #el bucle se ejecuta siempre que la variable no sea true
        if divisa_usuario in keys:
            nombre_divisa_usuario = divisas['rates'][divisa_usuario] #se asigna el valor de la divisa a una variable
            divisa_correcta = True #se convierte la variable a true para cerrar el bucle
        
           
        else:
            print()
            divisa_usuario = input("""     
Por favor, introduzca una moneda en formato codigo ISO, por ejemplo EUR.                   
Si desea ver un listado de los codigos ISO de las monedas pulse 1: 
 """).upper() #input para solicitar datos forzados a mayusculas
            print()
        if divisa_usuario == "1": #si el dato introducido en el input es 1 se le muestra un diccionario con los codigos ISO
            print(diccionario_currencies)

            
            
    return (divisa_usuario, nombre_divisa_usuario) #devuelve los valores

## MEJORAR LEGIBILIDAD DE RETORNO POR PANTALLA (MILLARES SEPARADOS POR PUNTOS, DECIMALES POR COMAS) ##
def prettify_number(numero: float):
    
    #Saneamos valores de entrada
    try:
        numero=float(numero)
    except ValueError:
        return str(numero)

    #Pasamos número a cadena para poder trabajar con él
    numero=str(numero)

    #Separamos parte entera de parte decimal
    [n, d]=(numero).split(".")

    #Invertimos la cadena entera
    n=n[::-1]

    #Viajamos por la cadena, insertando un punto cada tres dígitos
    j=0
    m=[]
    for i in n:
        if j==3:
            m.append(".")
            j=1
        else:
            j+=1

        m.append(i)
    #Convertimos la lista en cadena y volvemos a invertir        
    m="".join(m)[::-1]

    #Si es decimal, añadimos coma y parte decimal; si no, nos quedamos solo con la parte entera
    if d!="0":
        m=m+","+d
    
    return m

                        #//////////////////////////////////#
                        #//##  MOTOR DE LA APLICACION  ##//#         
                        #//////////////////////////////////#
def standalone(): 
    #impresion de bienvenida
    print(">")
    print("""Bienvenido a su calculadora de divisas. 

    Introduciendo la CANTIDAD, 
    el codigo de su MONEDA
    y el codigo de la DIVISA a la que la desea convertir,
    obtendrá el valor correspondiente.""")                      

    #variable para controlar el bucle principal
    nueva_operacion = "s" 
    #variable para realizar pruebas e ir imprimiendo datos para control
    debuggin = True

    #se realiza un bucle para controlar que una posible nueva operacion
    while nueva_operacion == "s": #bucle mientras la nueva operacion es un si ("s") a una nueva operacion por parte de usuario
        if nueva_operacion == "n": #si la eleccion del usuario es no (n) se cierra la aplicacion
            print()
            print("Gracias por utilizar su calculadora de divisas.¡Hasta la proxima!") #impresion de despedida
            print()
        else:
            #se solicitan datos de capital al usuario
            print(">")
            cantidad_moneda = comprobar_cantidad_moneda(input("Por favor introduzca la cantidad que desea convertir: ")) #input para recibir el capital del usuario, que inmediatamente es gestionado por la funcion correspondiente
            print()
            print( "Usted ha seleccionado", prettify_number(cantidad_moneda), "como cantidad.") #impresion de confirmación para el usuario
            
            
            #input para recibir el tipo de divisa del usuario
            nombre_divisa_usuario, divisa_usuario = comprobar_divisa() #se pasan datos a dos variables llamando a la funcion
            nombre_moneda_usuario, moneda_usuario = nombre_divisa_usuario, divisa_usuario #se convierten los datos recibidos de la funcion a los necesarios en la primera parte de la formula de calculo de conversion
            
            print()
            print( "Usted ha seleccionado", nombre_moneda_usuario, "como moneda.") #impresion de confirmación para el usuario
        
            
            nombre_divisa_usuario, divisa_usuario = comprobar_divisa() #se pasan datos a dos variables llamando a la funcion, estas dos variables son necesarios en la segunda parte de la formula de calculo de conversion
            
            print()
            print( "Usted ha seleccionado", nombre_divisa_usuario, "como divisa.") #impresion de confirmación para el usuario
            print()
            
            
            
            #se realizan los calculos necesarios
            cambio_divisa = round(cantidad_moneda * (1/divisas['rates'][nombre_moneda_usuario]) * divisas['rates'][nombre_divisa_usuario],5) #se realiza la conversion y se redondea el resultado a 5 decimales
            valor_unidad_divisa = divisas['rates'][nombre_divisa_usuario] / divisas['rates'][nombre_moneda_usuario]#se calcula el valor de una unidad de su moneda a divisa
            valor_unidad_moneda = divisas['rates'][nombre_moneda_usuario] / divisas['rates'][nombre_divisa_usuario]#se calcula el valor de una unidad de la divisa en su moneda
            #FORMULA: Valor de la moneda de destino = Valor de la moneda de origen * (1 / Valor de la moneda de origen respecto al euro) * Valor de la moneda de destino respecto al euro

            
            #se imprime el resultado
            print()
            print("El valor de 1", nombre_moneda_usuario,"es de", prettify_number(valor_unidad_divisa), nombre_divisa_usuario) #impresion de resultado para valor de una sola unidad, con funcion prettify intedrada
            print()
            print("El valor de 1", nombre_divisa_usuario,"es de", prettify_number(valor_unidad_moneda), nombre_moneda_usuario) #impresion de resultado para valor de una sola unidad, con funcion prettify intedrada
            print()
            print("El cambio de", prettify_number(cantidad_moneda), nombre_moneda_usuario,"es de", prettify_number(cambio_divisa), nombre_divisa_usuario) #impresion de resultado para valor de la cantidad solicitada, con funcion prettify intedrada
            print()
            
        
        #se consulta si se desea realizar una nueva operacion  
        nueva_operacion = str(input("Desea realizar una nueva consulta? S/n Teclee s ó n: ")).lower() #input consultando posible nueva operacion o cierre forzado a minusculas para que coincida con el dato almacenado en la variable

        if nueva_operacion == "n": #valor para cierre de la aplicacion
            print()
            print("Gracias por utilizar su calculadora de divisas.¡Hasta la proxima!") #impresion de despedida
            print()
            
if __name__ == "__main__":  #se puede utilizar como componente o utilizarlo por separado
    standalone()
    pass


