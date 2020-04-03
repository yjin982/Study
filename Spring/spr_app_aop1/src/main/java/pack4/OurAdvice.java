package pack4;

import java.util.Scanner;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class OurAdvice {
	@Around("execution(public void startProcess())")
	public Object trace(ProceedingJoinPoint joinPoint) throws Throwable{
		System.out.println("AOP 시작 : 핵심 메소드 수행 전에 id 검증");
		System.out.print("input id : ");
		Scanner scanner = new Scanner(System.in);
		String id = scanner.nextLine();
		
		if(! id.equals("aa")) {
			System.out.println("id 불일치! 아쉽지만 핵심을 못 보고 안녕!");
			return null;
		}
		Object object = joinPoint.proceed();
		return object;
	}
}
