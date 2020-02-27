import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class NetTest3Server {
	
	
	public static void main(String[] args) {
		// Echo Server
		ServerSocket ss = null;
		
		/*
		for (int i = 0; i < 65536; i++) {
			try {
				ss = new ServerSocket(i);
				ss.close();
			}catch (Exception e) {
				System.out.println(i + "번째 포트 사용 중");
			}
		}
		System.out.println("확인 종료");
		*/
		
		Socket socket = null;
		try {
			ss = new ServerSocket(9999);
			System.out.println("서버 서비스 중...");
			socket = ss.accept(); // 클라이언트 요청을 기다림
			System.out.println("접속자 정보 : " + socket.toString());
			
			BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			String msg = reader.readLine();
			System.out.println("수신 자료 : " + msg);
			
			reader.close();
			socket.close();
			ss.close();
			System.out.println("서버 종료");
			
		}catch (Exception e) {
			System.out.println("server err\t" + e);
			e.printStackTrace();
		}
	}
}
