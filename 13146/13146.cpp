#include <iostream>
#include <string>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define NONE 0
#define REPLACE 1
#define DELETE 2
#define INSERT 3
#define MAXN 102 //max

char w1[MAXN];
char w2[MAXN];

struct {
	int d, op, pos;
} lf[MAXN +1][MAXN + 1];

int levenshtein(int n, int m) {
	lf[0][0].d = 0;
	lf[0][0].pos = 1;
	FOR(i,1,n+1) {lf[i][0].d = i; lf[i][0].pos = 1;}
	FOR(i,1,m+1) {lf[0][i].d = i; lf[0][i].pos = 1;}

	FOR(i,1,n+1) {
		FOR(j,1,m+1) {
			lf[i][j].d = min(lf[i-1][j-1].d + ((w1[i-1] == w2[j-1])?0:1),min(lf[i][j-1].d+1,lf[i-1][j].d+1));
		}
	}
	return lf[n][m].d;
}

int main() {
	int tc;
	cin >> tc;
	string ol;
	getline(cin, ol);
	while (tc--) {
		string doo, doodle;
		getline(cin, doo);
		getline(cin, doodle);
		FOR(i,0,doo.length()) {
			w1[i] = doo[i];
		}
		FOR(i,0,doodle.length()) {
			w2[i] = doodle[i];
		}
		int erg = levenshtein(doo.length(), doodle.length());

		cout << erg << endl;
	}
}
