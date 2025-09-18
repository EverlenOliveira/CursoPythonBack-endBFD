# analise_turma.py

# Estrutura de dados da turma
alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"},
]

# 1. Filtrar alunos elegíveis: frequência >= 75 e status = "ativo"
elegiveis = filter(
    lambda a: a["frequencia"] >= 75.0 and a["status_matricula"] == "ativo",
    alunos
)

# 2. Aplicar bônus de 10% na nota_final (máximo 10.0)
com_bonus = map(
    lambda a: {**a, "nota_final": min(a["nota_final"] * 1.1, 10.0)},
    elegiveis
)

# 3. Selecionar os alunos destaque (nota_final >= 9.0 após bônus)
destaques = filter(
    lambda a: a["nota_final"] >= 9.0,
    com_bonus
)

# 4. Imprimir os destaques
print("=== Alunos Destaque ===")
for aluno in destaques:
    print(f"{aluno['nome']} - Nota Final: {aluno['nota_final']:.2f}")
