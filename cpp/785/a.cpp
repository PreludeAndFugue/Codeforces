#include <iostream>
#include <cassert>

using namespace std;

int face_count(string);

int main() {
    int n;
    cin >> n;
    int count = 0;
    string name;
    for (int i; i < n; i++) {
        cin >> name;
        count += face_count(name);
    }
    cout << count << endl;
}


int face_count(string name) {
    if (name == "Tetrahedron") {
        return 4;
    }
    if (name == "Cube") {
        return 6;
    }
    if (name == "Octahedron") {
        return 8;
    }
    if (name == "Dodecahedron") {
        return 12;
    }
    if (name == "Icosahedron") {
        return 20;
    }
    return 0;
}
