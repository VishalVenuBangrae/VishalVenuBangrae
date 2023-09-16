package com.internshala.smartappformeterreading

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast

lateinit var btnPayNow : Button
class BillActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_bill)

        btnPayNow = findViewById(R.id.btnPayNow)

        btnPayNow.setOnClickListener {
            val intent = Intent(this@BillActivity, PaymentActivity::class.java)
            startActivity(intent)

        }
    }
}