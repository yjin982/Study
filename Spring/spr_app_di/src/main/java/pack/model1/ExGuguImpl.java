package pack.model1;

public class ExGuguImpl implements ExamGugu{
	
	public ExGuguImpl() {}
	
	public void showGugu() {
		for(int i = 2; i < 10; i++) {
			for (int j = 1; j < 10; j++) {
				System.out.print(i + " * " + j + " = " + (i*j) + " | ");
			}
			System.out.println();
		}
	}
}
