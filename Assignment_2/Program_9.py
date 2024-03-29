from collections import Counter


s = "ADCFEBECEABEBADFCDFCBFCBEAD"
t = "ABCA"

def contains_all(freq1, freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True

def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n+1
    for length in range(1, n+1):
        freqs = Counter()
        satisfied = 0
        for ch in s[:length]:
            freqs[ch] += 1
            if ch in freqt and freqs[ch] == freqt[ch]:
                satisfied += 1
        if satisfied == len(freqt) and length < end-start:
            start, end = 0, length
        for i in range(1, n-length+1):
            freqs[s[i+length-1]] += 1
            if s[i+length-1] in freqt and freqs[s[i+length-1]] == freqt[s[i+length-1]]:
                satisfied += 1
            if s[i-1] in freqt and freqs[s[i-1]] == freqt[s[i-1]]:
                satisfied -= 1
            freqs[s[i-1]] -= 1
            if satisfied == len(freqt) and length < end-start:
                start, end = i, i+length
    return s[start:end] if end-start <= n else ""

print(min_window(s,t))