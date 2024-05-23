#include <iostream>
#include <assert.h>
using namespace std;
 
class x_ref
{
    public:
        int x = 5; // x - variable
        int& ref = x; // ref - reference
 };
