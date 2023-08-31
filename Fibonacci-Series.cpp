#include <iostream>
#include <math.h>
using namespace std;


void fibonacci(int num){
    int t1 = 0;
    int t2 = 1;
    int next_term ;
    for (int i=1;i<=num;i++){
        cout<<t1<<" ";
        next_term = t1+t2;
        t1 = t2;
        t2 = next_term;
    }
    return;

}

int main()
{
    int n;
    cin>>n;
   
    fibonacci(n);
    return 0;
}   

