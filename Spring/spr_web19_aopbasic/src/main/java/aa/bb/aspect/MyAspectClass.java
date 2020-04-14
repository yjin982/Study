package aa.bb.aspect;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Aspect
@Component //aspect와 같이 써주는게 좋음
public class MyAspectClass {
	@Autowired
	private SecurityClass class1;
	
	@Around("execution(public String processMsg()) or execution(* bu*(..))") //표현식 혹은 특정 메소드만
	public Object AopProcess(ProceedingJoinPoint joinPoint) throws Throwable{
		
		class1.MySecurity(); //핵심 메소드 수행 전에 
		
		Object object = joinPoint.proceed(); //핵심 메소드 호출
		
		System.out.println("핵심 메소드 수행 >후< 뭔가를 진행");
		
		return object; //오브젝을 리턴하면 비즈니스 로직으로 넘어감, null 이면 ㄴㄴ
	}
}
