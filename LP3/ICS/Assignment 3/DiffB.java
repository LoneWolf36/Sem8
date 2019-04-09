import java.io.*;
import java.net.*;
import java.lang.Math;

class DiffB {
	public static void main(String[] args)throws Exception {
		int g,n,y;
		double B = 0.0, A, k2 = 0.0;
		String returnMessage;

		Socket bob_socket = new Socket("localhost",5000);
		InputStream is = socket.getInputStream();
		BufferedReader br = new BufferedReader(is);
		BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

		//receiving g,n and A from alice
		g = Integer.parseInt(br.readLine());
		n = Integer.parseInt(br.readLine());
		A = Double.parseDouble(br.readLine());
		System.out.println("Enter Y");
		y = Integer.parseInt(userInput.readLine());
		B = Math.pow(g,y) % n;

		//sending B to alice
		returnMessage = Double.toString(B) + "\n";
		OutputStream os = bob_socket.getOutputStream();
        OutputStreamWriter osw = new OutputStreamWriter(os);
        BufferedWriter bw = new BufferedWriter(osw);
        bw.write(returnMessage);
		bw.flush();

		bob_socket.close();

		k2 = Math.pow(A,y) % n;
		System.out.println("K2 = "+k2);

		
	}
}
