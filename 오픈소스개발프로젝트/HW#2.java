/*****************************
* ���α׷��� : ����������α׷�
* �ۼ��� : 2019038004_���ο�
* �ۼ��� : 2020.09.19
*���α׷� ���� : ������ ������ �Է¹޾� ������ ����մϴ�.
*********************************/
import java.util.Scanner;


public class Main {
	 public static float sum(float m, float n)
	 {
		 return m + n;
	 }
	 public static void main(String args[]) 
	 {
		 Scanner SC = new Scanner(System.in);
	     System.out.println("�̸�, �й�, ������ ������� �Է��ϼ���. (����, ����, ����, C���)");
	     String num = SC.next();
	     String name = SC.next();
	     float kor = SC.nextFloat();
	     float eng = SC.nextFloat();
	     float math = SC.nextFloat();
	     float clan = SC.nextFloat();
	     System.out.println("�̸� : " + name);
	     System.out.println("�й� : " + num);
	     float result = sum (kor, eng);
	     result = sum(result, math);
	     result = sum(result, clan);
	     System.out.println("���� : " + result);
	     float ave = (float)result;
	     ave /= 4;
	     System.out.println("��� : " + ave);
	     String hak;
	     if (ave >= 4.5)
	     {
	    	 hak = "A+";
	     }
	     else if (ave >= 4.0)
	     {
	    	 hak = "A0";
	     }
	     else if (ave >= 3.5)
	     {
	    	 hak = "B+";
	     }
	     else if (ave >= 3.0)
	     {
	    	 hak = "B0";
	     }
	     else if (ave >= 2.5)
	     {
	    	 hak = "C+";
	     }
	     else if (ave >= 2.0)
	     {
	    	 hak = "C0";
	     }
	     else if (ave >= 1.5)
	     {
	    	 hak = "D+";
	     }
	     else
	     {
	    	 hak = "F";
	     }
	     System.out.println("���� : " + hak);
	 }
}
