import java.io.PrintWriter;
import java.net.Socket;

public class NetTest3Client {
	public static void main(String[] args) {
		// Client
		try {
			Socket socket = new Socket("192.168.0.66", 9999);
			
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true	);
			out.println("hello world" + "\n");
			
			out.close();
			socket.close();
			
		} catch (Exception e) {
			System.out.println("Client err\t" + e);
			e.printStackTrace();
		} 
		
		
		
	}
}
