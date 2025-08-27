quantidade = int(input("Quantos alunos deseja adicionar?: "))

notas = []

for i in range(quantidade):
  nota = float(input(f"Digite a nota do {i+1}º aluno: "))
  notas.append(nota)
  
  aprovados = 0
  reprovados = 0
  soma_notas = 0
  maior_nota = 0
  menor_nota = 0
  
for nota in notas:
  soma_notas += nota
  
  if nota >= 7.0:
    print(f"Nota {nota} -> Aprovado")
    aprovados += 1
  else:
    print(f"Nota {nota} -> Reprovado")
    reprovados += 1
    
  if nota > maior_nota:
    maior_nota = nota
    
    media_turma = soma_notas / len(notas)
    
print("\n--- RESULTADOS ---")
print(f"Total de alunos: {len(notas)}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")
print(f"\nMédia da turma: {media_turma:.2f}")
print(f"Maior nota da turma: {maior_nota}")
print(f"Menor nota da turma: {min(notas)}")

print("\n--- FIM DO PROGRAMA ---")