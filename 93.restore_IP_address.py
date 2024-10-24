'''
93. Restore IP Addresses
Solved
Medium
Topics
Companies

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]



Constraints:

    1 <= s.length <= 20
    s consists of digits only.

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = [0]
        res = []
        def bt(s, ip):
            #print('s: ',s,'  ip: ', ip)
            if len(s)==0 and ip.count('.') == 4:
                ans[0]+=1
                res.append(ip)
                return
            elif len(s)==0:
                return
            t = s[0:3]
            if len(t) == 1:
                new_ip = ip + t[0:1] + '.'
                bt(s[1:], new_ip)
            elif len(t) == 2:
                new_ip = ip + t[0:2] + '.'
                bt(s[2:], new_ip)
                new_ip1 = ip + t[0:1] + '.'
                bt(s[1:],new_ip1)
            elif len(t) == 3:
                new_ip = ip + t[0:3] + '.'
                bt(s[3:], new_ip)
                new_ip1 = ip + t[0:2] + '.'
                bt(s[2:],new_ip1)
                new_ip2 = ip + t[0:1] + '.'
                bt(s[1:],new_ip2)
            '''
            if len(t) == 4:
                new_ip = ip + t[0:] + '.'
                bt(s[4:], new_ip)
                new_ip1 = ip + t[1:] + '.'
                bt(s[3:],new_ip1)
                new_ip2 = ip + t[2:] + '.'
                bt(s[2:],new_ip2)
                new_ip3 = ip + t[3:] + '.'
                bt(s[1:],new_ip3)
            '''
        def isValidIP(ip):
            ip = ip.split('.')
            #print(ip)
            for e in ip:
                if e[0] == '0' and len(e) > 1:
                    return False
                if int(e) > 255:
                    return False
            return True
        bt(s, "")
        #print('-----------------------')
        #print(ans)
        #print(res)
        ans = 0
        valid = []
        for ip in res:
            if isValidIP(ip[:-1]):
                #print('valid ip: ', ip[:-1])
                ans += 1
                valid.append(ip[:-1])
        return valid
