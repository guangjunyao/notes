#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

int fibonacci(int n)
{
  std::vector<int> v;
  v =  {0, 1};
  while(n>v.size())
    v.push_back(v.back()+v[v.size()-2]);
  return v[n-1];

  int prev = 0;
  int curr = 1;
  if (n<2)
    {
      return n;
    }
  for(int i=1; i<n; ++i){
    int temp = curr;
    curr += prev;
    prev = curr;
    }
  return curr;
}
int main(){
  using namespace std;

  std::cout << fibonacci(3) << std::endl;
  return -1;
}
