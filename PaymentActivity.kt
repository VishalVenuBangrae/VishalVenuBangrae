package com.internshala.smartappformeterreading

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast

lateinit var btnGo : Button
class PaymentActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_payment)
        btnGo = findViewById(R.id.btnProceed)

        btnGo.setOnClickListener {
            Toast.makeText(this@PaymentActivity," You have successfully paid the bill" , Toast.LENGTH_SHORT).show()
            val intent = Intent(this@PaymentActivity, SplashPayActivity::class.java)
            startActivity(intent)
        }

    }
}