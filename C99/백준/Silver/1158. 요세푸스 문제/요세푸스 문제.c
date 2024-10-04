#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>


int main() {

	int n, k;
	int arr[5001] = {0,};
	int answer[5001] = {0, };

	scanf("%d %d", &n, &k);


	for (int i = 0; i < n; i++)
		arr[i] = i + 1;

	int c = 0;
	int b = 0;
	int num = n;

	do
	{
		for (int i = 0; i < n; i++) {
			c++;
			if (c == k) {
				c = 0;
				answer[b++] = arr[i];
				for (int j = i; j < n - 1; j++)
					arr[j] = arr[j + 1];
				n--;
				i--;
			}

		}

	} while (n!=0);

	printf("<");
	for (int i = 0; i < num-1 ; i++)
		printf("%d, ", answer[i]);
	printf("%d>", answer[num-1]);

}