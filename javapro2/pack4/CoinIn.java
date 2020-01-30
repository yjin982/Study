package pack4;

public class CoinIn {
	private int jandon = 0;
	private int coin = 0;
	private int coffee = 200;
	
	public CoinIn() {}
	
	public void setCoin(int coin) {
		this.coin = coin;
	}
	public int getCoin() {
		return coin;
	}
	
	public int getJandon() {
		return jandon;
	}
	
	public int calc(int cupCount) {
		this.jandon = this.coin - (cupCount*coffee);
		return this.jandon; 
	}
	/**
	 * public String calc(int cupCount){
	 * 		String result = "";
	 * 		this.jandon = this.coin - (this.coffee*cupCount);
	 * 		if(this.coin < 200) {
	 * 			result = "최소 금액 이상을 넣어주세요.";
	 * 		}else if(this.jandon > 0) {
	 * 			result = "커피 " + this.cupCount +"잔과 잔돈 "+ jandon +"원";
	 * 		}else{
	 * 			result = "금액이 부족합니다.";
	 * 		}
	 * 		return result;
	 * }
	 */
}
