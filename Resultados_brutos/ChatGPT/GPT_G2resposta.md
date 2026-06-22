# Visão Geral

Em uma **árvore binária de busca (BST)**, os valores menores que um nó ficam na subárvore esquerda e os maiores ficam na subárvore direita. A busca aproveita essa propriedade: compara o valor procurado com o valor do nó atual e, recursivamente, segue para a esquerda ou para a direita até encontrar o elemento desejado ou alcançar um ponteiro `NULL`, indicando que o valor não existe na árvore.

# Código Fonte

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *esquerda;
    struct No *direita;
} No;

No *buscar(No *raiz, int valor) {
    if (raiz == NULL || raiz->valor == valor) {
        return raiz;
    }

    if (valor < raiz->valor) {
        return buscar(raiz->esquerda, valor);
    }

    return buscar(raiz->direita, valor);
}

No *criarNo(int valor) {
    No *novo = (No *)malloc(sizeof(No));
    novo->valor = valor;
    novo->esquerda = NULL;
    novo->direita = NULL;
    return novo;
}

int main() {
    No *raiz = criarNo(50);
    raiz->esquerda = criarNo(30);
    raiz->direita = criarNo(70);
    raiz->esquerda->esquerda = criarNo(20);
    raiz->esquerda->direita = criarNo(40);
    raiz->direita->esquerda = criarNo(60);
    raiz->direita->direita = criarNo(80);

    int valorBuscado = 60;

    No *resultado = buscar(raiz, valorBuscado);

    if (resultado != NULL) {
        printf("Valor %d encontrado no endereco %p\n",
               resultado->valor, (void *)resultado);
    } else {
        printf("Valor %d nao encontrado.\n", valorBuscado);
    }

    return 0;
}
```

# Análise

A função `buscar` recebe um ponteiro para o nó atual da árvore. Em cada chamada recursiva:

1. Verifica se o ponteiro é `NULL` (fim do caminho) ou se o valor foi encontrado.
2. Se o valor procurado for menor que o valor do nó atual, a função é chamada novamente passando o ponteiro `raiz->esquerda`.
3. Caso contrário, a busca continua pela subárvore direita através de `raiz->direita`.

Dessa forma, a recursividade percorre a árvore seguindo os ponteiros adequados até retornar um ponteiro para o nó encontrado ou `NULL` quando o valor não está presente na estrutura.
