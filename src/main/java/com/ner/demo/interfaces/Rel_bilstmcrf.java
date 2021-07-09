package com.ner.demo.interfaces;

import java.io.*;

public class Rel_bilstmcrf implements bilstmcrf{

    @Override
    public void lstm_train(String path1, String path2) throws IOException {
        String env="python";
        File dic=new File(".");
        System.out.println(dic.getCanonicalFile());
        String model=dic.getCanonicalFile()+"/src/main/java/com/ner/demo/python/transform_data.py";
        String  cmd=env+" "+model+" "+path1;
        System.out.println(cmd);
        Runtime run=Runtime.getRuntime();
        try{
            Process process=run.exec(cmd);
            InputStream in=process.getInputStream();
            InputStreamReader reader=new InputStreamReader(in);
            BufferedReader br =new BufferedReader(reader);
            StringBuffer sb=new StringBuffer();
            String message;
            while((message=br.readLine())!=null){
                sb.append(message);
            }
            System.out.println(sb);
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}


