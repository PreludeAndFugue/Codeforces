#include <iostream>
#include <vector>

using namespace std;

int left_large_index(vector<int> &hs) {
    int position = 0;
    int large = 0;
    int h;
    for (int i = 0; i < hs.size(); i++) {
        h = hs[i];
        if (h > large) {
            large = h;
            position = i;
        }
    }
    return position;
}


int right_small_index(vector<int> &hs) {
    int position = hs.size();
    int small = 200;
    int h;
    for (int i = 0; i < hs.size(); i++) {
        h = hs[i];
        if (h <= small) {
            small = h;
            position = i;
        }
    }
    return position;
}


int main() {
    int n;
    cin >> n;
    vector<int> hs = {};

    int x;
    for (int i = 0; i < n; i++) {
        cin >> x;
        hs.push_back(x);
    }

    int l = left_large_index(hs);
    int s = right_small_index(hs);

    int steps = l + (hs.size() - 1) - s;
    if (l > s) {
        steps -= 1;
    }

    // cout << l << " " << s << " answer: " << steps << endl;
    cout << steps << endl;
}
