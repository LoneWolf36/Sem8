import java.io.*;
import java.net.*;
import java.lang.Math;

class RSA_B {
	public static void main(String[] args)throws Exception {
		int e,n,plaintext;
		double C = 0.0;
		String returnMessage;

		Socket bob_socket = new Socket("localhost",5000);
		InputStream is = bob_socket.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);
		BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

		//receiving g,n and A from alice
		e = Integer.parseInt(br.readLine());
		n = Integer.parseInt(br.readLine());
		System.out.println("e sent = "+e);
		System.out.println("n sent = "+n);

		System.out.println("Enter plaintext");
		plaintext = Integer.parseInt(userInput.readLine());
		C = Math.pow(plaintext,e) % n;

		//sending B to alice
		returnMessage = Double.toString(C) + "\n";
		OutputStream os = bob_socket.getOutputStream();
    OutputStreamWriter osw = new OutputStreamWriter(os);
    BufferedWriter bw = new BufferedWriter(osw);
    bw.write(returnMessage);
		bw.flush();

		bob_socket.close();

	}
}
