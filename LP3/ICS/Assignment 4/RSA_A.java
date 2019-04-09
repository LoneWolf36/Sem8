import java.io.*;
import java.net.*;
import java.lang.Math;
import java.math.*;

class RSA_A {
	public static void main(String[] args)throws Exception {
		int p,q,n,e,d,i,fn,temp;
		BigI
		double  C= 0.0, P=0.0;
		String returnMessage;
		boolean found = false;

		ServerSocket alice_sock = new ServerSocket(5000);
		BufferedReader usr = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter p");
		p = Integer.parseInt(usr.readLine());
		System.out.println("Enter q");
		q = Integer.parseInt(usr.readLine());
		System.out.println("Enter e");
		e = Integer.parseInt(usr.readLine());
		n = p*q;
		fn = (p-1)*(q-1);
		i = 1;
		d = 1;

		while(!found) {
			temp = fn*i + 1;
			// System.out.println("temp = "+temp);
			if(temp % e ==0) {
				d = temp/e;
				found = true;
			}
			i++;
		}
		System.out.println("d = "+d);
		//sending e,n to bob
		returnMessage = Integer.toString(e) + "\n" + Integer.toString(n) + "\n";
		Socket sock = alice_sock.accept();
		OutputStream os = sock.getOutputStream();
    OutputStreamWriter osw = new OutputStreamWriter(os);
    BufferedWriter bw = new BufferedWriter(osw);
    bw.write(returnMessage);
		bw.flush();

		InputStream is = sock.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		BufferedReader br = new BufferedReader(isr);

		C = Double.parseDouble(br.readLine());
		System.out.println("CT from Bob = "+C);

		P = Math.pow(C,d) % n;
		System.out.println("PT = "+P);
		sock.close();
	}
}
