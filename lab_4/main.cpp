#include <iostream>
#include <assert.h>
#include "ref_and_var.h"// include file with original values
using std::cout;
int main()
{
    x_and_ref x_ref;// include class from ref_and_var.h
    x_ref.x = 7;// change value of variable x, so reference also changes
    assert(x_ref.ref==7); // returns true
    x_ref.ref = 10;// change value of reference, which prescribes x new value
    assert(x_ref.x==10); // returns true
    return 0;
}
