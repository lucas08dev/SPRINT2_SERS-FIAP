import matplotlib.pyplot as plt

# Listas para armazenar dados

dias = []
geracoes = []
consumos = []

print("=" * 50)
print("☀️ ECOSOLAR MONITOR")
print("Sistema Inteligente de Monitoramento Solar")
print("=" * 50)

quantidade_dias = int(input("\nQuantos dias deseja analisar? "))

for i in range(quantidade_dias):

    print(f"\n--- DIA {i + 1} ---")

    dia = input("Nome do dia: ")

    radiacao = float(input("Radiação Solar (W/m²): "))
    area = float(input("Área dos painéis (m²): "))
    eficiencia = float(input("Eficiência dos painéis (%): "))
    consumo = float(input("Consumo energético (Wh): "))

    energia_gerada = radiacao * area * (eficiencia / 100)

    dias.append(dia)
    geracoes.append(energia_gerada)
    consumos.append(consumo)

# Estatísticas

total_gerado = sum(geracoes)
total_consumido = sum(consumos)

saldo = total_gerado - total_consumido

indice_sustentabilidade = (
    total_gerado / total_consumido
) * 100

print("\n" + "=" * 50)
print("📊 RELATÓRIO FINAL")
print("=" * 50)

print(f"Energia Total Gerada: {total_gerado:.2f} Wh")
print(f"Consumo Total: {total_consumido:.2f} Wh")
print(f"Saldo Energético: {saldo:.2f} Wh")
print(f"Índice de Sustentabilidade: {indice_sustentabilidade:.2f}%")

# Classificação

if indice_sustentabilidade >= 120:
    classificacao = "Excelente"

elif indice_sustentabilidade >= 100:
    classificacao = "Boa"

elif indice_sustentabilidade >= 80:
    classificacao = "Regular"

else:
    classificacao = "Crítica"

print(f"Classificação: {classificacao}")

# Economia energética

if saldo > 0:
    print("\n✅ O sistema produziu mais energia do que consumiu.")

elif saldo == 0:
    print("\n⚠ Produção igual ao consumo.")

else:
    print("\n❌ O consumo foi maior que a produção.")

# Melhor dia

maior_geracao = max(geracoes)
indice_maior = geracoes.index(maior_geracao)

print(
    f"\n🏆 Melhor dia de geração: "
    f"{dias[indice_maior]}"
)

print(
    f"Energia gerada: "
    f"{maior_geracao:.2f} Wh"
)

# Gráfico

plt.figure(figsize=(10, 5))

plt.plot(
    dias,
    geracoes,
    marker="o",
    label="Energia Gerada"
)

plt.plot(
    dias,
    consumos,
    marker="o",
    label="Consumo"
)

plt.title(
    "Monitoramento de Energia Solar"
)

plt.xlabel("Dias")

plt.ylabel("Energia (Wh)")

plt.legend()

plt.grid(True)

plt.show()

print("\nSistema encerrado.")