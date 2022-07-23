class alumno:
    # iniciamos atributos del alumno
    def descripcion(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    # imprimimos los atrubutos del alumno
    def imprime(self):
        print (self.nombre)
        print (self.nota)
    # metodo de aprobacion de nota
    def resultado(self):
        if self.nota >= 10:
            print("Este alumno aprobo")
        else:
            print("Este alumno desaprobo")
Alumno = alumno()
# Determinamos los atributos
Alumno.descripcion('Jose', 8)
# Imprimimos los atributos y resultado del alumno
Alumno.imprime()
Alumno.resultado()




