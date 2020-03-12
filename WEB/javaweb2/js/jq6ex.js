$(document).ready(()=>{
	$("#btnOk").on("click", () => {
		$("#showJ").empty();
		$("#cntJ").empty();
		$("#showC").empty();
		var buserName = $("#buser").val();
		
		$.ajax({
			type:"get",
			url:"jq6exjson.jsp",
			data: "bName=" + buserName,
			dataType:"json",
			success:(data) => {
				
				var cnt = 0;
				var str = "<table border='1' style='border-collapse:collapse; width:800px;'>";
				str += "<tr><th>직원번호</th><th>직원명</th><th>부서전화</th><th>관리 고객 수</th></tr>";
				
				$.each(data, (index, value) => {
					str += "<tr><td class='jno'>" + value["no"] + "</td>";
					str += "<td><a href='#' class='jikwon'>" + value["name"] + "</a></td>";
					str += "<td>" + value["buserTel"] + "</td>";
					str += "<td>" + value["gogeksu"] + "</td></tr>";
					cnt++;
				});
				str += "</table>";

				$("#showJ").append(str); 
				$("#cntJ").append(cnt + "명");
				
				
				
				/////////// 직원이 담당하는 고객 명단 출력하기
				$(".jikwon").on("click", function() {
					$("#showC").empty();
					var jikwonName = $(this).text();
					var jikwonNo = $(this).parent().prev(".jno").text();
					//console.log(jikwonName + " / " + jikwonNo);
					
					$.ajax({
						type:"post",
						url:"jq6exjson2.jsp",
						data: "jName=" + jikwonName + "&jNo=" + jikwonNo,
						dataType:"json",
						success:(data) => {
							
							var re = "<table border='1' style='border-collapse:collapse; width:400px;'";
							re += "<tr><th>고객명</th><th>고객전화</th><th>성별</th></tr>";
							$.each(data, (index, value) => {
								re += "<tr><td>" + value["name"] + "</td>";
								re += "<td>" + value["tel"] + "</td>";
								re += "<td>" + value["gen"] + "</td></tr>";
							});
							re += "</table>";
							
							$("#showC").append(re);
						}
					});
				});
				/////////// 직원이 담당하는 고객 명단 출력하기
				
			}, error: () => {
				alert("err");
			},statusCode:{
				200:() => { console.log("읽기 성공");	},
				404:() => { console.log("찾기 실패");	}
			}
		});
	});
});

