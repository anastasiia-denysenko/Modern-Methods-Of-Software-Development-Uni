#include <iostream>
using namespace std;
 
int main()
{
    int x = 10;
 
    // ref - референс для x.
    int& ref = x;
    std::cout << "x = " << x << std::endl;
    std::cout << "ref = " << ref << std::endl;
    return 0;
 }