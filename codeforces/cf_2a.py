import sys

for line in sys.stdin:
    n = int(line.strip())
    s, a = [], []
    mp = {}
    for i in range(n):
        si, ai = input().split()
        s.append(si)
        a.append(int(ai))
        if si not in mp:
            mp[si] = 0
        mp[si] += a[i]
    mx = max(mp.values())
    mp2 = {}
    ans = ""
    for i in range(n):
        if s[i] not in mp2:
            mp2[s[i]] = 0
        mp2[s[i]] += a[i]
        if mp2[s[i]] >= mx and mp[s[i]] == mx:
            ans = s[i]
            break
    print(ans)
