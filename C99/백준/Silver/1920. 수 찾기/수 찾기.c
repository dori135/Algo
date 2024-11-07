#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int static compare(const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}



int bin_search(const int a[], int n, int key) {
    int pl = 0;
    int pr = n - 1;
    do {
        int pc = (pl + pr) / 2;
        if (a[pc] == key)
            return 1;
        else if (a[pc] < key)
            pl = pc + 1;
        else
            pr = pc - 1;
    } while (pl <= pr);

    return 0;
}
int main(void) {
    int n, m;

    scanf("%d", &n);
    int* a = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", &a[i]);

    qsort(a, n, sizeof(int), compare);
    
    scanf("%d", &m);
    int* b = (int*)malloc(sizeof(int) * m);
    for (int i = 0; i < m; i++)
        scanf("%d", &b[i]);

    for (int i = 0; i < m; i++) {
        printf("%d\n", bin_search(a, n, b[i]));
    }
    return 0;
}