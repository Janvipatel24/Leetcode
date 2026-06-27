class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.put((long) num, freq.getOrDefault((long) num, 0) + 1);
        }

        int ans = 1;

        if (freq.containsKey(1L)) {
            int count = freq.get(1L);
            ans = Math.max(ans, (count % 2 == 0) ? count - 1 : count);
        }

        for (long x : freq.keySet()) {

            if (x == 1)
                continue;

            long curr = x;
            int length = 0;

            while (freq.getOrDefault(curr, 0) >= 2) {
                length += 2;

                if (curr > Math.sqrt(Long.MAX_VALUE))
                    break;

                curr = curr * curr;
            }

            if (freq.getOrDefault(curr, 0) == 1) {
                length++;
            } else {
                length--;
            }

            ans = Math.max(ans, length);
        }

        return ans;
    }
}