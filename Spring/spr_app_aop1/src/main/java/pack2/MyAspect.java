package pack2;

import org.aspectj.lang.ProceedingJoinPoint;

public class MyAspect {
	//핵심 메소드 수행 전후에 관심사항 코드를 기술
	public Object kbs(ProceedingJoinPoint joinPoint) throws Throwable{ 
		//지정된 핵심 메소드 이름 얻기
		String methodName = joinPoint.getSignature().toString();
		
		System.out.println(methodName + " 시작 전에 어떤 작업을 수행(ex:로그인, 보안설정, 트랜잭션 등등)");
		Object object = joinPoint.proceed(); // 이 코드에 의해 지정된 인터셉트 대상 핵심 메소드가 수행됨.
		System.out.println(methodName + " 처리 후에 어떤 작업을 수행");
		
		return object;
	}
}
