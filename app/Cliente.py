class Cliente:
    padron = 0

    def __init__(self, padron, nombre, apellido, email, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.padron = padron
        self.email = email
        self.contrasenia = contrasenia

    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getPadron(self):
        return self.padron

    def getEmail(self):
        return self.apellido

    def getContrasenia(self):
        return self.contrasenia

    
    @classmethod
    def getNuevoPadron(cls):
        cls.padron += 1
        return cls.padron 