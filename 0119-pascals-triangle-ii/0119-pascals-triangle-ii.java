class Solution {
    public List<Integer> getRow(int rowIndex) {
        int arr[][] = new int[rowIndex + 1][];
        for (int i = 0; i <= rowIndex; i++) {
            arr[i] = new int[i + 1]; 
            arr[i][0] = arr[i][i] = 1;
            for (int j = 1; j < i; j++) {
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i <= rowIndex; i++) {
            list.add(arr[rowIndex][i]);
        }
        
        return list;
    }
}