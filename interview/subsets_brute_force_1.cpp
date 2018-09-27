#include <stdio.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>

using namespace std;
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int check_each_digit(int x, int min, int max, vector<int>& combination)
{
    if(x >= 10)
       check_each_digit(x / 10, min, max, combination);

    int digit = x % 10;
    //std::cout << digit << '\n';
	if (digit >= min && digit <= max)
	{
		combination.push_back(digit);
		return true;
	}
	else{
		return false;
	}
}

int main()
{
	int minValue = 2;
	int maxValue = 4;
	int rotorCount = 3;
	int count = 0;
	vector<int> combination;
	int start = pow(10.0, rotorCount-1);
	int end = pow(10.0, rotorCount);
	/* 通过数所有数字，只取出现在数组的元素 */
	for(int i= start; i < end; i++){

		if (check_each_digit(i, minValue, maxValue, combination)){
			if (combination.size() == 3){
				int first = combination.front();
				cout << "first " << first;
				bool good = true;
				for (std::vector<int>::iterator it = combination.begin()+1 ; it != combination.end(); ++it){
					if (gcd(first, *it) != 1) {
            // 只取与第一个元素的最大公约数为1的数
						good = false;
						break;
					}
					std::cout << ' ' << *it;
				}
			if (good) count += 1;
			std::cout << '\n';
			}
		combination.clear();
		}
	}
	cout << count << endl;
}
