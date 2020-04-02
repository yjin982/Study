package other;

import java.io.FileWriter;

public class OutFileImpl implements OutFileInter{
	private String filePath;
	
	public void setFilePath(String filePath) {
		this.filePath = filePath; //경로 및 파일명을 얻기 위한 setter
	}
	
	public void outFile(String msg) {
		//메세지를 파일로 출력
		try {
			FileWriter writer = new FileWriter(filePath);
			writer.write(msg);
			writer.close();
			System.out.println("파일 저장 성공");
		}catch (Exception e) {
			System.out.println("outFile err " + e);
		}
	}
	
	public void etc() {/*여러가지 메소드가 있다는 것을 보여주기 위해서 */}
}
