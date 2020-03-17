<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>jsp 출발</h2>
<% // <== 스크립트릿
	String ir = "홍길동";
	//System.out.println(ir); // 콘솔로, 개발시 확인용, 배포시 삭제
	out.println(ir + "님의 홈페이지!"); //내장객체를 이용해 브라우저로 출력
	
	for(int i = 1; i < 7; i++){
		out.print("<h" + i + ">");
		out.print("jsp");
		out.print("</h" + i + ">");
	}
	out.println("출력 자료1<br>");
%>
여기는 html<br>
<% out.println("출력 자료2<br>"); %>
여기는 html<br>
<%="출력 자료3<br>" %>
<br>
<%
	int a=0, sum=0;
	do{
		a++;
		sum +=a;
	}while(a < 10);
%>
<b><%="10 까지의 합은 " + sum %></b><br>
<%=ir + "님의 전화번호는 " + tel + "<br>"  %>
<%!  // <== ! 는 클래스의 멤버 필드(전역변수)로 선언
	String tel = "02-111-1111"; //이 부분은 원래 자바&지역변수니까 선언 후 사용
	// ...
%>
<%! 
	public int add(int m, int n){
		return m+n;
	}// ! 없이 사용 불가, 메소드의 멤버로 들어가기 불가능이니까 클래스의 멤버필드로 넣어줘야함.
%>
<%= add(10,20) %>
</body>
</html>