#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;


int gcd(int a, int b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

int main()
{
	//float y = 2.1;
	//// foo<float, 3>(y);
  //   int arr[] = { 1, 2, 3 };
  //   int n = sizeof(arr) / sizeof(arr[0]);
  //
  //   vector<int> vect(arr, arr + n);
	//cout << maxProduct(vect, 4) << endl;
	//cout << numSubarrayProductLessThanK(vect, 4) << endl;
  int a = 2, b = 3;
  printf("Gcd of given numbers is %d\n", gcd(a, b));

}
