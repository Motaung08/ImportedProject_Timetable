package com.example.pwa;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {
    private WebView mywebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        mywebView = (WebView)findViewById(R.id.web);
        WebSettings webSettings=mywebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        //webSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        mywebView.setWebViewClient(new WebViewClient());
        mywebView.loadUrl("http://10.199.35.20:8000/login/");
    }

    @Override
    public void onBackPressed(){
        if(mywebView.canGoBack()){
            mywebView.goBack();
        }else{
            super.onBackPressed();
        }
    }
}
