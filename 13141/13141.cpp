#include <iostream>
using namespace std;

int main() {
	long long fib[86];
	fib[0] = 0;
	fib[1] = 1;
	for(int i=2; i<86; i++){
		fib[i] = fib[i-1] + fib[i-2];
	}
	int level;
	while(true){
		cin >> level;
		if(level == 0) return 0;
		cout << fib[level] << endl;
	}
}
