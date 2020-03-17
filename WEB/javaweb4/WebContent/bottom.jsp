<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<hr>
문서의 바닥글 footer &nbsp;
<% Date date = new Date(); %>
<%= date.toLocaleString() %>
<!-- page import="java.util.Date" 부분을 지워서 여기서 에러가 떠도 부르는 파일에 포함시키면 에러가 아님 -->