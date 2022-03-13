#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
int dp[1 << 21][51];
int n, m;
pair<int, int> a[51];
int func(int state, int pos) {
    if (pos == m)return 0;
    int &ret = dp[state][pos];
    if (ret != -1)return ret;
    int x = a[pos].first;
    int y = a[pos].second;
    if (!((1 << x)&state) && !((1 << y)&state)) {
        ret = max(ret, func(state | (1 << x) | (1 << y), pos + 1) + 2);
    }
    return ret = max(ret, func(state, pos + 1));
}
int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++) 
        scanf("%d%d", &a[i].first, &a[i].second);
    memset(dp, -1, sizeof(dp));
    int res = func(0, 0);
    if (res != n)res++;
    printf("%d\n", res);
    return 0;
}