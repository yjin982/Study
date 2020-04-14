package pack.aspect;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class MyAdvice {
	@Autowired
	private LoginClass loginClass;
	
	@Around("execution(* aa(..))") //포인트컷으로 조인포인트 대상을 지정
	public Object aopProcess(ProceedingJoinPoint joinPoint) throws Throwable{
		HttpServletResponse response = null;
		HttpServletRequest request = null;
		
		for(Object obj : joinPoint.getArgs()) { //
			if(obj instanceof HttpServletResponse) { //obj 에 response 객체가 있으면 
				response = (HttpServletResponse)obj;
			}
			if(obj instanceof HttpServletRequest) {
				request = (HttpServletRequest)obj;
			}
		}
		
		if(loginClass.loginCheck(request, response)) { //logincheck으로 로그인이 안된 것을 확인 되면
			return null; //null을 리턴함으로써 핵심로직 실행 하지 않음
		}
		
		//핵심 로직으로 간다는 의미
		Object object = joinPoint.proceed();
		return object;
		
	}
}
