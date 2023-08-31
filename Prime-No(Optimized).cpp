#include <iostream>
#include <math.h>
using namespace std;


int main(){
    int num,i,flag=0;
    cin>>num;
    for (i=2;i<=sqrt(num);i++){
        if(num%i==0){
            cout<<num<<" is not a Prime Number"<<endl;
            flag=1;
            break;
        }    
    }
    if(flag==0){
        cout<<num<<" is a Prime Number"<<endl;
    }

    
}
    



