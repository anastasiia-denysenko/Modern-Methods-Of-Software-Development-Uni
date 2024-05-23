#include <iostream>
#include <assert.h>
using std::cout;
class x_and_ref
{
    public:
        int x = 5; // x - змінна
        int& ref = x; // j is a reference variable for i
};