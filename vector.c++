#include <iostream>

using namespace std;

int main()
{

    vector<int> vect;
  
    vect.push_back(1);
    vect.push_back(2);
    vect.push_back(3);
  
    for (int x : vect)
        cout << x << " ";
  
    return 0;
}