#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int maxProduct(vector<int>& nums, int k)
{
    int lProduct = 1, rProduct = 1;
    int size = nums.size(), maxProduct = nums[0];
    for(int i = 0; i < size; ++i)
    {
        lProduct *= nums[i];
        rProduct *= nums[size-i-1];
        maxProduct = max(maxProduct, max(lProduct, rProduct));
        if(lProduct == 0) lProduct = 1;
        if(rProduct == 0) rProduct = 1;
    }
    return maxProduct;
}
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
	int n = nums.size();
	vector<int> products(n + 1, 1);
	for (int i = 0; i < n; ++i) products[i + 1] = products[i] * nums[i];

	int ans = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j <= n; ++j) {
			if (products[j] / products[i] < k) ++ans;
		}
	}
	return ans;
}

int main()
{
	float y = 2.1;
	// foo<float, 3>(y);
    int arr[] = { 1, 2, 3 };
    int n = sizeof(arr) / sizeof(arr[0]);

    vector<int> vect(arr, arr + n);
	cout << maxProduct(vect, 4) << endl;
	cout << numSubarrayProductLessThanK(vect, 4) << endl;

}
