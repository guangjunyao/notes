#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>

// vector<char> generate_26_letters(){
// 	using namespace std;
// 	vector<char> s;
// 	for(char i='a'; i<= 'z'; i++)
//     {
//       s.push_back(i);
//     }
// 	for (std::vector<char>::const_iterator i = s.begin(); i != s.end(); ++i)
//     std::cout << *i << ' ';
// 	// cout << s << endl;
// 	return s;
// }

int bit(unsigned int x)
{
  int c = 0;
  while( x )
    {
      c++;
      x = (x & (x - 1));
    }
  return c;
}

void print(unsigned int x, int count)
{
  int i = 0;
  //控制，假如count为3， x 里边有三个 1
  if( bit(x) == count )
    {
      for(i=0; i<26; i++)
        {
          if( x & 1)
            {
              printf("%c ", (char)('a' + i));
            }
          x = (x >> 1);
        }
      printf("\n");
    }
}

int main()
{
  const unsigned int N = 26;
  const unsigned int C = 3;
  const unsigned int X = (1 << N) - 1;  //X=(1<<26)-1
  unsigned int i = 0;

  for(i=0; i<X; i++)
    {
      print(i, C);
    }
  return 0;
}
