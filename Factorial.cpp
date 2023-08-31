#include <iostream>
#include <math.h>
using namespace std;


int fact(int num){
    int factorial = 1;
    for(int i =1;i<=num;i++){
        factorial *= i;
    }
    return factorial;
}

int main(){
    int ans,n;
    cin>>n;
    ans = fact(n);
    cout<<"The factorial of "<<n<<" is "<<ans<<endl;
    
}
    



