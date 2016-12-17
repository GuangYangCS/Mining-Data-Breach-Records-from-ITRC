/*
 *Authors: Hao Guo, Guang Yang, Shengzhe Qu, Shuchi Gan, Wen Chen Wu
 *Date: 12/01/2016
 *This program is for BigData team project whose title is "Mining Data Breach Records from ITRC";
 *This program could extract breach categories and content information for each report in report files;
 *The final generated file will be the form as "Breach_Category :: Number_of_Reports :: Content_Information";
 *
 * */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HandledPDF {
	public static void main(String[] args){
		Scanner sc2 = null;
		PrintWriter out = null;
		
		try {
			//specify the output file
			out = new PrintWriter("C:\\Users\\Hao\\Desktop\\Big Data\\newGenerated.txt");
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		
	    try {
	    	//specify the input file
	        sc2 = new Scanner(new File("C:\\Users\\Hao\\Desktop\\Big Data\\ITRCBreachReport2016.txt"));
	    } catch (FileNotFoundException e) {
	        e.printStackTrace();  
	    }
	    
	    while (sc2.hasNextLine()) {
	    	String curLine = sc2.nextLine();
	    	if(curLine.startsWith("ITRC2016")){
	    		String t = curLine;
	    		while(t.indexOf("Paper Data") == -1 && t.indexOf("Electronic") == -1) t = sc2.nextLine();
	    		if(t.indexOf("Paper Data") != -1){
	    			t = t.substring(t.indexOf("Paper Data"));
	    			String[] sarr = t.split(" ");
	    			if(sarr.length > 2) out.print(sarr[2]);
	    		}else if(t.indexOf("Electronic") != -1){
	    			t = t.substring(t.indexOf("Electronic"));
	    			String[] sarr = t.split(" ");
	    			if(sarr.length >= 2) out.print(sarr[1]);
	    		}
	    		
	    		out.print("::");
	    		
	    		while(true){
	    			String t1 = sc2.nextLine();
	    			if(t1.startsWith("Attribution")) break;
	    			out.print(t1);
	    		}
	    		out.println("");
	    	}
	    }
	    
	    
	    try {
			out = new PrintWriter("C:\\Users\\Hao\\Desktop\\Big Data\\newGenerated_1.txt");
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		
	    try {
	        sc2 = new Scanner(new File("C:\\Users\\Hao\\Desktop\\Big Data\\newGenerated.txt"));
	    } catch (FileNotFoundException e) {
	        e.printStackTrace();  
	    }
	    
	    while (sc2.hasNextLine()) {
	    	String t = sc2.nextLine();
	    	if(!t.startsWith("::")){
	    		out.println(t);
	    	}
	    }
	    
	    
	    try {
			out = new PrintWriter("C:\\Users\\Hao\\Desktop\\Big Data\\newGenerated_2.txt");
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		}
		
	    try {
	        sc2 = new Scanner(new File("C:\\Users\\Hao\\Desktop\\Big Data\\newGenerated_1.txt"));
	    } catch (FileNotFoundException e) {
	        e.printStackTrace();  
	    }
	    
	    Map<String, String> map = new HashMap<>();
	    Map<String, Integer> map1 = new HashMap<>();
	    while(sc2.hasNextLine()){
	    	String t = sc2.nextLine();
	    	String[] tarr = t.split("::");
	    	if(tarr.length >= 2){
	    		if(map.containsKey(tarr[0])){
		    		map.put(tarr[0], map.get(tarr[0])+tarr[1]);
		    	}else{
		    		map.put(tarr[0], tarr[1]);
		    	}
		    	if(map1.containsKey(tarr[0])){
		    		map1.put(tarr[0], map1.get(tarr[0])+1);
		    	}else{
		    		map1.put(tarr[0], 1);
		    	}
	    	}
	    }
	    
	    for(String key: map.keySet()){
	    	out.print(key);
	    	out.print("::");
	    	out.print(map1.get(key));
	    	out.print("::");
	    	out.println(map.get(key));
	    }
	    
	}
}
