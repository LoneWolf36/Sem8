import java.io.*;
import java.net.*;
import java.lang.Math;

class DiffA {
	public static void main(String[] args)throws Exception {
		int n,g,un,k,x;
		double A = 0.0, B, k1 = 0.0;
		String returnMessage;
		n = 7;
		g = 1;
		int rem_array[] = new int[n-1];
		boolean found = false;
		boolean equal = false;

		//finding generator g for n
		while(g<n && !found) {
			System.out.println("trying for g = "+g);
			for(int j=1;j<n;j++) {
				rem_array[j-1] = (int)Math.pow(g,j) % n;
				System.out.print(rem_array[j-1]+"\t");
			}
			System.out.println("");
			for(int j=0;j<n-2;j++) {
				equal = false;
				k = j+1;
				while(!equal && k<n-1) {
					if(rem_array[j] == rem_array[k]) {
						equal = true;
					}
					k++;
				}
				if(equal)
					break;
			}
			if(!equal) {
				System.out.println("g = "+g);
				found = true;
				break;
			}
			g++;
		}
		ServerSocket alice_sock = new ServerSocket(5000);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter X");
		x = Integer.parseInt(br.readLine());
		A = Math.pow(g,x) % n;
		
		//sending g,n and A to bob
		returnMessage = Integer.toString(g) + "\n" + Integer.toString(n)+"\n" + Double.toString(A) + "\n";
		Socket sock = alice_sock.accept();
		OutputStream os = sock.getOutputStream();
        OutputStreamWriter osw = new OutputStreamWriter(os);
        BufferedWriter bw = new BufferedWriter(osw);
        bw.write(returnMessage);
		bw.flush();

		//reading B from bob
		InputStream is = sock.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader fromBob = new BufferedReader(isr);

		B = Double.parseDouble(fromBob.readLine());

		sock.close();
		k1 = Math.pow(B,x) % n;
		System.out.println("K1 = "+k1);
	}
}
