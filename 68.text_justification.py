"""
68. Text Justification
Solved
Hard
Topics
Companies
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_len = []
        for word in words:
            words_len.append(len(word))
        #print(words)
        #print(words_len)
        ans = []
        tmp_line_len = 0
        tmp_line_words = 0
        tmp_line = []
        for i,x in enumerate(words_len):
            if tmp_line_len==0:
                tmp_line.append(words[i])
                tmp_line_len += x
                tmp_line_words += 1
            else:
                if ( tmp_line_len + (x+1) ) <= maxWidth:
                    tmp_line.append(words[i])
                    tmp_line_len += x+1
                    tmp_line_words += 1
                else:
                    #end con - add to ans - clear vars with next iteration
                    print(tmp_line, tmp_line_len)
                    if tmp_line_words == 1:
                        total_spaces = maxWidth - tmp_line_len
                        spaces = total_spaces
                        tmp_ans = tmp_line[0]+(" ")*spaces
                    else:
                        total_spaces = maxWidth - (tmp_line_len - (tmp_line_words-1))
                        #spaces = math.ceil(total_spaces/(tmp_line_words-1))
                        tmp_ans = ""
                        #print(total_spaces, spaces)

                        for y in tmp_line:
                            if tmp_line_words ==1:
                                spaces = total_spaces
                            else:
                                spaces = math.ceil(total_spaces/(tmp_line_words-1))
                            tmp_line_words -=1
                            cur_space = min(spaces, total_spaces)
                            total_spaces -= spaces
                            tmp_ans = tmp_ans + y+((" ")*cur_space)
                    #print(tmp_ans)
                    ans.append(tmp_ans)




                    tmp_line = [words[i]]
                    tmp_line_len = x
                    tmp_line_words = 1
        #end-con again - copy paste to here
        #print(tmp_line, tmp_line_len)
        if tmp_line_words == 1:
            total_spaces = maxWidth - tmp_line_len
            spaces = total_spaces
            tmp_ans = tmp_line[0]+(" ")*spaces
        else:
            """
            total_spaces = maxWidth - (tmp_line_len - (tmp_line_words-1))
            spaces = math.ceil(total_spaces/(tmp_line_words-1))
            tmp_ans = ""
            for y in tmp_line:
                cur_space = min(spaces, total_spaces)
                total_spaces -= spaces
                tmp_ans = tmp_ans + y+((" ")*cur_space)
            """
            total_spaces = maxWidth - (tmp_line_len - (tmp_line_words-1))
            spaces = math.ceil(total_spaces/(tmp_line_words-1))
            tmp_ans = ""
            #print(total_spaces)
            for y in tmp_line:
                cur_space = min(1, total_spaces)
                total_spaces -= 1
                tmp_ans = tmp_ans + y+((" ")*cur_space)
            tmp_ans = tmp_ans + total_spaces*(" ")
        #print(total_spaces, spaces)
        #print(tmp_ans)
        ans.append(tmp_ans)
        #print(ans)
        return ans
