package pack6;

public class InterVolMain {
	public static void main(String[] args) {
		InterRadio radio = new InterRadio();
		radio.volUp(5);
		radio.volDown(2);
		radio.show();
		radio.volOff();
		radio.volResume();
	}
}
