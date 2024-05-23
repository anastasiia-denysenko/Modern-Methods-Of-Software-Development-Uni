#include <assert.h>
#include <iostream>
#include <cassert>
#include ref_and_var
#define assertm(exp, msg) assert(((void)msg, exp))
int main()
{
    ref_and_point_zero rp_zero;
    ref_and_point_one rp_one;
    ref_and_point_two rp_two;
    assert(rp_zero.x == rp_zero.ref);
    std::cout << "Checkpoint #1\n";
    assert(rp_one.x != rp_one.ref);
    std::cout << "Checkpoint #2\n";
    assert(rp_two.x == rp_two.ref);
    std::cout << "Checkpoint #3\n";
}
