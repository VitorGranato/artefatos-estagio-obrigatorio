Fala, pessoal! Sejam muito bem-vindos ao mundo da Arquitetura de Software. Quando falamos em sistemas de alta performance, como índices de bancos de dados ou sistemas de arquivos, a Árvore Binária de Busca (BST) é uma das estruturas mais fundamentais que vocês encontrarão. Compreender como navegar por ela usando ponteiros e recursão é o divisor de águas entre um programador que apenas escreve código e um engenheiro que projeta sistemas eficientes.

Abaixo, estruturei a solução desse problema focando em boas práticas de engenharia: código limpo, tipagem clara e eficiência algorítmica.

---

## Estratégia de Resolução

A estratégia para buscar um elemento em uma BST baseia-se no princípio de "dividir para conquistar", aproveitando a propriedade nativa da árvore: elementos menores que a raiz ficam à esquerda, e elementos maiores ficam à direita. Para resolver isso via recursão, estabelecemos dois **casos base**. O primeiro ocorre quando o ponteiro do nó atual é nulo (`NULL`), indicando que navegamos até o fim de um ramo sem encontrar a chave, ou que a árvore está vazia. O segundo caso base ocorre quando o valor do nó atual coincide exatamente com a chave buscada, significando que o elemento foi encontrado com sucesso. Em ambos os casos, interrompemos a recursão e retornamos o ponteiro atual.

Se nenhum dos casos base for atendido, a lógica transiciona para as **chamadas recursivas direcionadas**. Em vez de buscar a árvore inteira cegamente — o que degradaria a performance para uma complexidade linear $O(n)$ —, o algoritmo compara a chave com o valor do nó atual. Se a chave for menor, a função invoca a si mesma passando o suboficial da esquerda (`root->left`); se for maior, invoca a si mesma passando o da direita (`root->right`). Isso reduz o espaço de busca pela metade a cada linha de descida em uma árvore balanceada, garantindo uma eficiência de tempo média de $O(\log n)$.

---

## Implementação em C

```c
#include <stdio.h>
#include <stdlib.h>

/* Estrutura que define o nó da Árvore Binária de Busca (BST) */
typedef struct Node {
    int key;
    struct Node* left;
    struct Node* right;
} Node;

/**
 * Cria um novo nó na memória dinâmica.
 */
Node* createNode(int key) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        fprintf(stderr, "Erro: Falha na alocação de memória.\n");
        exit(EXIT_FAILURE);
    }
    newNode->key = key;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

/**
 * Executa a busca recursiva de uma chave na BST.
 * Retorna o ponteiro para o nó encontrado ou NULL se a chave não existir.
 */
Node* search(Node* root, int key) {
    if (root == NULL || root->key == key) {
        return root;
    }
    
    if (key < root->key) {
        return search(root->left, key);
    }
    
    return search(root->right, key);
}

/**
 * Função utilitária para liberar a memória da árvore (Evita Memory Leaks).
 */
void freeTree(Node* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main(void) {
    /* Montagem manual da estrutura conforme o cenário proposto */
    Node* root = createNode(10);
    root->left = createNode(5);
    root->right = createNode(15);

    // ---- CASO DE USO 1: Busca Bem-Sucedida ----
    int targetSuccess = 5;
    Node* resultSuccess = search(root, targetSuccess);
    
    if (resultSuccess != NULL) {
        printf("Busca por (%d): Sucesso! Nó encontrado no endereço de memória %p.\n", targetSuccess, (void*)resultSuccess);
    } else {
        printf("Busca por (%d): Falha. Nó não encontrado.\n", targetSuccess);
    }

    // ---- CASO DE USO 2: Busca Mal-Sucedida ----
    int targetFailure = 20;
    Node* resultFailure = search(root, targetFailure);
    
    if (resultFailure != NULL) {
        printf("Busca por (%d): Sucesso! Nó encontrado no endereço de memória %p.\n", targetFailure, (void*)resultFailure);
    } else {
        printf("Busca por (%d): Falha. Nó retornado como NULL.\n", targetFailure);
    }

    /* Boa prática de arquitetura: Liberar recursos antes de encerrar o processo */
    freeTree(root);
    return 0;
}

```

---

## Casos de Uso

Para entender o fluxo de execução do código acima, imagine o comportamento do ponteiro `root` caminhando pela memória do ponteiro original:

* **Cenário 1: `search(root, 5)**` A execução inicia na raiz, onde `root->key` é `10`. Como `5 != 10` e `root` não é nulo, os casos base são ignorados. O algoritmo avalia a condição `5 < 10` e dispara a chamada recursiva para o ponteiro da esquerda: `search(root->left, 5)`. Na nova instância da função, o ponteiro atual aponta para o nó de valor `5`. O caso base `root->key == key` (`5 == 5`) é imediatamente satisfeito, interrompendo a recursão e retornando exatamente o endereço de memória deste nó para a função principal (`main`).
* **Cenário 2: `search(root, 20)**` A execução começa novamente na raiz (`10`). Como `20 > 10`, o algoritmo ignora o lado esquerdo e faz a chamada recursiva para a direita: `search(root->right, 20)`. No próximo nível, o nó avaliado possui o valor `15`. A comparação determina que `20 > 15`, acionando mais uma chamada à direita: `search(root->right, 20)`. Contudo, o ponteiro `right` do nó `15` é `NULL`. Ao entrar nessa última instância, o primeiro caso base (`root == NULL`) é acionado, fazendo com que a função retorne `NULL` em cascata até a `main`, consolidando a busca mal-sucedida.