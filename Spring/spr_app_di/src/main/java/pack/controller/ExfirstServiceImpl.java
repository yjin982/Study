package pack.controller;

import pack.model1.ExamGugu;
import pack.model1.ExamWriter;

public class ExfirstServiceImpl implements ExfirstService{
	private ExamGugu data;
	private ExamWriter writer;
	
	public ExfirstServiceImpl(ExamGugu data) {
		this.data = data;
	}
	
	public void setWriter(ExamWriter writer) {
		this.writer = writer;
	}
	
	public void showData() {
		System.out.println(writer.getName("정유진"));
		data.showGugu();
	}

}
