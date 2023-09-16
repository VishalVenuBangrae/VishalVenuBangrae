package com.internshala.smartappformeterreading

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.cardview.widget.CardView

lateinit var scanNow: CardView

class DashBoardActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dash_board)

        scanNow = findViewById(R.id.card)
        scanNow.setOnClickListener {
            val intent = Intent(this@DashBoardActivity, ScanElectricityActivity::class.java)
            startActivity(intent)
        }
    }
}