Aqui está um exemplo em C que implementa a busca de um valor em uma árvore binária utilizando ponteiros e recursividade:

#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da árvore binária
typedef struct No {
    int valor;
    struct No *esquerda;
    struct No *direita;
} No;

// Função para criar um novo nó
No* criarNo(int valor) {
    No *novo = (No*) malloc(sizeof(No));

    if (novo != NULL) {
        novo->valor = valor;
        novo->esquerda = NULL;
        novo->direita = NULL;
    }

    return novo;
}

// Função recursiva para buscar um valor na árvore
No* buscar(No *raiz, int valor) {
    // Caso base: árvore vazia ou valor encontrado
    if (raiz == NULL || raiz->valor == valor) {
        return raiz;
    }

    // Busca na subárvore esquerda
    No *resultado = buscar(raiz->esquerda, valor);

    // Se encontrou na esquerda, retorna
    if (resultado != NULL) {
        return resultado;
    }

    // Caso contrário, busca na direita
    return buscar(raiz->direita, valor);
}

int main() {
    // Construção manual da árvore
    No *raiz = criarNo(10);
    raiz->esquerda = criarNo(5);
    raiz->direita = criarNo(20);
    raiz->esquerda->esquerda = criarNo(3);
    raiz->esquerda->direita = criarNo(7);

    int valorBuscado = 7;

    No *encontrado = buscar(raiz, valorBuscado);

    if (encontrado != NULL) {
        printf("Valor %d encontrado na árvore.\n", valorBuscado);
    } else {
        printf("Valor %d não encontrado na árvore.\n", valorBuscado);
    }

    return 0;
}
Como funciona
Cada nó da árvore contém:
um valor (valor);
um ponteiro para o filho esquerdo (esquerda);
um ponteiro para o filho direito (direita).
A função buscar() é recursiva:
Se o nó atual for NULL, o valor não foi encontrado naquele ramo.
Se o valor do nó atual for igual ao procurado, retorna o ponteiro para esse nó.
Caso contrário, procura primeiro na subárvore esquerda e depois na direita.
O retorno é um ponteiro para o nó encontrado ou NULL caso o valor não exista na árvore.

Complexidade:

Melhor caso: O(1) (valor encontrado na raiz).
Pior caso: O(n), onde n é o número de nós da árvore.