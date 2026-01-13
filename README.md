📊 Análise Estatística de Futebol – Times e Jogadores
📌 Descrição do Projeto

Este projeto tem como objetivo analisar o desempenho individual de jogadores e o desempenho coletivo de times utilizando dados estatísticos extraídos de planilhas do Excel.
A análise combina métricas ofensivas, defensivas e estatísticas avançadas como xG (expected goals), permitindo comparações objetivas baseadas em números.

🧍‍♂️ Análise de Jogadores
📂 Fonte de Dados

A análise individual utiliza 4 arquivos Excel, cada um contendo um conjunto específico de métricas:

Standard.xlsx – informações gerais do jogador (posição, minutos/90s)

Shooting.xlsx – finalizações e xG

Passing.xlsx – passes-chave (KP)

Gca.xlsx – ações que geram chances de gol (SCA)

Esses arquivos seguem o padrão do FBref, com cabeçalhos duplos, que são tratados no código.

📈 Métricas Utilizadas

Para cada jogador são calculadas métricas por 90 minutos, garantindo comparações justas entre atletas com minutagens diferentes:

xG por 90

Chutes por 90

Passes-chave por 90

Ações criadoras de chances (SCA) por 90

Essas métricas são normalizadas usando Min-Max Scaling.

⭐ Índice Ofensivo

Foi criado um Índice Ofensivo autoral, combinando as métricas normalizadas com pesos:

xG: 40%

Chutes: 25%

SCA: 20%

Passes-chave: 15%

Esse índice permite ranquear jogadores ofensivamente e identificar os atletas mais influentes.

📊 Resultados

Geração do Top 10 jogadores ofensivos

Visualização gráfica com ranking horizontal

Filtro mínimo de jogos (90s ≥ 10) para evitar distorções

🏟️ Análise de Times
📂 Fonte de Dados

A análise coletiva considera a tabela final do Brasileirão 2025, contendo:

Jogos disputados

Gols feitos

Gols sofridos

xG

Médias por jogo

📈 Métricas Analisadas

Média de gols feitos por jogo

Média de gols sofridos por jogo

Média de xG por jogo

Comparação entre gols reais e xG

Desvios padrão para identificar dispersão e regularidade

🔍 Objetivos da Análise

Identificar padrões que diferenciam os 4 primeiros colocados

Identificar padrões dos 4 últimos (rebaixados)

Encontrar times que performaram acima ou abaixo do esperado com base no xG

Comparar eficiência ofensiva e consistência defensiva

📌 Principais Conclusões

Times do topo combinam alto xG, boa conversão e defesas sólidas

Times rebaixados apresentam baixo xG e defesas vulneráveis

Alguns times criaram muito (xG alto), mas finalizaram mal

Outros times foram eficientes ofensivamente e escaparam do rebaixamento mesmo com números defensivos ruins

🛠️ Tecnologias Utilizadas

Python 3

Pandas

Matplotlib

Excel (.xlsx)

🎯 Conclusão Geral

O projeto demonstra como estatísticas avançadas permitem análises mais profundas do futebol, indo além do resultado final.
Tanto no nível individual quanto coletivo, métricas como xG e eficiência ofensiva ajudam a explicar desempenhos, identificar padrões e apontar tendências que nem sempre são visíveis apenas pela tabela.
