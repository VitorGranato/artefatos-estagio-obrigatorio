# Busca em Árvore Binária de Busca (BST)

## Visão Geral

A busca em uma BST explora a propriedade fundamental da estrutura: para qualquer nó, todos os valores à esquerda são menores e todos à direita são maiores. A cada chamada recursiva, o algoritmo descarta metade da árvore ao comparar o valor buscado com o nó atual, navegando para a subárvore esquerda se o valor for menor, ou para a direita se for maior — encerrando quando encontra o valor ou atinge um nó `NULL`.

---

## Código Fonte

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *left;
    struct Node *right;
} Node;

Node *create_node(int value) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->value = value;
    node->left  = NULL;
    node->right = NULL;
    return node;
}

Node *insert(Node *root, int value) {
    if (root == NULL) return create_node(value);
    if (value < root->value)
        root->left  = insert(root->left,  value);
    else if (value > root->value)
        root->right = insert(root->right, value);
    return root;
}

Node *search(Node *root, int target) {
    if (root == NULL || root->value == target)
        return root;
    if (target < root->value)
        return search(root->left,  target);
    return search(root->right, target);
}

int main(void) {
    Node *root = NULL;
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(values) / sizeof(values[0]);

    for (int i = 0; i < n; i++)
        root = insert(root, values[i]);

    int target = 40;
    Node *result = search(root, target);

    if (result != NULL)
        printf("Valor %d encontrado no endereço %p.\n", result->value, (void *)result);
    else
        printf("Valor %d não encontrado na árvore.\n", target);

    return 0;
}
```

---

## Análise

A recursividade em `search` opera como uma série de delegações encadeadas ao longo dos ponteiros da árvore. Cada chamada recebe um ponteiro `root` e avalia dois casos-base: `root == NULL`, indicando que o caminho se esgotou sem sucesso, ou `root->value == target`, encerrando com o nó encontrado. Nos casos recursivos, a função não processa nada após a chamada filho — ela simplesmente **propaga o retorno** (`return search(...)`) diretamente à pilha anterior. Isso caracteriza uma **recursão em cauda**, onde o resultado de cada nível é o retorno direto do nível seguinte, sem acumulação de estado intermediário. O ponteiro retornado percorre de volta toda a cadeia de chamadas até `main`, mantendo sua identidade intacta.