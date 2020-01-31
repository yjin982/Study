package pack6;

public class VolumeMain {
	public static void main(String[] args) {
		//인터페이스 상속
//		Volume volume = new Volume();     X
		Volume volume; //까지는 가능
		
		VolumeRadio radio = new VolumeRadio();
		VolumeTv tv = new VolumeTv();
		
		radio.volumeUP(5);
		radio.volumeDown(2);
		tv.volumeUP(10);
		tv.volumeDown(3);
		
		System.out.println();
		
		volume = radio;
		volume.volumeUP(1);
		volume = tv;
		volume.volumeUP(1);
		
		System.out.println();
		
		Volume v[] = new Volume[2]; // new 는 Volume가 아니라 배열 
		v[0] = radio;
		v[1] = tv;
		
		for(Volume kbs:v)
			kbs.volumeDown(2);
	}
}
