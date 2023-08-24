import java.io.*;
import java.io.IOException;

public class io {
	
	public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
	
	public static void printInteger(int a)
	{
		System.out.println(a);
	}

	public static void printFloat(float a)
	{
		System.out.println(a);
	}

    public static void printDouble(double a)
	{
		System.out.println(a);
	}

	public static void printString(String a)
	{
		System.out.println(a);
	}

    public static void printChar(char a)
	{
		System.out.println(a);
	}

	public static void printBoolean(boolean a)
    {
        System.out.println(a);
    }

    public static String readString() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

    public static char readChar() {
        char tmp = '\0';
        try {
            tmp = input.readLine().charAt(0);
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

	public static int readInteger() {
		int tmp = 0;
        try {
            tmp = Integer.parseInt(input.readLine());
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

	public static float readFloat() {
		float tmp = 0;
        try {
            tmp = Float.parseFloat(input.readLine());
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

    public static double readDouble() {
		double tmp = 0;
        try {
            tmp = Double.parseDouble(input.readLine());
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

	public static boolean readBoolean() {
		boolean tmp = true;
        try {
            tmp = Boolean.parseBoolean(input.readLine());
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }
    
    public static void close() {
    	try {
    		writer.close();
    	} catch (IOException e) {
			e.printStackTrace();
		}
    }
}