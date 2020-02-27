package pack6;

public class VolumeTv implements Volume{
	private int volLevel;
	
	public VolumeTv() {
		volLevel = 0;
	}
	
	
	@Override
	public void volumeUP(int level) {
		volLevel += level;
		System.out.println("TV 볼륨을 올리면 " + volLevel);
	}
	@Override
	public void volumeDown(int level) {
		volLevel -= level;
		if(volLevel < 0) volLevel = 0;
		System.out.println("TV 볼륨을 내리면 " + volLevel);
	}
}
