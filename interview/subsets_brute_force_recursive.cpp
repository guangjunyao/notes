#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
// vector<vector<int> > subsets(vector<int> &S) {
//   sort(S.begin(), S.end()); // 输出有序
//   vector<vector<int> > result;
//   vector<int> path;
//   subsets(S, path, 0, result);
//   return result;
// }
static void subsets(const vector<int> &S, vector<int> &path, int step,
                      vector<vector<int> > &result) {
    if (step == S.size()) {
      result.push_back(path);
      return;
    }
    // 不选 S[step]
    subsets(S, path, step + 1, result);
    // 选 S[step]
    path.push_back(S[step]);
    subsets(S, path, step + 1, result);
    path.pop_back();
  }
vector<vector<int> > subsets(vector<int> &S) {
  sort(S.begin(), S.end()); // 䓂ܩ㺰ⅱ᰸Ꮎ
  vector<vector<int> > result(1);
  for (auto elem : S) {
    result.reserve(result.size() * 2);
    auto half = result.begin() + result.size();
    copy(result.begin(), half, back_inserter(result));
    for_each(half, result.end(), [&elem](decltype(result[0]) &e){
        e.push_back(elem);
      });
  }
  return result;
}

vector<vector<int> > subset(vector<int> &S) {
  sort(S.begin(), S.end());
  vector<vector<int> > result;
  const size_t n = S.size();
  vector<int> v;
  for (size_t i = 0; i < 1 << n; i++) {
    for (size_t j = 0; j < n; j++) {
      if (i & 1 << j) v.push_back(S[j]);
    }
    result.push_back(v);
    v.clear();
  }
  return result;
}
int main()
{
	int minValue = 2;
	int maxValue = 4;
	int rotorCount = 3;
	int count = 0;
	vector<int> combination;
	int start = pow(10.0, rotorCount-1);
  int arr[] = {1,2,3};
  int n = sizeof(arr) / sizeof(arr[0]);
  vector<int> vect(arr, arr + n);
  vector<vector<int> > sets = subsets(vect);
  for (auto x: sets){
    for (auto y: x){
      cout << y << ' ';
    }
    cout << endl;
  };
  return 0;
}
