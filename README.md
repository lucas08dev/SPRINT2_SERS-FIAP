☀️ EcoSolar Monitor

📌 Sobre o Projeto

O EcoSolar Monitor é um sistema desenvolvido em Python com o objetivo de simular o monitoramento de uma instalação de energia solar.

A aplicação permite registrar dados de operação durante vários dias, calcular a energia gerada pelos painéis solares, comparar a produção com o consumo energético e gerar indicadores de sustentabilidade.

O projeto foi desenvolvido como uma Prova de Conceito (PoC) para demonstrar a viabilidade técnica de soluções voltadas para energias renováveis e eficiência energética.

🎯 Objetivos
Simular a geração de energia solar.
Monitorar o consumo energético.
Calcular indicadores de sustentabilidade.
Identificar períodos de maior eficiência energética.
Demonstrar a aplicação prática de conceitos de energia renovável.
🌱 Sustentabilidade e Energias Renováveis

A energia solar é uma das principais fontes de energia limpa disponíveis atualmente.

O EcoSolar Monitor busca demonstrar como sistemas computacionais podem auxiliar no monitoramento da geração de energia renovável, contribuindo para:

Redução do consumo de fontes não renováveis.
Melhor aproveitamento da energia produzida.
Tomada de decisões baseada em dados.
Incentivo ao uso de tecnologias sustentáveis.
⚙️ Funcionalidades
Cadastro de Dados

O usuário informa:

Nome do dia analisado
Radiação solar (W/m²)
Área dos painéis solares (m²)
Eficiência dos painéis (%)
Consumo energético (Wh)
Processamento

O sistema realiza automaticamente:

Cálculo da energia gerada
Comparação entre geração e consumo
Cálculo do saldo energético
Cálculo do índice de sustentabilidade
Relatórios

O sistema exibe:

Energia total gerada
Consumo total
Saldo energético
Classificação de sustentabilidade
Melhor dia de geração
Visualização Gráfica

O sistema gera gráficos comparando:

Energia gerada
Consumo energético
🏗️ Arquitetura da Solução

Fluxo do sistema:

Sensores Simulados
↓
Coleta de Dados
↓
Processamento em Python
↓
Cálculo de Indicadores
↓
Relatório Final
↓
Visualização Gráfica

🧮 Fórmula Utilizada

Energia Gerada = Radiação Solar × Área dos Painéis × Eficiência

Onde:

Radiação Solar = W/m²
Área = m²
Eficiência = percentual de aproveitamento dos painéis
💻 Tecnologias Utilizadas
Python 3
Matplotlib
GitHub
📊 Exemplo de Uso

Entrada:

Dia: Segunda
Radiação: 900
Área: 10
Eficiência: 22
Consumo: 1700

Saída:

Energia Gerada: 1980 Wh
Saldo Energético: +280 Wh
Classificação: Boa

🚀 Como Executar
Instalar dependências

pip install matplotlib

Executar o projeto

python energywatch.py

📈 Resultados Esperados

O sistema permite avaliar a eficiência de uma instalação solar simulada, fornecendo informações importantes para o acompanhamento da produção energética e da sustentabilidade do sistema.
