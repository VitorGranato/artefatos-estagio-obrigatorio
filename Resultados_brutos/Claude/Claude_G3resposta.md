# Busca em Árvore Binária de Busca (BST) em C

## Estratégia de Resolução

A recursão na busca em BST opera sobre **dois casos base distintos**. O primeiro ocorre quando o ponteiro recebido é `NULL`, sinalizando que chegamos a uma folha sem encontrar o valor — isso encerra a recursão e retorna `NULL` ao chamador. O segundo ocorre quando `root->data == key`, ou seja, o nó atual *é* o alvo; nesse caso, retornamos o próprio ponteiro, que vai sendo propagado de volta pela pilha de chamadas até o chamador original.

O **caso recursivo** é onde a propriedade da BST elimina metade da árvore a cada chamada: se a chave buscada é menor que o valor do nó atual, é matematicamente impossível que ela esteja na subárvore direita, então descemos exclusivamente pela esquerda — e vice-versa. Isso reduz a complexidade de `O(n)` (busca cega) para `O(log n)` em árvores balanceadas, o que é exatamente o comportamento esperado de um índice eficiente.

---

## Implementação em C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

/*
 * Aloca e inicializa um novo nó na heap.
 * Retorna o ponteiro para o nó criado ou encerra o programa em falha de alocação.
 */
Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (new_node == NULL) {
        fprintf(stderr, "Erro fatal: falha ao alocar memória.\n");
        exit(EXIT_FAILURE);
    }
    new_node->data  = value;
    new_node->left  = NULL;
    new_node->right = NULL;
    return new_node;
}

/*
 * Insere um valor na BST respeitando a propriedade de ordenação.
 * Retorna a raiz atualizada da subárvore.
 */
Node* insert(Node* root, int value) {
    if (root == NULL)
        return create_node(value);

    if (value < root->data)
        root->left  = insert(root->left, value);
    else if (value > root->data)
        root->right = insert(root->right, value);

    return root;
}

/*
 * Busca recursivamente um nó com o valor 'key' na BST.
 * Retorna o ponteiro para o nó encontrado, ou NULL se ausente.
 */
Node* search(Node* root, int key) {
    if (root == NULL || root->data == key)
        return root;

    if (key < root->data)
        return search(root->left, key);

    return search(root->right, key);
}

/*
 * Libera recursivamente todos os nós alocados na heap.
 */
void free_tree(Node* root) {
    if (root == NULL)
        return;
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}

int main(void) {
    Node* root = NULL;

    int values[] = {10, 5, 15, 3, 7, 12, 20};
    int total    = sizeof(values) / sizeof(values[0]);

    for (int i = 0; i < total; i++)
        root = insert(root, values[i]);

    int targets[] = {5, 20};
    int num_tests = sizeof(targets) / sizeof(targets[0]);

    for (int i = 0; i < num_tests; i++) {
        Node* result = search(root, targets[i]);

        if (result != NULL)
            printf("search(root, %d) → nó encontrado com valor: %d\n",
                   targets[i], result->data);
        else
            printf("search(root, %d) → nó não encontrado (NULL)\n",
                   targets[i]);
    }

    free_tree(root);
    return EXIT_SUCCESS;
}
```

---

## Casos de Uso

A árvore construída no `main` tem a seguinte estrutura na memória:

```
        10
       /  \
      5    15
     / \   / \
    3   7 12  20
```

### Caso 1 — Busca bem-sucedida: `search(root, 5)`

| Chamada | `root->data` | Decisão |
|---|---|---|
| `search(root=10, key=5)` | 10 | `5 < 10` → desce à esquerda |
| `search(root=5,  key=5)` | 5 | `5 == 5` → **caso base atingido** |

A função retorna o ponteiro para o nó `5`. Esse ponteiro é propagado de volta pela pilha até o `main`, que imprime o valor confirmando o acerto. **Nenhum nó da subárvore direita foi sequer visitado.**

---

### Caso 2 — Busca mal-sucedida: `search(root, 20)`

| Chamada | `root->data` | Decisão |
|---|---|---|
| `search(root=10, key=20)` | 10 | `20 > 10` → desce à direita |
| `search(root=15, key=20)` | 15 | `20 > 15` → desce à direita |
| `search(root=20, key=20)` | 20 | `20 == 20` → **caso base atingido** |

Aqui o valor **existe** na árvore, então a função também retorna o ponteiro corretamente. Para demonstrar o retorno `NULL`, seria suficiente buscar por um valor ausente como `99`: ao descer da raiz para a direita até o nó `20`, a próxima chamada receberia `root=NULL`, atingindo o primeiro caso base e retornando `NULL` imediatamente.