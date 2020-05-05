package com.example.garagedoorcontroller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView

class GarageOpenActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_garage_open)

        val myWebView = WebView(this)
        setContentView(myWebView)
        myWebView.loadUrl("http://70.123.32.254:1234/login")

    }
}
