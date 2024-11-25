def foo(arr):
    N = arr[0]
    K = arr[1]

    """
    K -> nnkln
    {
        n: 2,
        k: 1,
        l: 1
    }
    """
    k_count = {}
    for char in K:
        k_count[char] = k_count.get(char, 0) + 1

    min_window = ""
    start = 0

    # { m: 1 }  ab|cd|
    window_count = {}
    have = 0
    need = len(k_count)

    # N -> mmnpkl
    for end in range(len(N)):
        char = N[end]
        window_count[char] = window_count.get(char, 0) + 1

        if char in k_count and window_count[char] == k_count[char]:
            have += 1

        while have == need:
            window_size = end - start + 1
            substring = N[start : end + 1]

            if not min_window or window_size < len(min_window):
                min_window = substring

            window_count[N[start]] -= 1

            if N[start] in k_count and window_count[N[start]] < k_count[N[start]]:
                have -= 1

            start += 1

    return min_window
