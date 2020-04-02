package pack.model1;

public class ExamWriterImpl implements ExamWriter{
	public String getName(String name) {
		String s = "작성자 : " + name;
		return s;
	}
}
