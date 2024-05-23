#include <iostream>
#include <assert.h>
#include "x_and_ref.cpp"
using std::cout;
int main()
{
    int x = 5; // x - змінна
    int& ref = x; // j is a reference variable for i
    x = 7;
    assert(ref==7); // returns true
    std::cout << "Checkpoint #1\n";
    ref = 10;
    assert(x==10); // returns true
    std::cout << "Checkpoint #2\n";
    return 0;
}
