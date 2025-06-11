P1, M1 = 31, 10**9 + 7  # First base and mod
P2, M2 = 53, 10**9 + 9  # Second base and mod:w

def check(length,  n1, n2):
    """Time complexity: O(n1+n2)"""
    if length == 0:
        return True
    if length > min(n1, n2):
        return False

    # Calculate initial hash for the first substring of s1
    h1_s1, h2_s1 = 0, 0
    p1_pow, p2_pow = 1, 1

    for i in range(length):
        h1_s1 = (h1_s1 * P1 + ord(s1[i])) % M1
        h2_s1 = (h2_s1 * P2 + ord(s1[i])) % M2
        if i < length - 1:
            p1_pow = (p1_pow * P1) % M1
            p2_pow = (p2_pow * P2) % M2
    
    # Store hashes of all substrings of s1 of the given length
    hashes_s1 = {(h1_s1, h2_s1)}

    # Roll the hash for the rest of s1's substrings
    for i in range(length, n1):
        h1_s1 = ((h1_s1 - ord(s1[i - length]) * p1_pow) * P1 + ord(s1[i])) % M1
        h2_s1 = ((h2_s1 - ord(s1[i - length]) * p2_pow) * P2 + ord(s1[i])) % M2
        hashes_s1.add((h1_s1, h2_s1))

    # Calculate initial hash for the first substring of s2
    h1_s2, h2_s2 = 0, 0
    for i in range(length):
        h1_s2 = (h1_s2 * P1 + ord(s2[i])) % M1
        h2_s2 = (h2_s2 * P2 + ord(s2[i])) % M2

    # Check if the first hash of s2 exists in s1's hashes
    if (h1_s2, h2_s2) in hashes_s1:
        return True

    # Roll the hash for the rest of s2's substrings and check for a match
    for i in range(length, n2):
        h1_s2 = ((h1_s2 - ord(s2[i - length]) * p1_pow) * P1 + ord(s2[i])) % M1
        h2_s2 = ((h2_s2 - ord(s2[i - length]) * p2_pow) * P2 + ord(s2[i])) % M2
        if (h1_s2, h2_s2) in hashes_s1:
            return True
    
    return False

def longest_common_substring(s1, s2):
    """Time complexity: O((n1+n2)*log(min(n, m))) which can be represented as O(n log n)"""
    n1, n2 = len(s1), len(s2)

    # Binary search for the longest possible length
    left, right = 0, min(n1, n2)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid, n1, n2):
            ans = mid  # mid is a possible answer, try for a longer one
            left = mid + 1
        else:
            right = mid - 1 # mid is too long, try for a shorter one
            
    return ans


s1 = "abcdefgh"
s2 = "cde"

result = longest_common_substring(s1, s2)
print(f"The first string is: '{s1}'")
print(f"The second string is: '{s2}'")
print(f"Length of the Longest Common Substring is: {result}")

print("-" * 20)

s1 = "abcdefghijkl"
s2 = "cdefgahijk"

result = longest_common_substring(s1, s2)
print(f"The first string is: '{s1}'")
print(f"The second string is: '{s2}'")
print(f"Length of the Longest Common Substring is: {result}")

