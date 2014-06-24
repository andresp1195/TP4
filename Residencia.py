##import mechanize #Para descargarlo: https://pypi.python.org/pypi/mechanize/
apartas=[]
archi=open('Apartas.txt','a+')
archi.close()

def grabar(hecho):
        archi=open('Apartas.txt','a')
        archi.write(hecho+"\n")
        archi.close()
        
def leertxt():
    global apartas
    archi=open('Apartas.txt','r')
    linea=archi.readline()
    print(linea)
    while linea!="":
        lista=linea.split(";")
        apartas.append(lista)
        print(apartas)
        linea=archi.readline()
    archi.close()

## Clase Apartamento 
class Residencia(object):
    global apartas
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max):

            if type(self) is Residencia:
                raise Exception('Error: Acceso denegado')
            else:         
                self.precio_min=precio_min
                self.precio_max=precio_max
                self.publicarAparta(titulo,descripcion+'Es un apartamento',TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono)
    ##Consiste en la funcion que publica Apartamentos, Casas y Habitaciones para el alquiler.
    def publicarAparta(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono):
            
                self.titulo=titulo
                self.descripcion=descripcion
                self.TV=TV
                self.luz=luz
                self.agua=agua
                self.internet=internet
                self.num_cuartos=num_cuartos
                self.cochera=cochera
                self.ubicacion=ubicacion
                self.precio=precio
                self.correo=correo
                self.telefono=telefono
                self.alimentacion=alimentacion
                self.amueblado=amueblado        
                global apartas
                paraGrabar=''
                if self.verificarAparta(titulo)==False and telefono.isdigit() and precio.isdigit():
                    paraGrabar=self.titulo+';'+self.descripcion+';'+str(self.TV)+';'+str(self.luz)+';'+str(self.agua)+';'+str(self.internet)+';'+str(self.num_cuartos)+';'+str(self.cochera)+';'+str(self.alimentacion)+';'+str(self.amueblado)+';'+str(self.ubicacion)+';'+str(self.precio)+';'+str(self.correo)+';'+str(self.telefono)
                    grabar(paraGrabar)
                    paraGrabar=paraGrabar.split(';')
                    apartas.append(paraGrabar)            
                                
                else:
                    return "Error: Datos invalidos o apartamento existente."

    ##Las posiciones para esta funcion son: TV,luz,agua,internet,num_cuartos,cochera,ubicacion,precio
    def consultarAparta(self,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,precio_min,precio_max):
        self.TV=TV
        self.luz=luz
        self.agua=agua
        self.internet=internet
        self.num_cuartos=num_cuartos
        self.cochera=cochera
        self.precio_min=precio_min
        self.precio_max=precio_max
        self.alimentacion=alimentacion
        self.amueblado=amueblado
        global apartas
        listaActual=[TV,luz,agua,internet,cochera,alimentacion,amueblado,num_cuartos,precio_min,precio_max]
        cont=0
        while cont<len(apartas):
            for each in apartas:
                if ((listaActual[0]=="True" and each[2]=="True") or (listaActual[0]=="False")) and ((listaActual[1]=="True" and each[3]=="True") or (listaActual[1]=="False")) and ((listaActual[2]=="True" and each[4]=="True") or (listaActual[2]=="False")) and ((listaActual[3]=="True" and each[5]=="True") or (listaActual[3]=="False")) and ((listaActual[4]=="True" and each[7]=="True") or (listaActual[4]=="False")) and ((listaActual[5]=="True" and each[8]=="True")or(listaActual[5]=="False")) and ((listaActual[6]=="True" and each[9]=="True") or (listaActual[6]=="True"))and(listaActual[7]==each[6])and(each[8]<=listaActual[11]<=each[9]):
                     return each
                     cont+=1
                else:
                     cont+=1

    ##Retorna True si la residencia que se desea ingresar ya existe.    
    def verificarAparta(self,titulo):
        self.titulo=titulo
        global apartas
        contAp=0
        while contAp<len(apartas):
            if apartas[contAp][0]==self.titulo:
                return True
            else:
                contAp+=1
        return False



class Casa(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max):
        Residencia.__init__(self,titulo,descripcion+'. Casa de habitacion.',TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max)
class Habitacion(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max):
        Residencia.__init__(self,titulo,descripcion+'. Habitacion',TV,luz,agua,internet,'1',cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max)

class Apartamento(Residencia):
    def __init__(self,titulo,descripcion,TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max):
        Residencia.__init__(self,titulo,descripcion+'. Apartamento.',TV,luz,agua,internet,num_cuartos,cochera,alimentacion,amueblado,ubicacion,precio,correo,telefono,precio_min,precio_max)

leertxt()          
##casa=Casa('hola','lindo cercano al TEC, con vista al mar','True','False','False','False','1','True','False','True','Norte de la sonny','1234567890','hola@hotmail.com','25913510','21358907','12345678901')
##hab=Habitacion('beibi','lindap cercana al TEC, con vista al Estadio Fello Meza Ivancovich','True','True','False','True','3','True','False','False','Sur de la sonny','12345','adios@gmail.com','259','21358','123')
##apartas2=Apartamento('beibi','lindo apartamento cercano al TEC, con vista al Estadio Fello Meza Ivancovich','True','True','False','True','3','True','False','False','Sur de la sonny','12345','adios@gmail.com','259','21358','123')
##apartas3=Apartamento('pequeno','lindo apartamento cercano al TEC, con vista al Estadio Fello Meza Ivancovich','True','True','False','True','3','True','False','False','Sur de la sonny','12345','adios@gmail.com','259','21358','123')



