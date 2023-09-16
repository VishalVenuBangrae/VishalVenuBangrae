package com.internshala.smartappformeterreading

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

lateinit var btnGetBill : Button

class ScanElectricityActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_scan_electricity)

        btnGetBill = findViewById(R.id.btnGetBill)

        btnGetBill.setOnClickListener {
            val intent = Intent(this@ScanElectricityActivity, BillActivity::class.java)
            startActivity(intent)
        }

    }
}
