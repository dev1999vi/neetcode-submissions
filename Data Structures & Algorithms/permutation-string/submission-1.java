class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1Freq = new int[26];
        int[] s2Freq = new int[26];
        for(int j=0;j<s1.length();j++)
            s1Freq[s1.charAt(j)-'a']++;

        if(s1.length()>s2.length())
            return false;
        int i;
        for(i=0;i<s1.length();i++) {
            s2Freq[s2.charAt(i)-'a']++;
        }
        if(isTotalFreqZero(s1Freq, s2Freq))
            return true;
        for(int j=i;j<s2.length();j++) {
            s2Freq[s2.charAt(j)-'a']++;
            if(s2Freq[s2.charAt(j-s1.length())-'a']<0)
                s2Freq[s2.charAt(j-s1.length())-'a']++;
            else
                s2Freq[s2.charAt(j-s1.length())-'a']--;
            if(isTotalFreqZero(s1Freq, s2Freq))
                return true;
        }
        return false;
    }
    public boolean isTotalFreqZero(int[] s1, int[] s2) {
        for(int j=0;j<s1.length;j++)
            if(s1[j] !=s2[j])
                return false;
        return true;
    }
}
