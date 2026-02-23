#include<iostream>
using namespace std;
int main() {
    typedef int test;
    test x = 5;
    test a = 3;

    enum Color { RED, GREEN, BLUE } c ;
    c = RED; 
    cout << c << endl;
    /*double b = 5;
    cout << x << endl; 
    cout << 3*3 << endl;
    cout << "3 + 5 = " << a+b << endl;
    cout << sizeof(a) << " " << sizeof(b) << endl;
    */
    return 0;
}