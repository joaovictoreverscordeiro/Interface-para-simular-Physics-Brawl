# Recomendações para preenchimento do Excel
### Caso alguma dessas recomendações não sejam seguidas, o código dará erro

1. Todas os itens inseridos na tabela devem ser numéricos (número da questão, número de tentativas, resposta numérica)

2. A coluna 'quest' se refere ao número da questão
  3. Questões normais são numeradas com 1, 2, 3...; 
  4. Questões especiais (M.1, M.2... X.1, X.2... E.1, E.2...) deverão
	     ser colocadas na coluna 'quest' com o número na série (o número na série de M.1 é 1) seguido da posição da letra
	     no alfabeto; ex: M é a 13ª letra no alfabeto, então M.1=113. Caso a posição seja menor que 10, adicione um zero
	     antes do número; ex: A.3=301

5. A coluna 'scorei' é a pontuação inicial da questão e deve ser preenchida de acordo com o arquivo da prova passada. As 
   pontuações devem ir de 3 até 9. (caso em anos antigos aconteça de não ir, pode me avisar que eu adapto o código pra funcionar)

6. A coluna 'resp' deve ser preenchida com a resposta numérica de cada questão.
   Casas decimais devem ser representadas com pontos!! ex: 3,20 vai fazer o código travar, 3.20 não;
  7. Na Physics Brawl o número de algarismos significativos importa bastante então as respostas devem ser inseridas olhando
	     pra isso;
  8. Notação científica é representada usando "e". ex: 3.10*10^4 = 3.10e4. "*" é multiplicação.


As colunas já estão criadas no Excel, o texto que já tá inserido não pode ser alterado.
