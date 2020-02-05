package pack8;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class IoTest1 {
	public static void main(String[] args) throws Exception {
		// 1Byte 단위의 입출력
		/*
		System.out.print("1Byte 입력 : ");
		int a = System.in.read();
		System.out.println("a:" + a + "   " + (char)a);
		*/
		
		OutputStreamWriter os = new OutputStreamWriter(System.out);
		/*
		byte b = 98; // 출력 : b
		os.write(b);
		os.flush(); // 버퍼 비우기 
		os.close(); // 메모리 해제 = 자원 해제
		*/
		BufferedWriter bw = new BufferedWriter(os, 1024); // 사이즈가 기본 1024(1kb 단위)
		PrintWriter out = new PrintWriter(bw); // 출력
		out.println(123);
		out.println("문자열 출력");
		out.close();
		bw.close();
		os.close();
//		위의 줄(os,bw,out) == System.out.println("문자열 출력");
		
		System.out.println();
		File f = new File("c:/work/iotest.txt");
		FileWriter fw = new FileWriter(f);
		BufferedWriter bw2 = new BufferedWriter(fw, 1024);
		PrintWriter out2 = new PrintWriter(bw2);
		out2.println("날씨가 춥네");
		out2.println("내일까지");
		out2.println("견디자");
		out2.close();
		bw2.close();
		fw.close();
	}
}
