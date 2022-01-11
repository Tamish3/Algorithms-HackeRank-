// Student class
class Student {
	String name;
	int studentID;

	// static variable
	static String collegeName;

	// static counter to set unique roll no
	static int counter = 0;

	public Student(String name)
	{
		this.name = name;
		this.studentID = setStudentID();
	}

	// getting unique rollNo
	// through static variable(counter)
	static int setStudentID()
	{
		counter++;
		return counter;
	}

	// static method
	static void setCollege(String name) {
    collegeName = name;
  }

	// instance method
	void getStudentInfo()
	{
		System.out.println("name : " + this.name);
		System.out.println("studentID : " + this.studentID);

		// accessing static variable
		System.out.println("College Name : " + collegeName);
	}
}

// Driver class
public class StaticDemo {
	public static void main(String[] args)
	{
		Student.setCollege("UMD");

		Student s1 = new Student("Ram");
		Student s2 = new Student("Matt");

		s1.getStudentInfo();
		s2.getStudentInfo();
	}
}
