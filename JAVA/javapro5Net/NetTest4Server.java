import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class NetTest4Server {
	ServerSocket ss;
	Socket socket;
	PrintWriter out;
	BufferedReader reader;
	
	
	public NetTest4Server() {
		try {
			ss = new ServerSocket(7777);
			
		}catch (Exception e) {
			System.out.println("NetTest4Server err\t" + e);
			e.printStackTrace();
			return;
		}
		System.out.println("Eco Server start...");
		
		try {
			socket = ss.accept();
			
			out = new PrintWriter(socket.getOutputStream(), true);
			reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), "euc-kr"));
			
			
		}catch (Exception e) {
			System.out.println("Server err\t" + e);
			e.printStackTrace();
		}
	}
	
	public void receiveMsg() {
		try {
			String msg = reader.readLine();
			System.out.println("receiveMsg : " + msg);
			
			out.println("from server : " + msg);
			
			reader.close();
			out.close();
			socket.close();
			ss.close();
		}catch (Exception e) {
			System.out.println("receiveMsg err\t" + e);
			e.printStackTrace();
		}
		
	}
	
	public static void main(String[] args) {
		while(true) {
			NetTest4Server server = new NetTest4Server();
			server.receiveMsg();
		}
	}
}
