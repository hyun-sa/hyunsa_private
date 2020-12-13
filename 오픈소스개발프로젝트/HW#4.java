/*****************************
* 프로그램명 : 학점출력프로그램
* 작성자 : 2019038004_조민우
* 작성일 : 2020.09.28
*프로그램 설명 : 성적과 정보를 5번 입력받아 정보를 출력합니다.
*********************************/
import java.util.Scanner;


public class Main {
	 public static float sum(float m, float n)
	 {
		 return m + n;
	 }
	 public static void input(int n)
	 {
		 Scanner SC = new Scanner(System.in);
	     System.out.println("학생의 이름, 학번, 성적을 순서대로 입력하세요. (국어, 영어, 수학, C언어)");
	     String num = SC.next();
	     String name = SC.next();
	     float kor = SC.nextFloat();
	     float eng = SC.nextFloat();
	     float math = SC.nextFloat();
	     float clan = SC.nextFloat();
	     float result = sum (kor, eng);
	     result = sum(result, math);
	     result = sum(result, clan);
	     float ave = (float)result;
	     ave /= 4;
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
		 if (n > 0)
		 {
			 input(n-1);
		 }
	     System.out.println("이름 : " + name + " 학번 : " + num + " 총점 : " + result + " 평균 : " + ave + " 학점 : " + hak);
	 }
	 
	 
	 public static void main(String args[]) 
	 {
		 input(4);
	 }
}
