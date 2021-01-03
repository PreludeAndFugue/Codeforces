#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool are_same(vector<char>, vector<char>);

int main() {
    string n1;
    string n2;
    string n3;
    cin >> n1;
    cin >> n2;
    cin >> n3;
    vector<char> v1_2;
    vector<char> v3;
    for (int i = 0; i < n1.size(); i++) {
        v1_2.push_back(n1.at(i));
    }
    for (int i = 0; i < n2.size(); i++) {
        v1_2.push_back(n2.at(i));
    }
    for (int i = 0; i < n3.size(); i++) {
        v3.push_back(n3.at(i));
    }

    string answer;
    if (are_same(v1_2, v3)) {
        answer = string("YES");
    } else {
        answer = string("NO");
    }
    cout << answer << endl;
}


bool are_same(vector<char> v1, vector<char> v2) {
    if (v1.size() != v2.size()) {
         return false;
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    char c1;
    char c2;
    for (int i = 0; i < v1.size(); i++) {
        c1 = v1.at(i);
        c2 = v2.at(i);
        if (c1 != c2) {
            return false;
        }
    }
    return true;
}