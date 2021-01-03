#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> home;
    vector<int> away;

    int h;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> h;
        cin >> a;
        home.push_back(h);
        away.push_back(a);
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        h = home.at(i);
        for (int j = 0; j < n; j++) {
            if (j == i) {
                continue;
            }
            a = away.at(j);
            if (a == h) {
                count += 1;
            }
        }
    }

    cout << count << endl;
}
