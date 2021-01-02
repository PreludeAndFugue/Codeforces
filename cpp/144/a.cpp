#include <iostream>
#include <vector>

using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> hs = {};

    int x;
    for (int i = 0; i < n; i++) {
        cin >> x;
        hs.push_back(x);
    }

    int large_position = 0;
    int large_value = 0;
    int small_position = 0;
    int small_value = 200;
    int h;

    for (int i = 0; i < hs.size(); i++) {
        h = hs.at(i);
        if (h <= small_value) {
            small_value = h;
            small_position = i;
        }
        if (h > large_value) {
            large_value = h;
            large_position = i;
        }
    }

    int steps = large_position + (hs.size() - 1) - small_position;
    if (large_position > small_position) {
        steps -= 1;
    }

    cout << steps << endl;
}
