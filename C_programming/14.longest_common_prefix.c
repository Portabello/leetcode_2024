/*
14. Longest Common Prefix
Solved
Easy
Topics
premium lock iconCompanies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

*/
char* longestCommonPrefix(char** strs, int strsSize) {
    char **itr = strs;
    static char ans[200];
    ans[0] = '\0';
    int ans_len=0;
    int index=0;

    // empty array of strings
    if (strsSize == 0) return ans;

    // first string is empty => prefix is ""
    if (strs[0] == NULL || strs[0][0] == '\0') return ans;
    if (strsSize == 1) return strs[0];

    while(1){
        char cur=0;
        int keep_going = 0;
        if (itr[0][index] == '\0') break;
        for(int i=0; i<strsSize; i++){
            if(i==0)
                cur=itr[i][index];
            else{
                if (itr[i][index]!=cur){
                    keep_going = 1;
                    break;
                }
            }
            printf("%s  -   %c\n",itr[i], cur);
        }

        if(keep_going == 1)
            break;
        ans[ans_len] = itr[0][index];
        itr=strs;
        index ++;
        ans_len++;
    }
    ans[ans_len]='\0';
    return ans;
}
