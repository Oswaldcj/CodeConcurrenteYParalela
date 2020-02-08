#programa que abre un archivo, lee el texto y cuenta vocales, mayusculas, miusculas, espacios , etc.
import shutil, os

copia = "/home/zentinel/Documents/Programacion Concurrente y Paralela/CodeGit"

class Archivo:
    def __init__(self, nombre):
        try:
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            print('No se puede abrir el archivo ',nombre)
            exit()

    def muestra(self):
        i = 1
        for linea in self.f:
            print("{:3}, {}".format(i, linea))
            i+=1
        self.f.seek(0)

    def cuentaVocales(self):
        def vocales(s):
            contador = 0
            for i in range(len(s)):
                if s[i].lower() in set("aeiouáéíóú"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += vocales(linea)
        self.f.seek(0)
        return contador

    def cuentaConsonantes(self):
        def consonantes(s):
            contador = 0
            for i in range(len(s)):
                if s[i].lower() in set("bcdfghjklmnpqrstvwxyz"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += consonantes(linea)
        self.f.seek(0)
        return contador
    
    def cuentaMayusculas(self):
        def mayusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("AÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += mayusculas(linea)
        self.f.seek(0)
        return contador

    def cuentaMinusculas(self):
        def minusculas(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set("aeiouáéíóúbcdfghjklmnpqrstvwxyz"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += minusculas(linea)
        self.f.seek(0)
        return contador

    def cuentaEspacios(self):
        def espacios(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(" "):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += espacios(linea)
        self.f.seek(0)
        return contador

    def cuentaPalabras(self):
        text = self.f.read()
        pal = text.split()
        i = 0
        while i < len(pal):
            palabra=pal[i]
            if palabra == 'Fin':
                break
            i+=1
        return i

    def cuentaSignos(self):
        def signos(s):
            contador = 0
            for i in range(len(s)):
                if s[i] in set(".,;:¿?¡!"):
                    contador += 1
            return contador
        contador = 0
        for linea in self.f:
            contador += signos(linea)
        self.f.seek(0)
        return contador
    
    def copiaArchivo(self, nombreCopia):
        shutil.copy(self.f.name, nombreCopia)

    def copiaMinus(self):
        msm = self.f.read()
        print("Mensaje en minusculas:\n",msm.lower())
        self.f.seek(0)

    def copiaMayus(self):
        msm = self.f.read()
        print("Mensaje en mayusculas:\n",msm.upper())
        self.f.seek(0)

    def cuentaLineas(self):
        contador = 0
        for linea in self.f:
            contador += 1
        self.f.seek(0)
        return contador
    
    def toHex(self):
        lt = []
        def th(s):
            for i in range(len(s)):
                lt.append(hex(ord(s[i])))

        for linea in self.f:
            th(linea)
        print(lt)
        self.f.seek(0)

if __name__ == '__main__':
    nob = input('que archivo deseas abrir?\n')
    arc = Archivo('/home/zentinel/Documents/Programacion Concurrente y Paralela/CodeGit/'+nob)
    arc.muestra()
    print('el texto tiene:', arc.cuentaVocales(), 'vocales')
    print('el texto tiene:', arc.cuentaConsonantes(), 'consonantes')
    print('el texto tiene:', arc.cuentaSignos(), 'signos de puntuacion')
    print('el texto tiene:', arc.cuentaEspacios(), 'espacios')
    print('el texto tiene:', arc.cuentaPalabras(), 'palabras')
    print('el texto tiene:', arc.cuentaLineas(), 'lineas')
    print('el texto tiene:', arc.cuentaMayusculas(), 'mayusculas')
    print('el texto tiene:', arc.cuentaMinusculas(), 'minusculas')
    print('el archvio ha sido copado', arc.copiaArchivo("textoCopia.txt"))
    arc.copiaMayus()
    arc.copiaMinus()
    arc.toHex()
