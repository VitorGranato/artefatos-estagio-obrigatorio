## Estratégia de Resolução

Em uma Árvore Binária de Busca (BST), cada nó obedece à propriedade: valores menores ficam na subárvore esquerda e valores maiores ficam na subárvore direita. Essa característica permite que a busca seja muito eficiente, pois não é necessário percorrer toda a árvore. A cada chamada recursiva, o algoritmo compara a chave procurada (`key`) com o valor armazenado no nó atual. Dependendo do resultado, ele segue apenas para a subárvore que pode conter o valor desejado.

A recursão possui dois casos base. O primeiro ocorre quando o ponteiro recebido é `NULL`, indicando que o caminho de busca chegou ao fim sem encontrar o valor; nesse caso, a função retorna `NULL`. O segundo ocorre quando o valor do nó atual é igual à chave procurada; nesse momento, a função retorna o ponteiro para o nó encontrado. Caso nenhum desses casos base seja atingido, a função realiza uma chamada recursiva para a esquerda ou para a direita, respeitando a propriedade da BST.

---

## Implementação em C

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *left;
    struct Node *right;
} Node;

/* Cria um novo nó da BST */
Node* createNode(int value) {
    Node* newNode = (Node*) malloc(sizeof(Node));

    if (newNode == NULL) {
        fprintf(stderr, "Erro de alocacao de memoria.\n");
        exit(EXIT_FAILURE);
    }

    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}

/* Busca recursivamente uma chave em uma BST */
Node* search(Node* root, int key) {
    if (root == NULL) {
        return NULL;
    }

    if (root->value == key) {
        return root;
    }

    if (key < root->value) {
        return search(root->left, key);
    }

    return search(root->right, key);
}

/* Libera toda a memória da árvore */
void freeTree(Node* root) {
    if (root == NULL) {
        return;
    }

    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

int main() {
    /*
        Árvore montada na memória:

              10
             /  \
            5   15
    */

    Node* root = createNode(10);
    root->left = createNode(5);
    root->right = createNode(15);

    Node* result1 = search(root, 5);

    if (result1 != NULL) {
        printf("Valor encontrado: %d\n", result1->value);
    } else {
        printf("Valor nao encontrado.\n");
    }

    Node* result2 = search(root, 20);

    if (result2 != NULL) {
        printf("Valor encontrado: %d\n", result2->value);
    } else {
        printf("Valor nao encontrado.\n");
    }

    freeTree(root);

    return 0;
}
```

---

## Casos de Uso

### Caso 1 — Busca bem-sucedida

Árvore:

```
      10
     /  \
    5   15
```

Chamada:

```c
search(root, 5);
```

Passos:

1. Compara `5` com `10` → `5 < 10`, segue para a esquerda.
2. Chega ao nó com valor `5`.
3. O valor procurado foi encontrado.
4. Retorna o ponteiro para esse nó.

Resultado:

```text
Valor encontrado: 5
```

---

### Caso 2 — Busca mal-sucedida

Árvore:

```
      10
     /  \
    5   15
```

Chamada:

```c
search(root, 20);
```

Passos:

1. Compara `20` com `10` → `20 > 10`, segue para a direita.
2. Compara `20` com `15` → `20 > 15`, segue para a direita.
3. O ponteiro direito de `15` é `NULL`.
4. A função atinge o caso base nulo e retorna `NULL`.

Resultado:

```text
Valor nao encontrado.
```

### Complexidade

* **Melhor caso:** `O(1)` (valor encontrado na raiz).
* **Árvore balanceada:** `O(log n)`.
* **Pior caso (árvore degenerada):** `O(n)`.
* **Memória adicional:** `O(h)`, onde `h` é a altura da árvore devido à pilha de chamadas recursivas.
