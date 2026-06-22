Atue como um Arquiteto de Software Sênior orientando estudantes de graduação que estão no início do curso de Ciência da Computação (ou áreas afins).
Sua tarefa é escrever um código em linguagem C para resolver o problema de buscar um valor específico dentro de uma Árvore Binária de Busca (BST), utilizando obrigatoriamente manipulação de ponteiros e recursividade.

Contexto Adicional:
A busca em árvores binárias é o coração de sistemas de indexação e bancos de dados. A eficiência e a correta manipulação da memória ao transitar pelos nós são críticas para evitar segmentation faults e vazamentos de memória.

Critérios de Qualidade Esperados:

Clareza: A lógica recursiva (caso base e chamadas recursivas) deve ser autoexplicativa pela própria nomenclatura das variáveis e funções.

Completude: O código deve conter a estrutura do nó (struct), a função principal de busca e uma breve função main simulando uma busca bem-sucedida e uma mal-sucedida.

Adequação: O código deve respeitar a propriedade da BST (valores menores à esquerda, maiores à direita) para otimizar as chamadas recursivas, não buscando na árvore inteira cegamente.

Estrutura Obrigatória da Resposta:

Estratégia de Resolução: Explique em dois parágrafos os casos base da recursão utilizados.

Implementação em C: O código fonte completo.

Casos de Uso: Demonstração textual de como o algoritmo se comporta com base no exemplo abaixo.

Restrições e Diretrizes:

Utilize a formatação Markdown, garantindo que o código esteja encapsulado em um bloco de linguagem C.

A função de busca deve ter a assinatura: Node* search(Node* root, int key);.

Mantenha o código limpo e direto. Remova o excesso de comentários linha a linha para não ficar com muita cara de IA; limite-se a documentar o cabeçalho das funções, simulando um ambiente real de engenharia.

Exemplo de Entrada e Saída (Few-Shot):
Considere a seguinte árvore montada na memória:
Raiz (10) -> Esquerda (5), Direita (15)
Entrada 1: search(root, 5)
Saída Esperada 1: A função deve retornar o ponteiro para o nó que contém o valor 5 (navegando uma vez para a esquerda e atingindo o caso base).
Entrada 2: search(root, 20)
Saída Esperada 2: A função deve retornar NULL (navegando para a direita do 15, encontrando um ponteiro vazio e atingindo o caso base nulo).