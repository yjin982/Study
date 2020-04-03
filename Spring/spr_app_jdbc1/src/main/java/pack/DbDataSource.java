package pack;

import org.springframework.jdbc.datasource.DriverManagerDataSource;


public class DbDataSource extends DriverManagerDataSource{
	public DbDataSource() {
		setDriverClassName("org.mariadb.jdbc.Driver");
		setUrl("jdbc:mysql://localhost:3306/test");
		setUsername("root");
		setPassword("123");
	}
}
