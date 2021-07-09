package com.ner.demo.interfaces;

import java.io.IOException;

public interface bilstmcrf {
    public abstract void lstm_train(String path1,String path2) throws IOException;
}
