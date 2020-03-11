function chkData(){
	if(frm.name.value === "" || isNaN(frm.name.value) == false){
		frm.name.focus();
		alert("이름을 입력하시오(문자로)");
		return;
	}
	if(frm.id.value === "" || frm.id.value.length < 2){
		frm.id.focus();
		alert("아이디는 2자 이상");
		return;
	}
	//frm.email.value.indexOf("@") === -1 || frm.email.value.indexOf(".") === -1 이 조건 보다 좀더 정확하게 하려면 정규표현식으로
	//정규 표현식으로 이메일 검사
	var regExp = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;
	if(frm.email.value === "" || !frm.email.value.match(regExp)){
		frm.email.focus();
		alert("이메일을 정확히 입력!");
		return;
	}
	//정규 표현식 나이
	var regExp2 = /^[0-9]{1,2}$/; 
	if(frm.age.value === "" || !frm.age.value.match(regExp2)){
		frm.age.focus();
		alert("나이는 숫자 입력!");
		return;
	}
	
	//html 애트리뷰트 말고 여기서 적어도 괜춘
	frm.action = "js11form.jsp";
	frm.method = "post";
	frm.submit();
}
function clsData(){
	frm.name.focus();
}