/**
 * Implements a dictionary's functionality.
 */
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"

typedef struct node {
    bool is_word;
    struct node *child[27];
} node;

int hash(char *c);
void init_node(node *node);
void free_tries(node *node);

node *root;
FILE *fp;
int words_in_dictionary = 0;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    node *ptr = root;
    int hash_code = 0;
    for (int i = 0, n = strlen(word); i < n; i++) {
        hash_code = hash((char*)&word[i]);
        if (!ptr->child[hash_code]) {
            return false;
        }
        ptr = ptr->child[hash_code];
        if (i == (n-1) && !ptr->is_word) {
            return false;
        }
    }
    return true;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    fp = fopen(dictionary, "r");
    if (fp == NULL) {
        return false;
    }

    char word[LENGTH+1];
    int hash_code = 0;
    root = malloc(sizeof(node));
    init_node(root);
    while(fscanf(fp, "%s", word) != EOF) {
        words_in_dictionary++;
        node *ptr = root;
        for (int i = 0, n = strlen(word); i < n; i++) {
            hash_code = hash(&word[i]);
            if (!ptr->child[hash_code]) {
                node *child_node = malloc(sizeof(node));
                init_node(child_node);
                ptr->child[hash_code] = child_node;
            }
            ptr = ptr->child[hash_code];
            if (i == (n - 1)) {
                ptr->is_word = true;
            }
        }
    }

    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    if (fp == NULL) {
        return 0;
    }
    return words_in_dictionary;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    if (fp != NULL) {
        fclose(fp);
        free_tries(root);
        return true;
    }
    return false;
}

int hash(char *c) {
    if (*c == '\'') {
        return 26;
    }
    return (int)tolower(*c) - 97;
}

void init_node(node *node) {
    node->is_word = false;
    for (int i = 0; i < 27; i++) {
        node->child[i] = NULL;
    }
}

void free_tries(node *node) {
    if (!node) {
        return;
    }
    for (int i = 0; i < 27; i++) {
        free_tries(node->child[i]);
    }
    free(node);
}