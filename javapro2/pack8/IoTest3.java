package pack8;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;


/**1Byte 단위로 데이터 입출력 : text, image, media file 등을 처리*/
public class IoTest3 {
	
	
	public void write_file(File file, ArrayList<String> str_list) {
		try {
			BufferedWriter writer = new BufferedWriter(
										     new OutputStreamWriter(new FileOutputStream(file), "UTF-8"));
			for(String str:str_list) {
				writer.write(str, 0, str.length()); // 쓸 문장, 시작위치, 끝위치
				writer.newLine(); //다음줄
			}
			writer.close();
		}catch (Exception e) {
			System.out.println("writer_file err\t"+ e);
		}
		System.out.println("저장 성공");
	}
	public void read_file(File file) {
		try {
			StringBuffer buffer = new StringBuffer();
			BufferedReader reader = new BufferedReader(
											   new InputStreamReader(new FileInputStream(file)));
			String oneLine;
			while((oneLine = reader.readLine()) != null) {
				buffer.append(oneLine + "\n");
			}
			
			reader.close();
			System.out.println(buffer.toString());
		}catch (Exception e) {
			System.out.println("read_file err\t"+ e);
		}
		System.out.println("읽기 성공");
	}
	
	
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>();
		list.add("자바");
		list.add("파이썬");
		list.add("C-language");
		
		File file = new File("c:/work/abc.txt");
		IoTest3 test3 = new IoTest3();
		test3.write_file(file, list);
		test3.read_file(file);		
	}
}
