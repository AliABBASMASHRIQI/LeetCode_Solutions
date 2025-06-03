emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
class Solution:
    def numUniqueEmails(self, emails) -> int:
        res_set = set()
        for address in emails:
            local,domain = address.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            clean_address = local+"@"+domain
            res_set.add(clean_address)
        print(len(res_set))
        return len(res_set)
                
                
            
       
       
sol = Solution()
sol.numUniqueEmails(emails) 