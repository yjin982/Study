package pack.model;

import java.util.Calendar;

import org.springframework.stereotype.Component;

//mvc 중 모델 영역
@Component
public class HelloModel {
	public String getGreeting() {
		int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
		
		if(hour >= 6 && hour <= 10) {
			return "좋은 아침";
		}else if(hour >= 12 && hour <= 15){
			return "맛점";
		}else if(hour >= 18 && hour <= 22) {
			return "좋은 저녁 되세요";
		}else {
			return "안녕하세요";
		}
	}
}
