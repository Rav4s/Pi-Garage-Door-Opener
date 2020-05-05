package com.example.garagedoorcontroller

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView

class CheckSensor : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_check_sensor)

        val myWebView = WebView(this)
        setContentView(myWebView)
        myWebView.loadUrl("http://70.123.32.254:1234/sensor")

    }
}