#include <iostream>
#include <assert.h>
#include "ref_and_var.h"
using std::cout;
int main()
{
    x_and_ref x_ref;
    x_ref.x = 7;
    assert(x_ref.ref==7); // returns true
    std::cout << "Checkpoint #1\n";
    x_ref.ref = 10;
    assert(x_ref.x==10); // returns true
    std::cout << "Checkpoint #2\n";
    return 0;
}
