package pack;

import java.io.File;

import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.util.FileCopyUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class DownloadController {
	
	@RequestMapping("download")
	@ResponseBody
	public byte[] getDown(HttpServletResponse response, @RequestParam String filename) throws Exception{
		System.out.println("filename : " + filename);
		
		File file = new File("c:/work/upload/" + filename);
		byte[] bytes = FileCopyUtils.copyToByteArray(file);
		
		String fn = new String(file.getName().getBytes(), "utf-8"); //한글처리
		
		//전송되는 파일명 명시
		response.setHeader("Content-Disposition", "attatchment;filename=\"" + fn + "\"");
		response.setContentLength(bytes.length);
		
		return bytes;
	}
}
