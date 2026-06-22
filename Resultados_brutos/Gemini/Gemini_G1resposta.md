Aqui está uma solução limpa e eficiente em **C** para buscar um valor em uma árvore binária utilizando **ponteiros** e **recursividade**.

Como você não especificou se a árvore é uma Árvore Binária de Busca (BST) ou uma árvore binária comum, apresento a solução para uma **Árvore Binária Comum** (onde o valor pode estar em qualquer lugar). Se for uma BST, a busca pode ser ainda mais otimizada.

---

### Código Completo em C

```c
#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura do nó da árvore
typedef struct No {
    int conteudo;
    struct No *esquerda;
    struct No *direita;
} No;

// Função recursiva para buscar um valor na árvore
No* buscar(No *raiz, int valorAlvo) {
    // Caso Base 1: A árvore está vazia ou alcançamos um nó folha nulo
    if (raiz == NULL) {
        return NULL;
    }

    // Caso Base 2: O valor foi encontrado no nó atual
    if (raiz->conteudo == valorAlvo) {
        return raiz;
    }

    // Passo Recursivo 1: Busca na subárvore esquerda
    No *encontradoEsquerda = buscar(raiz->esquerda, valorAlvo);
    if (encontradoEsquerda != NULL) {
        return encontradoEsquerda; // Se achou na esquerda, retorna o ponteiro
    }

    // Passo Recursivo 2: Se não achou na esquerda, busca na subárvore direita
    return buscar(raiz->direita, valorAlvo);
}

// Função auxiliar para criar um novo nó
No* criarNo(int valor) {
    No *novoNo = (No*)malloc(sizeof(No));
    if (novoNo != NULL) {
        novoNo->conteudo = valor;
        novoNo->esquerda = NULL;
        novoNo->direita = NULL;
    }
    return novoNo;
}

// Função principal para testar o algoritmo
int main() {
    // Montando uma árvore binária simples para teste
    //        10
    //       /  \
    //      5    20
    //     /
    //    3
    No *raiz = criarNo(10);
    raiz->esquerda = criarNo(5);
    raiz->direita = criarNo(20);
    raiz->esquerda->esquerda = criarNo(3);

    int alvo = 20;
    No *resultado = buscar(raiz, alvo);

    if (resultado != NULL) {
        printf("Valor %d encontrado no endereco de memoria: %p\n", resultado->conteudo, (void*)resultado);
    } else {
        printf("Valor %d nao encontrado na arvore.\n", alvo);
    }

    // Liberação de memória (simplificada para o exemplo)
    free(raiz->esquerda->esquerda);
    free(raiz->esquerda);
    free(raiz->direita);
    free(raiz);

    return 0;
}

```

---

### Como funciona a lógica?

* **Ponteiros (`No *raiz`):** A função recebe o ponteiro para o nó atual. Isso nos permite navegar pelos endereços de memória dos filhos (`raiz->esquerda` e `raiz->direita`) sem duplicar a árvore na memória.
* **Casos Base (Recursão):** 1. Se o ponteiro for `NULL`, significa que a busca chegou ao fim de um caminho sem sucesso (retorna `NULL`).
2. Se `raiz->conteudo == valorAlvo`, o nó atual é o que procuramos (retorna o ponteiro do nó atual).
* **Casos Recursivos:** A função "combina" os caminhos. Ela primeiro desce tudo o que pode para a esquerda. Se encontrar o valor, o ponteiro vai subindo de volta pelas chamadas da função. Se não encontrar nada na esquerda (retornar `NULL`), ela tenta o caminho da direita.