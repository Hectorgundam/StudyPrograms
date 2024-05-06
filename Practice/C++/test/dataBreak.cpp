
// Including the standard input and output library boiler plate for most programs 
#include <iostream>

//Including the vector container library 
#include <vector>

//Containing 
#include <algorithm>

using namespace std;

// We receive the variable str (a vector class string containing the string we need to split and organize)
// and the string range_str that contains the alternating ranges we will be using for variables start_len and end_len
vector<string> split_string(string str, string range_str) {

// Testing improvement start

// Checking if the input string is empty, if it’s empty then
    if (str.empty()) {

        // Print out that the string is empty
        cout << "The input string is empty." << endl;

        // End the function by returning an empty vector
        return vector<string>(); 
    }

// Testing improvement end 

 // 1. Declare variables which will be used or returned.
 // Vector class string result that will be returned once the process is finalized
 vector<string> result;

// Declaring the variables start_len and end_len that will store the alternating ranges that will be used to split the
 int start_len, end_len;

 // 2. Parse the range_str for the function
 // Reading the contents of range_str (our ranges) and separating the contents to be stored into our two length variables
 // First case is ("4-6"), meaning that our ranges should be start_len=4 and end_len=6
 // Second case is ("1-5"), meaning that our ranges should be start_len=1 and end_len=5
 sscanf(range_str.c_str(), "%d-%d", &start_len, &end_len);

 // 3. Remove whitespaces from the string
 // Removing whitespaces from the input string 
 str.erase(remove(str.begin(), str.end(), ' '), str.end());

 // 4. Loop through the string
 // Variable pos is being used as a counter to interate through the string 
 int pos = 0;

 // New approach start 

// Testing using a boolean variable as sort of a toggle switch
// Initializing it as true to let so the program knows to use the start_len first 
// Later on false would mean NOT to use the start_len and use the end_len instead 
bool useStartLen = true; 

// New approach end

// Loop that runs while the value of pos is less than the length of the string str 
// It runs until it reaches the end of the initial string 
 while (pos < str.length()) {

    // 5. Determine the length of the next word

        // Original given solution start

    // Variable len will be random value within the specified range 
    // Here is where we start running into an issue since it shouldn't be a random value in between
    // The value SHOULD be one of the two
    // ISSUE
    // int len = rand() % (end_len - start_len + 1) + start_len;

    // Original given solution end 

    // New approach start 

    // If the useStartLen boolean value is true we use the value of start_len 
    // Otherwise we use the value of end_len 
    int len = useStartLen ? start_len : end_len; 

    // Toggle the "switch" of our boolean useStartLen to it's opposite value 
    useStartLen = !useStartLen;

    // New approach end


    // 6. Make sure we don't go past the end of the string
    // Making sure that the we don't go past the length of the string once the end is reached 
    if (pos + len > str.length()) {

        len = str.length() - pos;

    }

    // 7. Add the word to the result array
    // Extracting a substring of the determined length from the current position and storing it in word 
    string word = str.substr(pos, len);
    // And adding that word (string) to the result vector 
    result.push_back(word);

    // Updating the position value by increasing it by the length of the substring that was extracted (word)
    pos += len;

 }

 // 8. Sort the words using a custom comparison function
// Custom comparison function to sort the substrings 
// Custom order:
// Numbers
// Uppercase letters 
// 
 std::sort(result.begin(), result.end(), [](const string& a, const string& b) {

    // Iterators that will be used to iterate through the strings a and b 
    // ita currently "points" to the first character of string a 
    // itb current "points" to the first character of string b 
    string::const_iterator ita = a.begin(), itb = b.begin();

    // While loop to cycle through and compare the characters of strings a and b 
    while (ita != a.end() && itb != b.end()) {

        // Checking if the current character of string a IS a number AND the current character of string b is NOT a number 
        if (isdigit(*ita) && !isdigit(*itb)) {
            return true; // Giving priority to digits over non-digits

        // Checking if the current character of string a is NOT a number and the current character of string b IS a number
        } else if (!isdigit(*ita) && isdigit(*itb)) {
            return false; // Non-digits are deemed greater than digits 

        // Checking if the current character of string a IS an uppercase letter and the current character of string b is NOT an uppercase letter 
        } else if (isupper(*ita) && !isupper(*itb)) {
            return true; // Giving priority to uppercase letters over lowercase letters 

        // Checking it the current character of string a is NOT an uppercase letter and the current character of string b IS an uppercase letter
        } else if (!isupper(*ita) && isupper(*itb)) {
            return false; // Lowercase letters are deemed greater than uppercase 

        // If the current character of string a is lesser than the current character of string b
        } else if (*ita < *itb) {
            return true;

        // If the current character of string a is greater than the current character of string b
        } else if (*ita > *itb) {
            return false;

        } else {

            // Moving to the next character in string a
            ++ita;

            // Moving to the next character in string b 
            ++itb;
        }
    }

    // Compares the lengths of string a and string b if all other factors are equal 
    // and returns whether or not the length of a is less than the length of b 
    // ISSUE
    // On the assumptions section of the prompt it states that: 
    // The shortest word must appear at the end of the output array
    // Wouldn't this make it so that this is the opposite since it's show that smaller ones go first? 
    // Need to look more into this part 
    
    // Original given solution end 
    //return a.length() < b.length();
    // Original given solution end 

    // New approach start

    // This should add a final criteria that the shortest words will appear at the end of the output array 
    // This comes into effect if all other sorting criteria has already been exhausted and it comes to
    // this being the tie breaker 
    return a.length() > b.length();

    // New approach end

 });

 // 9. Return the result computed
 // Returns the result vector of strings once it has been split and sorted 
 return result;

}

// Main function 
int main() {

// The string that will be used

// TEST CASE 1 string
string str = "abcdEfghijklmnoPqrsTuvwxyz";

 // TEST CASE 2 string
 //string str = "hellomywonderfulfriend2000";

// TEST CASE 3 string
//string str = "";

// TEST CASE 4 string
//string str = "hellomywonderfulfriend2000";

// The ranges that we will be working with 

// TEST CASE 1 range
string range_str = "4-6";

 // TEST CASE 2 range
 //string range_str = "1-5";

 // TEST CASE 3 range 
 //string range_str = "1-5";

 // TEST CASE 4 range 
 //string range_str = "";

// The vector class string result will contain the returned results after the split_string function has been called 
 vector<string> result = split_string(str, range_str);

// Loop that cycles through the result vector printing out each substring within it
 for (const auto& word : result) {

 cout << word << " ";
 
 }

// Printing out a new line at the end of spacing aesthetic purposes 
 cout << endl;


// Indicates the completion of the program / ends the program 
 return 0;

}