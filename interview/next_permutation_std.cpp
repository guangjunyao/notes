#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

vector<vector<int> > permute(vector<int> &num) {
  vector<vector<int> > result;
  sort(num.begin(), num.end());
  do {
    result.push_back(num);
  } while(next_permutation(num.begin(), num.end()));
  return result;
}
int main()
{
  int arr[] = {1,2,3};
  int n = sizeof(arr) / sizeof(arr[0]);
  vector<int> vect(arr, arr + n);
  vector<vector<int> > sets = permute(vect);
  for (auto x: sets){
    for (auto y: x){
      cout << y << ' ';
    }
    cout << endl;
  };
  return 0;
}
