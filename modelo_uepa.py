class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        return f"Sou um membro da UEPA. Meu nome é: {self.nome}, minha matrícula: {self.matricula}, e o meu email: {self.email}"

class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def verificar_notas(self):
        return f"O aluno {self.nome} está verificando suas notas no curso de {self.curso}."

    def apresentar(self):
        return f"Sou o aluno {self.nome}, matriculado no curso de {self.curso}."

class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def lancar_frequencia(self):
        return f"O professor {self.nome}, do departamento de {self.departamento}, está lançando a frequência."

    def apresentar(self):
        return f"Sou o professor {self.nome}, do departamento de {self.departamento}."


# Área de Testes
if __name__ == "__main__":

    aluno1 = Aluno("Everlen Oliveira", "2025001", "eve.oliveira@uepa.br", "Geoprocessamento")
    professor1 = Professor("Dr. Carlos Silva", "P12345", "carlos.silva@uepa.br", "Engenharia")

    print(aluno1.apresentar())
    print(aluno1.verificar_notas())
    print(professor1.apresentar())
    print(professor1.lancar_frequencia())