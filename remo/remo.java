
class Profit {
    public static void main(String[] args)
    {
	int a[] = {110, 120, 80, 120, 10, 100};
        System.out.println(maxProfit(a));
    }

    public static int maxProfit(int stockPrices[]) {
        int maxProfit = 0;
        int minStockPrice = Integer.MAX_VALUE;

        for (int i = 0; i < stockPrices.length; i++) {
            if (stockPrices[i] < minStockPrice){
                minStockPrice = stockPrices[i];
            } else if (stockPrices[i] - minStockPrice > maxProfit) {
                maxProfit = stockPrices[i] - minStockPrice;
            }
        }
        return maxProfit;
    }

}


