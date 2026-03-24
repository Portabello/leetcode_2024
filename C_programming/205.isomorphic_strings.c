/*
205. Isomorphic Strings
Solved
Easy
Topics
premium lock iconCompanies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

*/
#include <ctype.h>
bool isIsomorphic(char* s, char* t) {
    struct mapping {
        char key;
        char value;
    };
    int str_len = strlen(s);
    struct mapping map[128];
    int map_len = 0;
    for (int i = 0; i < str_len; i++) {
        //check if mapping exists & if its valid
        bool mapping_exists = false;
        for (int j = 0; j <= map_len; j++) {
            //found mapping
            if (s[i] == map[j].key) {
                mapping_exists = true;
                if (t[i] != map[j].value) {
                    return false;
                }
            }
            //key already mapped to
            if (t[i] == map[j].value && map[j].key != s[i]) return false;
        }
        //make mapping if not already mapped
        if (mapping_exists == false){
            //printf("mapping %c -> %c\n", s[i], t[i]);
            map[map_len].key = s[i];
            map[map_len].value = t[i];
            map_len++;
        }
    }
    return true;
}
