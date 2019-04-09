import java.io.*;
import java.lang.Math;

class DES {
  static int plaintext[] = {0,1,1,0,1,1,0,1};
  static int ciphertext[] = new int[8];
  public static void main(String[] args) {

    DES obj = new DES();

    System.out.println("PT : ");
    obj.printArray(plaintext);

    ciphertext = obj.DES(plaintext,0);
    System.out.println("CT : ");
    obj.printArray(ciphertext);

    plaintext = obj.DES(ciphertext,1);
    System.out.println("PT : ");
    obj.printArray(plaintext);

  }

  public int[] fk(int right[], int key[]) {

    int postEP[] = new int[8];
    int postXOR[] = new int[8];
    int postSBox[] = new int[4];
    String postBox;
    int postP4[] = new int[4];

    int i;
    String r1,c1,r2,c2;
    int rs0,cs0,rs1,cs1;

    //applying EP on the right half of array
    for(i=0;i<8;i++)
      postEP[i] = right[Tables.EP[i]-1];

    System.out.println("post EP : ");
    printArray(postEP);

    //XOR with k1
    for(i=0;i<8;i++)
      postXOR[i] = postEP[i] ^ key[i];

    System.out.println("post XOR : ");
    printArray(postXOR);
    //applying s0 and s1
    r1 = String.valueOf(postXOR[0])+String.valueOf(postXOR[3]);
    r2 = String.valueOf(postXOR[4])+String.valueOf(postXOR[7]);
    c1 = String.valueOf(postXOR[1])+String.valueOf(postXOR[2]);
    c2 = String.valueOf(postXOR[5])+String.valueOf(postXOR[6]);

    System.out.println(r1 +" "+ c1+ "\n"+ r2+" "+c2);

    rs0 = Integer.parseInt(r1,2);
    rs1 = Integer.parseInt(r2,2);
    cs0 = Integer.parseInt(c1,2);
    cs1 = Integer.parseInt(c2,2);

    System.out.println(rs0 +" "+ cs0+ "\n"+ rs1+" "+cs1);

    postBox = Tables.S0[rs0][cs0].concat(Tables.S1[rs1][cs1]);

    for(i = 0;i<4;i++)
      postSBox[i] = Character.getNumericValue(postBox.charAt(i));

    System.out.println("post sbox : ");
    printArray(postSBox);

    for(i=0;i<4;i++)
      postP4[i] = postSBox[Tables.P4[i]-1];

    System.out.println("post P4 : ");
    printArray(postP4);

    return postP4;
  }


  public int[] DES(int arr[], int mode) {
    int postIP[] = new int[8];
    int left[] = new int[4];
    int right[] = new int[4];
    int temp[] = new int[4];
    int retArr[] = new int[8];
    int k1[] = {1,0,1,0,0,1,0,0};
    int k2[] = {0,1,0,0,0,0,1,1};
    int i;
    //applying IP
    for(i=0;i<8;i++) {
      postIP[i] = arr[Tables.IP[i]-1];

      if(i<4)
        left[i] = postIP[i];
      else
        right[i-4] = postIP[i];
    }

    System.out.println("post IP : ");
    printArray(postIP);

    System.out.println("before swap");
    if(mode == 0)
      temp = fk(right,k1);
    else
      temp = fk(right,k2);

    //XOR with old left
    for(i=0;i<4;i++) {
      left[i] = left[i] ^ temp[i];
    }

    //swap new left and old right
    for(i=0;i<4;i++) {
      temp[i] = left[i];
      left[i] = right[i];
      right[i] = temp[i];
    }

    System.out.println("after swap");
    if(mode == 0)
      temp = fk(right,k2);
    else
      temp = fk(right,k1);

    for(i=0;i<4;i++) {
      left[i] = left[i] ^ temp[i];
    }

    for(i = 0;i<4; i++) {
      postIP[i] = left[i];
      postIP[i+4] = right[i];
    }

    for(i=0;i<8;i++) {
      retArr[i] = postIP[Tables.IPinv[i]-1];
    }

    return retArr;
  }

  public void printArray(int arr[]) {
    for(int i=0; i < arr.length; i++) {
      System.out.print(arr[i] + "\t");
    }
    System.out.print("\n");
  }

}

class Tables {
  static int IP[] = {2,6,3,1,4,8,5,7};
  static int EP[] = {4,1,2,3,2,3,4,1};
  static String S0[][] = {{"01","00","11","10"},{"11","10","01","00"},{"00","10","01","11"},{"11","01","11","10"}};
  static String S1[][] = {{"00","01","10","11"},{"10","00","01","11"},{"11","00","01","00"},{"10","01","00","11"}};
  static int P4[] = {2,4,3,1};
  static int IPinv[] = {4,1,3,5,7,2,8,6};
}
