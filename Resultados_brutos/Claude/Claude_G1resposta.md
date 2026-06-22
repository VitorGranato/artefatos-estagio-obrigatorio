## Busca em Árvore Binária de Busca — C

O código implementa uma **BST (Binary Search Tree)** completa com três operações recursivas principais:

---

### Estrutura de dados

```c
typedef struct No {
    int valor;
    struct No *esquerda;  // ponteiro para filho esquerdo
    struct No *direita;   // ponteiro para filho direito
} No;
```

---

### Função de busca (`buscar`)

É o coração da solução. Usa dois casos base e recursão:

| Situação | Ação |
|---|---|
| `raiz == NULL` | Valor **não existe** na árvore → retorna `NULL` |
| `valor == raiz->valor` | **Encontrado** → retorna o ponteiro do nó |
| `valor < raiz->valor` | Desce para o **filho esquerdo** (recursão) |
| `valor > raiz->valor` | Desce para o **filho direito** (recursão) |

```c
No *buscar(No *raiz, int valor) {
    if (raiz == NULL)       return NULL;      // não encontrado
    if (valor == raiz->valor) return raiz;    // encontrado!
    if (valor < raiz->valor)
        return buscar(raiz->esquerda, valor); // busca à esquerda
    else
        return buscar(raiz->direita, valor);  // busca à direita
}
```

---

### Saída esperada

```
Árvore em ordem: 20 30 40 50 60 70 80

Busca por 40 → ENCONTRADO  (endereço: 0x...)
Busca por 99 → NÃO encontrado
Busca por 60 → ENCONTRADO  (endereço: 0x...)
Busca por 10 → NÃO encontrado
```

---

### Compile e execute

```bash
gcc -Wall -o bst binary_tree_search.c && ./bst
```

**Complexidade:** O(log n) no caso médio, O(n) no pior caso (árvore degenerada). A memória é completamente liberada ao final pela função `liberar()`.

Binary tree search · C
/**
 * Busca em Árvore Binária de Busca (BST)
 * Utiliza manipulação de ponteiros e recursividade.
 */
 
#include <stdio.h>
#include <stdlib.h>
 
/* ──────────────────────────────────────────
   Definição da estrutura do nó
   ────────────────────────────────────────── */
typedef struct No {
    int valor;
    struct No *esquerda;
    struct No *direita;
} No;
 
/* ──────────────────────────────────────────
   Cria e retorna um novo nó
   ────────────────────────────────────────── */
No *criar_no(int valor) {
    No *novo = (No *)malloc(sizeof(No));
    if (!novo) {
        fprintf(stderr, "Erro: falha na alocação de memória.\n");
        exit(EXIT_FAILURE);
    }
    novo->valor    = valor;
    novo->esquerda = NULL;
    novo->direita  = NULL;
    return novo;
}
 
/* ──────────────────────────────────────────
   Insere um valor na BST (recursivo)
   ────────────────────────────────────────── */
No *inserir(No *raiz, int valor) {
    if (raiz == NULL)
        return criar_no(valor);
 
    if (valor < raiz->valor)
        raiz->esquerda = inserir(raiz->esquerda, valor);
    else if (valor > raiz->valor)
        raiz->direita = inserir(raiz->direita, valor);
    /* valor == raiz->valor: duplicata ignorada */
 
    return raiz;
}
 
/* ──────────────────────────────────────────
   Busca um valor na BST (recursivo)
   Retorna ponteiro para o nó encontrado
   ou NULL se não existir.
   ────────────────────────────────────────── */
No *buscar(No *raiz, int valor) {
    /* Caso base 1: árvore vazia ou valor não encontrado */
    if (raiz == NULL)
        return NULL;
 
    /* Caso base 2: valor encontrado no nó atual */
    if (valor == raiz->valor)
        return raiz;
 
    /* Recursão: desce para o filho correto */
    if (valor < raiz->valor)
        return buscar(raiz->esquerda, valor);
    else
        return buscar(raiz->direita, valor);
}
 
/* ──────────────────────────────────────────
   Percurso Em-Ordem (in-order) — exibe
   os valores em ordem crescente
   ────────────────────────────────────────── */
void em_ordem(No *raiz) {
    if (raiz == NULL) return;
    em_ordem(raiz->esquerda);
    printf("%d ", raiz->valor);
    em_ordem(raiz->direita);
}
 
/* ──────────────────────────────────────────
   Libera toda a memória da árvore
   ────────────────────────────────────────── */
void liberar(No *raiz) {
    if (raiz == NULL) return;
    liberar(raiz->esquerda);
    liberar(raiz->direita);
    free(raiz);
}
 
/* ──────────────────────────────────────────
   Programa principal — demonstração
   ────────────────────────────────────────── */
int main(void) {
    No *raiz = NULL;
 
    /* Montagem da árvore:
     *
     *          50
     *         /  \
     *       30    70
     *      /  \  /  \
     *    20  40 60  80
     */
    int valores[] = {50, 30, 70, 20, 40, 60, 80};
    int n = sizeof(valores) / sizeof(valores[0]);
 
    for (int i = 0; i < n; i++)
        raiz = inserir(raiz, valores[i]);
 
    /* Exibe a árvore em ordem crescente */
    printf("Árvore em ordem: ");
    em_ordem(raiz);
    printf("\n\n");
 
    /* Testes de busca */
    int alvos[] = {40, 99, 60, 10};
    int total   = sizeof(alvos) / sizeof(alvos[0]);
 
    for (int i = 0; i < total; i++) {
        No *resultado = buscar(raiz, alvos[i]);
        if (resultado)
            printf("Busca por %2d → ENCONTRADO  (endereço: %p)\n",
                   alvos[i], (void *)resultado);
        else
            printf("Busca por %2d → NÃO encontrado\n", alvos[i]);
    }
 
    /* Libera memória */
    liberar(raiz);
    raiz = NULL;
 
    return 0;
}
 