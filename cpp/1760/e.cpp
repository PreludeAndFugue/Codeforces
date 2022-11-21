#include <iostream>
#include <vector>


int count_inversions(std::vector<int> a) {
    int c1 = 0;
    int answer = 0;
    for (int x : a) {
        if (x == 0) {
            answer += c1;
        } else {
            c1++;
        }
    }
}


int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        std::cin >> n;

        std::vector<int> a;
        for (int j = 0; j < n; j++) {
            int x;
            std::cin >> x;
            a.push_back(x);
        }

        int ci = count_inversions(a);

        std::cout << "count inversion: " << ci <<std::endl;

    }
}