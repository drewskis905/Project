# Andrew Pham
def cargo(crates, T, W, D):
    dp = [[[0 for _ in range(D + 1)] for _ in range(W + 1)] for _ in range(T + 1)]
    crate_counts = []
    for crate in crates:
        t_count = crate.count('t')
        w_count = crate.count('w')
        d_count = crate.count('d')
        crate_counts.append((t_count, w_count, d_count))
    for t_cost, w_cost, d_cost in crate_counts:
  
        for t in range(T, t_cost - 1, -1):
            for w in range(W, w_cost - 1, -1):
                for d in range(D, d_cost - 1, -1):
                    dp[t][w][d] = max(dp[t][w][d], dp[t - t_cost][w - w_cost][d - d_cost] + 1)
    return dp[T][W][D]