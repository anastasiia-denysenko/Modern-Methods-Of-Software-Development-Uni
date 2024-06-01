#include <iostream>
using namespace std;
class stack
{
public:
    int A [5];
};
class heap
{
public:
    int size;
    int *B = new int[size];
};
int main()
{
    stack stack_class;
    heap heap_class;
    cout << "Type a number: ";
    cin >> heap_class.size;
    cout<<"Stack object"<<stack_class.A<<endl;
    cout<<"Heap object"<<heap_class.B<<endl;
    delete [] heap_class.B;
    return 0;
}