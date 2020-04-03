package pack3;

import org.springframework.stereotype.Repository;

//가독성을 위해서 @Component 가 아니라 레파지토리(DB처리쪽은 레파지토리로 씀)
@Repository("articleDao")
public class ArticleDao implements ArticleInter{
	//DB처리 관련 클래스(모델쪽)
	
	public void selectAll() {
		System.out.println("ArticleDAO의 selectAll()에서 DB의 고객 전체 자료 읽었다고 가정");
	}
}
