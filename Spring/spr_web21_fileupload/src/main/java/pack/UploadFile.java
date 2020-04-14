package pack;

import org.springframework.web.multipart.MultipartFile;

public class UploadFile { // file처리용 DTO
	private MultipartFile file;
	//여러 개의 파일을 처리한다면 List<MultipartFile> files와 같이 선언함
	
	public MultipartFile getFile() {
		return file;
	}
	
	public void setFile(MultipartFile file) {
		this.file = file;
	}
}
