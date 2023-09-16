package com.internshala.smartappformeterreading

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

lateinit var btnOk : Button
class SplashPayActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash_pay)

        btnOk = findViewById(R.id.btnOkay)
        btnOk.setOnClickListener{
            val intent = Intent(this@SplashPayActivity, DashBoardActivity::class.java )
            startActivity(intent)

        }
    }
}