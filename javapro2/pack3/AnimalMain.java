package pack3;

public class AnimalMain {

	public static void main(String[] args) {
		Animal tiger = new Animal();
		tiger.display();
		tiger.display(5);
		tiger.display("호랑이");
		tiger.display("호랭이", 2);
		tiger.display(3, "호돌이\n");
		
		Animal dog = new Animal();
		dog.display();
				
		Animal hen = new Animal(2);
		hen.display();
		
		Animal wolf = new Animal("늑대");
		wolf.display();
	}

}
