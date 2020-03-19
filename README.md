#Automação de análise de carteira com Markowitz

##Objetivos
O objetivo deste projeto é realizar uma análise automatizada de carteiras, seguindo a metodologia de análise de portfólio de Markowitz, coletando dados de ações da B3. 
O intuito a princípio é apenas o cálculo de risco e retorno esperado de uma determinada carteira. O cálculo de índices será realizado no futuro.
Os dados históricos foram coletados do Yahoo Finance no dia 19/03/2020.

##Carteira a ser analisada
A carteira a ser analisada consiste em 10 cotações de ações lsitadas na B3:

- BBAS3: Banco do Brasil S.A.
- BBRK3: Brasil Brokers S.A.
- BRML3: BR Malls Participações S.A.
- CMIG3: Cemig Distribuidora S.A.
- GGBR4: Gerdau
- ITSA4: ITAUSA Investimentos
- ITUB4: Itau Unibanco S.A.
- PETR4: Petroleo Brasileiro S.A.
- USIM5: Usiminas S.A.
- VALE3: Vale S.A.

A carteira foi escolhida de maneira aleatória dentro dos papéis em negociação na B3.

##Metodologia
Será analisada a proporção de cada papel na carteira de mínima variância e a combinação desse portfólio de ações com títulos de renda fixa disponíveis de acordo com a metodologia de Markowitz. O retorno esperado das ações será calculado de acordo com o Capital Asset Pricing Model (CAPM) e a sua volatilidade futura a princípio será feita a partir da histórica. Após esse desenvolvimento inicial é esperado um avanço na estimação dessa volatilidade futura especialmente em relação a momentos percebidos de mercado e análise histórica da volatilidade, junto a índices como o VIX.

Em um momento futuro pode ser interessante desenvolver uma função que apresente a carteira ideal a partir de um determinado risco, incluir uma maneira de selecionar dos papéis negociados na B3 sem a necessidade de download dos dados e atualização de valores de maneira automatizada.
