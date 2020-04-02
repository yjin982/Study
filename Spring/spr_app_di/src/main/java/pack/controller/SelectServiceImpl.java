package pack.controller;

import pack.model1.DataDaoInter;

public class SelectServiceImpl implements SelectService{
	//private DataDaoImpl daoImpl; //포함관계 (상속(extends)로도 가능하나 강결합이라 비추)
	private DataDaoInter daoInter; 
	
	public SelectServiceImpl(DataDaoInter daoInter) {
		//생성자를 통해 DataDaoInter객체의 파생 객체의 주소를 치환
		System.out.println("selectServiceImpl 생성자 수행");
		this.daoInter = daoInter;
	}
	
	public void selectProcess() {
		System.out.println("selectProcess 에서 DataDaoInter의 메소드 수행");
		daoInter.selectDb();
	}
	
}
