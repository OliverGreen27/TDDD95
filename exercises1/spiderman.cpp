#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

void solve(vector<int> distances) {
    // För att hitta rätt lösning, spara den minimala max höjden
    // som för varje nod.  Gör man rekursion, använd map som cache
    // varje key ska vara funktionanropets 
}

int main()
{
    int num_tests;
    cin >> num_tests;
    // cout << num_tests << endl;

    for (int i = 0; i < num_tests; i++) {
        int num_distances;
        cin >> num_distances;
        // cout << num_distances << endl;

        vector<int> distances;
        for (int j = 0; j < num_distances; j++) {
            int temp_distance;
            cin >> temp_distance;
            distances.push_back(temp_distance);
            //cout << temp_distance << endl;
        }
        solve(distances);
    }
    return 0;
}