$(document).ready(function(){
	$("#addForm").hide();
	$("#delForm").hide();
	$("#code_err1").hide();
	$("#code_err2").hide();
	$("#sang_err").hide();
	$("#su_err").hide();
	$("#dan_err").hide();
	$("#dcode_err").hide();
	
	$("#btn_addSangpum").click(function(){
		$("#addForm").slideToggle("fast");
		$("#txtCode").focus();
	});
	
	$("#btn_delSangpum").click(function(){
		$("#delForm").slideToggle("fast");
		$("delCode").focus();
	});
	
	
	$("#btn_insertCancel").click(function(){  //추가 취소
		$("#txtCode").val("");
		$("#txtSang").val("");
		$("#txtSu").val("");
		$("#txtDan").val("");
		$("#addForm").slideToggle("fast");
	});
	
	$("#btn_deleteCancel").click(function(){  //삭제 취소
		$("#delCode").val("");
		$("#delForm").slideToggle("fast");
	});
	
	
	$("#btn_dispAll").click(dispAll);    //전체 자료 출력
	$("#btn_insertData").click(insertData);  //추가
	$("#btn_deleteData").click(deleteData);  //삭제
});


function dispAll(){
	$.getJSON("jq_crud_select.jsp", (data) =>{
		$("#disp").empty();
		var str = "<table border=1 style='border-collapse:collapse;'>";
		str += "<tr><th>상품명</th><th>수량</th><th>수량</th><th>단가</th></tr>";
		$.each(data, (ind, enrty) => {
			str += "<tr>";
			str += "<td>" + enrty["code"] + "</td>";
			str += "<td>" + enrty["sang"] + "</td>";
			str += "<td>" + enrty["su"] + "</td>";
			str += "<td>" + enrty.dan + "</td>";
			str += "</tr>";
		});
		str += "</table>";
		
		$("#disp").append(str);
	});
}

function insertData(){
	var code = $("#txtCode").val();
	var sang = $("#txtSang").val();
	var su = $("#txtSu").val();
	var dan = $("#txtDan").val();
	
	// 입력자료 검사 : 코드
	if(code.length < 1) { //입력 안 했을 때
		$("#code_err1").show();
		return false;
	}else {
		$("#code_err1").hide();
	}
	
	for(var i = 0; i < code.length; i++){
		var data = code.charAt(i).charCodeAt(0);  // charCodeAt() 문자열 중 하나를 아스키코드로 변환
		
		if(data < 48  || data > 57){
			$("#code_err2").show();
			return false;
		}else{
			$("#code_err2").hide();
		}
	}
	
	// 상품 검사
	if(sang.length < 1) { //입력 안 했을 때
		$("#sang_err").show();
		return false;
	}else {
		$("#sang_err").hide();
	}
	
	
	//수량 검사
	if(isNaN(su) || su.length < 1){
		$("#su_err").show();
		return false;
	}else {
		$("#su_err").hide();
	}
	
	if(isNaN(dan) || dan.length < 1){
		$("#dan_err").show();
		return false;
	}else {
		$("#dan_err").hide();
	}
	
	
	// 추가 작업 : Ajax
	$.ajax({
		type:"post",
		url:"jq_crud_ins.jsp",
		data:{"code":code,"sang":sang,"su":su,"dan":dan},
		success:(data) =>{
			if(data === "false"){
				alert("상품 추가 실패");
				return false;
			}else{
				alert("상품 추가 성공");
				$("#txtCode").val("");
				$("#txtSang").val("");
				$("#txtSu").val("");
				$("#txtDan").val("");
				$("addForm").slideToggle("fast");
				dispAll(); //추가 후 목록 보기
			}
		
		}, error:() => {
			console.log("insert err");
		}
	});
	
}
function deleteData(){
	var dcode = $("#delCode").val();
	
	if(isNaN(dcode) || dcode.length < 1){
		$("#dcode_err").show();
		return false;
	}else {
		$("#dcode_err").hide();
	}
	
	
	//삭제 계속
	$.ajax({
		type:"post",
		url:"jq_crud_del.jsp",
		data:{"dcode":dcode},
		success:(data) =>{
			console.log("1");
			
			if(data === "false"){
				alert("상품 삭제 실패");
				return false;
			}
			
			$("#delCode").val("");
			$("#delForm").slideToggle("fast");
			dispAll(); //삭제 후 목록 보기
		}, error:() => {
			console.log("delete err");
		}
	});
	
}