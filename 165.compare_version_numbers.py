'''
165. Compare Version Numbers
Solved
Medium
Topics
Companies
Hint

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.



Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".



Constraints:

    1 <= version1.length, version2.length <= 500
    version1 and version2 only contain digits and '.'.
    version1 and version2 are valid version numbers.
    All the given revisions in version1 and version2 can be stored in a 32-bit integer.

'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        def remove_leading_zeros(version):
            for i,x in enumerate(version):
                version[i] = str(int(x))
            #return version
        remove_leading_zeros(version1)
        remove_leading_zeros(version2)
        #print(version1)
        #print(version2)
        max_len = max(len(version1), len(version2))
        def extend_version(version, max_len):
            extend_by = max_len - len(version)
            for i in range(extend_by):
                version.append('0')
        if len(version1)!=max_len:
            extend_version(version1, max_len)
        else:
            extend_version(version2, max_len)
        #print(version1)
        #print(version2)
        def compare(version1, version2):
            for i in range(len(version1)):
                if int(version1[i]) < int(version2[i]):
                    return -1
                elif int(version1[i]) > int(version2[i]):
                    return 1
            return 0
        return compare(version1, version2)
