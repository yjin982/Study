package pack1;

import org.bson.Document;

import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

public class DbMongo {

	public DbMongo() {
		try {
			MongoClient client = new MongoClient("localhost", 27017);
			MongoDatabase db = client.getDatabase("test");
			MongoCollection<Document> collection = db.getCollection("user");
			
			
			////자료추가
			Document ins_doc = new Document("name", "나이스").append("age", "33").append("job", "음악가");
			collection.insertOne(ins_doc);
			System.out.println("건수 : " + collection.countDocuments());
			
			
			Document doc = collection.find().first();
			System.out.println("첫번째 자료 : " + doc.toJson());
			System.out.println();
			
			
			/*FindIterable<Document> iter = collection.find();
			MongoCursor<Document> cursor = iter.iterator(); 줄이면*/
			MongoCursor<Document> cursor = collection.find().iterator();
//			MongoCursor<Document> cursor = collection.find().limit(2).iterator(); //limit 2개 만 받아오기
			

			
			/*
			while(cursor.hasNext()) {
				//Document document = cursor.next();
				//String jsonResult = document.toJson();  줄이면
				String jsonResult = cursor.next().toJson();
				System.out.println(jsonResult);
			}
			*/
			cursor = collection.find().iterator();
			while(cursor.hasNext()) {
				Document document2 = cursor.next();
				System.out.println("이름:" + document2.get("name") + ", 나이:" + document2.get("age") + ", 직업:" + document2.get("job"));
			}
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	
	public static void main(String[] args) {
		new DbMongo();
	}

}
