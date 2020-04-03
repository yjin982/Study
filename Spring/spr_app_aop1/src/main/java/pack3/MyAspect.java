package pack3;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class MyAspect {
	//핵심 메소드 수행 전후에 관심사항 코드를 기술
	//앞뒤로 적용될때 around
	@Around("execution(public void selectDataProcess())") 
	public Object kbs(ProceedingJoinPoint joinPoint) throws Throwable{ 
		//지정된 핵심 메소드 이름 얻기
		String methodName = joinPoint.getSignature().toString();
		
		System.out.println(methodName + " 시작 전에 어떤 작업을 수행(ex:로그인, 보안설정, 트랜잭션 등등)");
		Object object = joinPoint.proceed(); // 이 코드에 의해 지정된 인터셉트 대상 핵심 메소드가 수행됨.
		System.out.println(methodName + " 처리 후에 어떤 작업을 수행");
		System.out.println("-------------------------------------------");
		
		return object;
	}
	
	@Before("execution(public void updateDataPart())") //execution하나만 적용할때
	public void mbc(){
		System.out.println("해당 메소드 처리 !!전!!에 추가기능인 mbc가 수행");
	}
}
