#include <iostream>
#include <cmath>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); i++)

int quersum(int a) {
	int sum = 0;
	while (a > 0) {
		sum += a % 10;
		a = a / 10;
	}
	return sum;
}

int main() {
	int start = 9999;
	FOR(i,0,7) {
		cout << start+i << " "<<(start+i) * (start+i) << endl;
	}
}

int main2() {
	int count = 16;
	int now = 0;
	int erg[7];
	while (true) {
		if (now == 7) {
			break;
		} else if (abs(sqrt(quersum(count * count)) - (int) sqrt(quersum(count * count))) < 0.0000000000000000000000000001) {
			erg[now] = count;
			count++;
			now++;
		} else {
			now = 0;
			count++;
		}
	}
	FOR(i,0,7)
	{
		cout << erg[i] <<" " <<  erg[i] * erg[i] << endl;
	}
}

