package pack4;

public class EmployeeMain {
	public static void main(String[] args) {
		//임시직 : 이름, 나이, 일수, 일당
		Employee tem = new Temporary("홍길동", 23,20,150000);
		tem.print();
		
		//정규직 : 이름, 나이, 고정급
		Regular reg = new Regular("신기해", 25, 2345000);
		reg.print();
		
		//영업직 : 이름, 나이, 고정급, 실적, 수수료율
		Salesman sal = new Salesman("손오공", 27, 2890000, 30000, 0.25);
		sal.print();
		
		//관리직 : 이름, 나이, 고정급
		Manager man = new Manager("사오정", 33, 4578000);
		man.print();
	}
}
