Olá! Que bom ver vocês por aqui. Como vocês já dominam a sintaxe básica do C e o conceito de ponteiros, vamos direto ao ponto que torna a Árvore Binária de Busca (BST) uma estrutura tão elegante: a sua propriedade de ordenação e a eficiência da recursão.

---

## Visão Geral

A lógica de busca em uma Árvore Binária de Busca aproveita-se de sua propriedade fundamental: para qualquer nó da árvore, todos os valores na sua subárvore à **esquerda** são menores que o seu próprio valor, e todos os valores na sua subárvore à **direita** são maiores. Portanto, a busca funciona por um processo de eliminação binária. Começamos na raiz: se o valor buscado for igual ao do nó atual, a busca termina; se for menor, ignoramos toda a metade direita e descemos para o ponteiro da esquerda; se for maior, fazemos o oposto. Esse processo se repete recursivamente, reduzindo o espaço de busca pela metade a cada passo (no melhor cenário), até encontrarmos o elemento ou atingirmos um ponteiro nulo.

---

## Código Fonte

Abaixo está a implementação da estrutura do nó e da função recursiva de busca.

```c
#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura do nó da árvore
typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;

// Função recursiva para buscar um valor na BST
Node* searchBST(Node *root, int target) {
    // Caso base: árvore vazia (valor não encontrado) ou valor encontrado na raiz atual
    if (root == NULL || root->data == target) {
        return root;
    }
    
    // Se o valor alvo for menor, busca na subárvore esquerda
    if (target < root->data) {
        return searchBST(root->left, target);
    }
    
    // Se o valor alvo for maior, busca na subárvore direita
    return searchBST(root->right, target);
}

```

---

## Análise do Fluxo de Execução

A beleza desse código está em como a recursividade manipula os ponteiros implicitamente através da pilha de execução (*call stack*):

* **Avanço na Árvore:** Quando a função chama `searchBST(root->left, target)` ou `searchBST(root->right, target)`, nós não estamos modificando a árvore original, mas sim passando o endereço de memória do próximo nó (`struct Node *`) como a nova "raiz" para a próxima instância da função.
* **Condição de Parada (Caso Base):** A recursão se aprofunda linha após linha de nós. Se o ponteiro passado for `NULL`, significa que caminhamos além das folhas da árvore e o valor não existe nela; a função então retorna `NULL`. Se `root->data == target`, o endereço daquele nó específico é retornado.
* **Retorno em Cadeia:** Graças à palavra-chave `return` antes das chamadas recursivas, assim que um caso base é atingido (seja o nó encontrado ou `NULL`), o ponteiro resultante é "passado de volta" linha por linha pelas funções que estavam esperando na pilha, retornando diretamente para quem chamou a função originalmente no topo do programa.