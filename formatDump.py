#funcion de busqueda
def searchSubStr():
    i = lineaAnterior.find(hora) #guarda la hora
    subStrHora = lineaAnterior[i:i+8]

    j = lineaAnterior.find(ipToSearch) #guarda la IP
    subStrIp = lineaAnterior[j:j+16]
            
    k = line.find('*RPC*') #guarda a partir de RPC
    subStrRPC = line[k:k+200]
    
    lineRFC = subStrRPC #copia la linea con RFC para buscar los BRN

    subStrBRN = lineRFC[-22:-1]
    if subStrBRN.startswith("P") or subStrBRN.startswith("L") or subStrBRN.startswith("M") or subStrBRN.startswith("R"):
        pass
    else:
        subStrBRN = lineRFC[-17:-1]

    #Verifica si algunos de los subStr no tiene espacios
    if ((not subStrHora.strip()) or (not subStrIp.strip()) or (not subStrRPC.strip())):
        pass
    else:
        if subStrRPC.find('BRN100') != -1:
            secondFile.write(subStrIp.rstrip('\n') + " | " + subStrHora.rstrip('\n')+ " | " + subStrRPC.rstrip('\n') + 
            " | " +subStrBRN.rstrip('\n') +  '\n' )

        else:
            secondFile.write(subStrIp.rstrip('\n') + " | " + subStrHora.rstrip('\n')+  " | " + subStrRPC.rstrip('\n') +  '\n' )
    
    subStrRPC = ""
    subStrHora = ""
    subStrIp = ""
    subStrBRN = ""

#Ejecucion del programa  INICIO              
substr = "[" 
ipToSearch = "IP"
lineaAnterior = ""
subStrBRN =""
hora = input("Ingresa la hora: (ejemplo formato 24 hrs '14: o 08:'): ")

#Lee archivo y crea uno adicional para guardar
with open ('listaene5.txt', 'rt') as myfile, open ('dumpOk5ene.txt', 'w') as secondFile : 
    
    for line in myfile:
        
        if line.find(hora) != -1: #si encuentra linea con la hora
            pass
        elif line.find(substr) != -1: #si encuentra la linea que empieza con "["
            searchSubStr() #llama a la funcion de buscar (LOGICA)
            
        lineaAnterior = line
        
