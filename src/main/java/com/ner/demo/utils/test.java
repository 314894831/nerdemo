package com.ner.demo.utils;

import com.ner.demo.interfaces.Rel_bilstmcrf;

import java.io.*;

public class test {
    public static void main(String[] args) throws IOException {
        Rel_bilstmcrf R1=new Rel_bilstmcrf();
        R1.lstm_train("C:\\Users\\Bcopton\\Desktop\\sourse_data","");



//        String env="python";
//        File dic=new File(".");
//        System.out.println(dic.getCanonicalFile());
//        String model=dic.getCanonicalFile()+"/src/main/java/com/ner/demo/python/test.py";
//        String cmd=env+" "+model;
//        System.out.println(cmd);
//        Runtime run=Runtime.getRuntime();
//        try{
//            Process process=run.exec(cmd);
//            InputStream in=process.getInputStream();
//            InputStreamReader reader=new InputStreamReader(in);
//            BufferedReader br =new BufferedReader(reader);
//            StringBuffer sb=new StringBuffer();
//            String message;
//            while((message=br.readLine())!=null){
//                sb.append(message);
//            }
//            System.out.println(sb);
//        }
//        catch (IOException e){
//            e.printStackTrace();
//        }
    }
}
