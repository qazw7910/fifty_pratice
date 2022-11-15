def main():
    so = Solution()
    print(so.subdomainVisits(cpdomains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        visit = {}
        for pair in cpdomains:
            count, domain = pair.split(" ")

            subs = domain.split(".")

            subs[0] = domain
            index = domain.find(".")
            subs[1] = domain[index + 1:]

            for sub in subs:
                if sub not in visit:
                    visit[sub] = int(count)
                else:
                    visit[sub] += int(count)

        pairs =[]
        for key, value in visit.items():
            pairs.append(str(value)+ " " + key)
        return pairs


if __name__ == '__main__':
    main()
