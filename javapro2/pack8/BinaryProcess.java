package pack8;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class BinaryProcess {
	public static void main(String[] args) throws Exception {
		BinaryData data = new BinaryData();
		
		//이진 자료 파일로 저장
		File dir = new File("c:/work/");
		File file = new File(dir, "abcbi.data"); // 경로와 파일명 구분
		FileOutputStream fo = new FileOutputStream(file);
		BufferedOutputStream bo = new BufferedOutputStream(fo, 1024);
		ObjectOutputStream oo = new ObjectOutputStream(bo);
		
		oo.writeObject(data);
		
		oo.close();
		bo.close();
		fo.close();
		System.out.println("저장 성공\n");
		
		
		//이진 자료 파일로 읽기
		File file2 = new File("c:/work/abcbi.data"); // 경로와 파일명 구분
		FileInputStream fi = new FileInputStream(file2);
		BufferedInputStream bi = new BufferedInputStream(fi, 1024);
		ObjectInputStream oi = new ObjectInputStream(bi);
		Object obj = oi.readObject();
		BinaryData data2 = (BinaryData) obj;
		
		System.out.println(data2.i + "   " + data2.d + "   " + data2.s1 + "   " + data2.s2);
		
		oi.close();
		bi.close();
		fi.close();
		System.out.println("읽기 성공");
	}
}
