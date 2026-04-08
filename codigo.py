MOD = 1010101

def count_ways(M, A, B):
    n = len(M)
    la = len(A)
    lb = len(B)

    dp = [[[0]*lb for _ in range(la)] for _ in range(n+1)]
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(la):
            for k in range(lb):
                if dp[i][j][k] == 0:
                    continue

                if M[i] == A[j]:
                    nj = (j + 1) % la
                    dp[i+1][nj][k] = (dp[i+1][nj][k] + dp[i][j][k]) % MOD

                if M[i] == B[k]:
                    nk = (k + 1) % lb
                    dp[i+1][j][nk] = (dp[i+1][j][nk] + dp[i][j][k]) % MOD

    return dp[n][0][0]


# 👇 CAMBIO AQUÍ
with open("decode.in") as f:
    for line in f:
        if line.strip() == "":
            continue
        M, A, B = line.strip().split()
        print(count_ways(M, A, B))