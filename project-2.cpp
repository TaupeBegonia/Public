#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <string>
using std::string;

#include <vector>
using std::vector;

#include <fstream>
using std::ifstream;

#include <algorithm>
using std::sort;

#include <cmath>

// Returns the length of the input or password, whichever is shortest
// Parameters: references to the input and password strings
// Returns length as an int
int shorter_str_len(string &input, string &password) {
	int len_1 = static_cast<int>(input.size());
	int len_2 = static_cast<int>(password.size());
	if (len_1 <= len_2) {
		return len_1;
	} else {
		return len_2;
	}
}

// Asks for an input, and compares to a list of given passwords for matches
// Prints out the closest password(s) as contents of a vector
int main() {
	string input;
	cout << "Give me a password:" << endl;
	cin >> input;
	cout << "You provided a password of " << input << endl;
	ifstream file_info("common_passwords.txt");  // reads from this file
	string password;
	vector<string> sim_passwords;
	int least_diff = 10000;  // initialize password diff to a large value
	while (getline(file_info, password)) {  // iterate through each password
		int p_diff = 0;
		if (password == input) {
			sim_passwords.clear();  // clears vector contents
			sim_passwords.push_back(password);
			least_diff = 0;
			break;  // since exact match found, done reading
		} else {
			// absolute value needed to ensure length diff is positive
			int len_diff = abs(input.size() - password.size());
			
			// finds the length of the shortest of the two strings
			int len_for_comp = shorter_str_len(input, password);
			for (int i = 0; i < len_for_comp; i++) {
				bool is_same = (input[i] == password[i]);  // compare by letter
				if (is_same == false) {
					p_diff += 1;  // increments by 1 for each diff
				}
			}
			p_diff += len_diff;
		}
		if (p_diff == least_diff) {
			sim_passwords.push_back(password);
		} else if (p_diff < least_diff) {
			sim_passwords.clear();
			sim_passwords.push_back(password);
			least_diff = p_diff;  // reassign least_diff
		}
	}
	sort(sim_passwords.begin(), sim_passwords.end());  // sort alphabetically
	cout << "The most similar passwords to " << input << " are:" << endl;
	for (auto match : sim_passwords) {
		cout << match << ", ";
	}
	cout << endl;
	cout << "All of which are " << least_diff << " character(s) different." << endl;
}
