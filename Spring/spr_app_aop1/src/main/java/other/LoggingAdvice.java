package other;

import org.aopalliance.intercept.MethodInterceptor;
import org.aopalliance.intercept.MethodInvocation;

//관심사항(=Aspect)을 기술한 클래스(=Advice)
//관심사항을 별도의 클래스로 만들고 아래 클래스에서 포함해도 됨
//이 경우 큰 내용이 없으므로 바로 여기서 작성
public class LoggingAdvice implements MethodInterceptor{ //메소드 가로채기?
	//MethodInterceptor는 Around Advice를 지원
	
	public Object invoke(MethodInvocation invocation) throws Throwable {
		//핵심 로직 클래스의 임의의 메소드 앞,뒤에 관심사항(login, transaction, security ... )을 적용
		//target 메소드명 얻기(타겟 메소드는 메타파일에서 지정)
		String methodName = invocation.getMethod().getName();
		System.out.println("호출된 메소드 이름 : " + methodName);
		
		//핵심 메소드 수행 - sayHi()를 지정할 예정
		Object object = invocation.proceed(); //<value>.*sayHi*.</value>
		
		System.out.println(methodName + " 수행 후 마무리 작업");
		return object;
	}
}
