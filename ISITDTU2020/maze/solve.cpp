#include<bits/stdc++.h>
using namespace std;
int v0 = 3, v1 = 0;
typedef struct tmp{
	int V0, V1;
	char path[35];
}tmp;
tmp* make(int V0, int V1, char* str){
	tmp* x = (tmp*)malloc(sizeof(tmp));
	memset(x, 0, sizeof(tmp));
	x->V0 = V0;
	x->V1 = V1;
	strcpy(x->path, str);
	return x;
} 
queue<tmp*> qe;
char* strcat_l(char* x, const char* y){
	char* ret = (char*)malloc(strlen(x));
	strcpy(ret, x);
	strcat(ret, y);
	return ret;
}
/*
bool check(tmp* x){
	char* path = x->path;
	int v0_ = 3, v1_ = 0;
	int y[strlen(path) + 5][2];
	memset(y, 0, sizeof(y));
//	cout << path << " "<< strlen(path) << endl;
	y[0][0] = v0_;
	y[0][1] = v1_;
	for(int i = 0; i < strlen(path); i++){
		if(path[i] == 'U'){
			y[i + 1][1] = y[i][1] -  1;	
			y[i + 1][0] = y[i][0];
		} 
		if(path[i] == 'D'){
			y[i + 1][1] = y[i][1] + 1;
			y[i + 1][0] = y[i][0];
		}
		if(path[i] == 'L'){
			y[i + 1][0] = y[i][0] - 1;
			y[i + 1][1] = y[i][1];	
		}
		if(path[i] == 'R'){
			y[i + 1][0] = y[i][0] + 1;
			y[i + 1][1] = y[i][1];	
		}
		for(int j = 0; j <= i; j++){
			if(y[j][0] == y[i + 1][0] && y[j][1] == y[i + 1][1]) return false;
		}
	}
	return true;
}
*/
char c1[] = {0,  1,   0,   1,   0,   1,   1,   1,   0,   0, 
    1,   1,   1,   0,   1,   1,   0,   1,   1,   0, 
    0,   1,   0,   1,   0,   1,   1,   0,   0,   1, 
    0,   0,   1,   0,   0,   0,   1,   0,   0,   1, 
    0,   0,   1,   1,   0,   1,   1,   0,   1,   1, 
    0,   0,   1,   0,   0,   0,   1,   1,   0,   0, 
    1,   1,   0,   0,   0,   1,   0,   1,   0,   0, 
    1,   1,   0,   0,   1,   1,   1,   0,   1,   0, 
    1,   0,   0,   1,   0,   1,   1,   0,   1,   0, 
    0,   1,   1,   1,   1,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   0,   1,   0,   1,   0,   0, 
    1,   1,   0,   1,   1,   0,   1,   1,   0,   0, 
    0,   1,   0,   1,   1,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   1,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   1,   1,   0,   0,   1,   1, 
    0,   0,   1,   0,   0,   1,   0,   1,   1,   0, 
    1,   1,   0,   0,   0,   1,   0,   1,   0,   0, 
    1,   1,   1,   0,   1,   0,   1,   1,   0,   0, 
    1,   1,   0,   0,   0,   1,   0,   1,   1,   0, 
    1,   0,   1,   1,   0,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   0,   1,   0,   1,   1,   0, 
    1,   0,   1,   1,   0,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   1,   0,   0,   1,   0,   0, 
    1,   1,   1,   0,   1,   0,   1,   0,   0,   1, 
    0,   1,   1,   0,   1,   0,   0,   1,   0,   0, 
    1,   1,   1,   0,   1,   0};
int main(){
	cout << "lol\n";
	char S[35] = {0};
	qe.push(make(v0, v1, S));
	int deep = 0;
	while(true){
		if(deep == 34) break;
		int cur = qe.size();
		while(cur > 0){
			tmp* x = qe.front();
			qe.pop();
			int v0_ = x->V0;
			int v1_ = x->V1;
			
			int id = 4 * (v0_ + 8 * v1_);
			if(v0_ < 0 || v1_ < 0 || v0_ >= 8 || v1_ >= 8){
				cur -= 1;
				continue;
			}
//			if(!check(x)){
//				cur -= 1;
//				continue;
//			}
			if(c1[id] == 1) qe.push(make(v0_, v1_ - 1, strcat_l(x->path, "U")));
			if(c1[id + 1] == 1) qe.push(make(v0_, v1_ + 1, strcat_l(x->path, "D")));
			if(c1[id + 2] == 1) qe.push(make(v0_ - 1, v1_, strcat_l(x->path, "L")));
			if(c1[id + 3] == 1) qe.push(make(v0_ + 1, v1_, strcat_l(x->path, "R")));
	//		cout << x->path << endl;
			cur -= 1;
		}
		deep += 1;
		cout << deep << " " << qe.size() << endl;
	}
	while(qe.size() > 0){
		tmp* x = qe.front();
		qe.pop();
		if(x->V0 == 4 && x->V1 == 7){
			cout << x->path << endl;
		}
	}
}
