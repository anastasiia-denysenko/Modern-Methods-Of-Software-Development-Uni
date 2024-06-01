#include <iostream>
using namespace std;
int main() 
{
    int val = 5;

    int* pointer = &val;

    int& reference = val;

    cout << "Originally: " <<endl;

    cout << "\t" <<"Value: " << val << endl;

    cout << "\t" << "Reference: " << reference << endl;

    cout << "\t" << "Pointer: " << pointer << endl;

    cout << "\t" << "Value stored by pointer: " << *pointer << endl;

    val = 10;

    cout << "val = 10. Now: "<< endl;

    cout << "\t" << "Value: " << val << endl;

    cout << "\t" << "Reference: " << reference << endl;

    cout << "\t" << "Pointer: " << pointer << endl;

    cout << "\t" << "Value stored by pointer: " << *pointer << endl;

    reference = 12;

    cout << "reference = 12. Now: "<< endl;

    cout << "\t" << "Value: " << val << endl;

    cout << "\t" << "Reference: " << reference << endl;

    cout << "\t" << "Pointer: " << pointer << endl;

    cout << "\t" << "Value stored by pointer: " << *pointer << endl;

    *pointer = 15;

    cout << "*pointer = 15. Now: "<< endl;

    cout << "\t" << "Value: " << val << endl;

    cout << "\t" << "Reference: " << reference << endl;

    cout << "\t" << "Pointer: " << pointer << endl;

    cout << "\t" << "Value stored by pointer: " << *pointer << endl;

    return 0;
}
