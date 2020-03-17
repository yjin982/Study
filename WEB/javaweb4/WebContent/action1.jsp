<%@page import="java.util.Calendar"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!-- 독립적인 뷰를 제공할 것이 아니라면 html,body 태그 필요 없음, 액션태그는결과값을 보내주기때문에 import가 여기서 해야 할 필요가 있음 -->
--------------<br>
홀수 출력 <br>
<% 
	for(int i = 1; i <= 10; i++){
		if(i % 2 == 1)
			out.print(i + " ");
	}
%>
<br>
<%
	Calendar calendar = Calendar.getInstance();
	out.println(calendar.get(Calendar.DATE) + "일");

%>
<br>
--------------