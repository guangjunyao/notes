#include <iostream>
#include <vector>

using namespace std;

vector<int> temp;
vector<vector<int> > result;
void SimpleKnapsack(vector<int> items, int capacity, int i)
{
	if (capacity == 0)
	{
		result.push_back(temp);
		return;
	}
	else if (i >= items.size() || items[i] > capacity)
		return;
  cout << items[i] << endl;
	temp.push_back(items[i]);
	SimpleKnapsack(items, capacity - items[i], i + 1);

  cout << items[i] << endl;
	temp.pop_back();
	SimpleKnapsack(items, capacity, i + 1);
}
void SimpleKnapsack_stack(vector<int> items, int capacity)
{
	int n = items.size(), sum = 0, i = 0, start = 0;
	vector<int> stack;
	vector<int> visited(n, 0);

	while (1)
	{
		for (i = start; i < n; ++i)
		{
			if (!visited[i] && items[i] + sum <= capacity)
			{
				sum += items[i];
				stack.push_back(i);
				temp.push_back(items[i]);
				visited[i] = 1;
				if (sum == capacity)
				{
					result.push_back(temp);
					break;
				}
			}
		}

		if (i == n)
		{
			if (stack.empty())
				return;
			int top = stack.back();
			stack.pop_back();
			temp.pop_back();
			visited[top] = 0;
			sum -= items[top];
			start = top + 1;
		}
	}
}
int knap(int w[], int t, int n)
{
	if(t==0)
		return 1;
	else
		if(t<0||t>0&&n<1)
			return 0;
		else
			if(knap(w,t-w[n-1],n-1)==1)
        {
          cout<<"result: n="<<n<<", w["<<n-1<<"]="<<w[n-1]<<endl;
          return 1;
        }
			else
				return knap(w,t,n-1);
}
int main()
{
	int w[] = { 2, 7, 5, 3, 8};
	vector<int> items(w, w + 5);

  knap(w, 15, 5);
  //	SimpleKnapsack(items, 15, 0);
	//SimpleKnapsack_stack(items, 15);
}
