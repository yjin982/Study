function zipCheck() {
	url = "zipcheck.jsp?check=y"; //동 이름을 입력하는 창을 띄우기
	window.open(url, "post", "toolbar=no,width=500,height=500, top=100,left=600,status=yes,scrollbars=yes,menubar=no");
}

function idCheck() {
	if(regForm.id.value == ""){
		alert("아이디를 입력하세요");
		regForm.id.focus();
	}else{
		url = "idcheck.jsp?id=" + regForm.id.value;
		window.open(url, "id", "toolbar=no,width=500,height=200, top=100,left=600");		
	}
}

function inputCheck() {
	if(regForm.id.value === ""){
		alert("아이디를 입력하세요");
		regForm.id.focus();
		return false;
	}
	// ... 나머지 생략
	if(regForm.job.value === "0"){
		alert("직업을 선택하세요");
		regForm.job.focus();
		return false;
	}
	regForm.submit();
}

function productDetail(no){ //관리자,고객에서 상품 처리 시
	//alert("상품번호 " + no);
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

function productUpdate(no){ // 관리자에서 상품수정
	//alert("상품번호 " + no);
	document.updateFrm.no.value = no;
	document.updateFrm.submit();
}

function productDelete(no){// 관리자에서 상품삭제
	//alert("상품번호 " + no);
	if(confirm("정말 삭제할까요?")){
		document.delFrm.no.value = no;
		document.delFrm.submit();		
	}
}

//카트 처리용 함수
function cartUpdate(form){
	form.flag.value = "update";
	//alert(form.flag.value);
	form.submit();
}

function cartDelete(form){
	form.flag.value = "del";
	//alert(form.flag.value);
	form.submit();
}

function productDetail(no){
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

function orderDetail(no){
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

//관리자 주문 상세 처리 관련
function orderUpdate(form){
	document.detailFrm.flag.value = "update";
	form.submit();
}

function orderDelete(form){
	document.detailFrm.flag.value = "delete";
	form.submit();
}
