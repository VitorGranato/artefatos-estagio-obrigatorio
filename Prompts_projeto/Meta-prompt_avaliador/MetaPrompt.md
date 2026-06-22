Atue como um Especialista em Garantia de Qualidade de Software e Avaliador Cego de Código. A sua tarefa é analisar criticamente a "Resposta Submetida" fornecida no final deste prompt. Essa resposta foi gerada por uma Inteligência Artificial em resposta a um desafio de programação: implementar uma busca por um valor específico numa Árvore Binária de Busca (BST) em linguagem C, utilizando obrigatoriamente ponteiros e recursividade.

Avalie a resposta com base estrita nos 4 critérios abaixo, atribuindo uma pontuação inteira de 1 a 5 para cada um deles.

CRITÉRIOS DE AVALIAÇÃO:

1. Precisão Técnica (P): O código está logicamente correto? Trata os casos base da recursão (árvore vazia/nó não encontrado e valor encontrado)? Manipula os ponteiros corretamente sem riscos de falhas de segmentação (segmentation faults)? Otimiza a busca respeitando as propriedades de uma BST (ir para a esquerda se menor, direita se maior) em vez de fazer uma busca cega?
2. Clareza e Legibilidade (C):A explicação teórica e o código possuem uma linguagem didática e de fácil compreensão para estudantes de graduação que estão no início do curso (cursando as primeiras disciplinas de algoritmos e estruturas de dados)? A nomenclatura de variáveis e funções é intuitiva e adequada para o padrão da linguagem C?
3. Completude (Co): A resposta entregou todos os elementos necessários para a correta compreensão e funcionamento do algoritmo? (Ex: definição da estrutura do nó 'struct', a função de busca e uma função 'main' com exemplos de teste)?
4. Aderência e Limpeza (A): O código está limpo e bem formatado? A resposta obedeceu à restrição de evitar o excesso de comentários linha a linha, mantendo um aspeto profissional e fluido (sem parecer um texto artificialmente gerado)?

ESCALA DE PONTUAÇÃO (Aplique rigorosamente a cada critério):
- 5 (Plenamente Satisfatório): Excelente. Sem erros lógicos ou de formatação; cumpre o critério de forma profissional e exemplar.
- 4 (Bom): Atende muito bem ao critério, apresentando apenas falhas mínimas de estilo ou pequenos comentários redundantes que não afetam a qualidade geral.
- 3 (Regular): O código é funcional, mas possui pontos evidentes de melhoria na lógica, na estrutura ou apresenta excesso de texto desnecessário.
- 2 (Insuficiente): Apresenta erros claros de lógica, má estruturação, omissão de elementos importantes ou código excessivamente poluído.
- 1 (Inaceitável): O código possui erros graves que impedem a compilação, lógica totalmente errada, violação das restrições ou a resposta está fora do escopo.

RESTRIÇÕES DE SAÍDA:
- Responda EXCLUSIVAMENTE utilizando o formato JSON abaixo. 
- Não inclua nenhuma introdução, saudação, notas de rodapé ou texto explicativo fora do bloco JSON.
- Forneça uma justificativa textual detalhada e objetiva para cada nota atribuída.
- NÃO calcule nenhuma nota final ou média. Limite-se a extrair as pontuações individuais.

FORMATO DE SAÍDA OBRIGATÓRIO:
{
  "pontuacao_precisao": [Número de 1 a 5],
  "justificativa_precisao": "[Escreva aqui a sua justificativa técnica]",
  "pontuacao_clareza": [Número de 1 a 5],
  "justificativa_clareza": "[Escreva aqui a sua justificativa técnica]",
  "pontuacao_completude": [Número de 1 a 5],
  "justificativa_completude": "[Escreva aqui a sua justificativa técnica]",
  "pontuacao_aderencia": [Número de 1 a 5],
  "justificativa_aderencia": "[Escreva aqui a sua justificativa técnica]"
}

RESPOSTA SUBMETIDA PARA AVALIAÇÃO:
[INSERIR AQUI O TEXTO INTEGRAL DA RESPOSTA DO MODELO G1, G2 OU G3]