var xhr;
var checkFirst = loopSend = false;

function sijak(){
	/*if(event.keyCode == 13){ //엔터키를 눌렀을 경우에만 실행되게 
    	if(checkFirst === false){
			kbs = setTimeout("sendKeyword()", 1000); //일정 시간이 지난 후에 "sendKeyword"를 부름 
			loopSend = true;
		}
    }*/
	if(checkFirst === false){
		kbs = setTimeout("sendKeyword()", 1000); //일정 시간이 지난 후에 "sendKeyword"를 부름 
		loopSend = true;
	}
}


function sendKeyword(){
	if(loopSend === false) return;
	
	var keyWord = document.frm.keyword.value;
	
	if(keyWord === ""){
		hide();
	}else{
		var para = "keyword=" + keyWord;
		
		xhr = new  XMLHttpRequest();
		xhr.open("post", "ajax7.jsp", true);
		xhr.onreadystatechange = function(){
			if(xhr.readyState == 4){
				if(xhr.status == 200){
					processPost();
				}else{
					alert("err : " + xhr.status);
				}
			}
		}
		xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		xhr.send(para);
	}
	//clear Timeout();

}

function processPost(){
	var data = xhr.responseText;
	console.log(data); //받아온거 확인 ex) 5|김뫄뫄,김솨솨,김돠돠 
	var result = data.split("|");
	
	var tot = result[0];  // 건수
	if(tot > 0){ // tot가 0이면 결과값이 없음
		var datas = result[1].split(",");  // | 다음의 이름들
		var imsi = "";
		for(var i = 0; i < datas.length; i++){
			imsi += "<a href=\"javascript:func('" + datas[i] + "')\">" + datas[i] + "</a><br>";
		}
	}
	//console.log(imsi);
	
	var listView = document.getElementById("suggestlist");
	listView.innerHTML = imsi;
	show();
}

function func(arg){
	//console.log("a태그 func");
	//console.log(arg);
	frm.sel.value = arg;
	
	loopSend = checkFirst = false;
	hide();
	frm.keyword.value="";
}
function hide(){
	document.getElementById("suggest").style.display = "none";
}
function show(){
	document.getElementById("suggest").style.display = "";
}