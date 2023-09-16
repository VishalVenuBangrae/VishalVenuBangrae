package com.internshala.smartappformeterreading

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

lateinit var txtSignUp: TextView
lateinit var btnGoToScan: Button

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        txtSignUp = findViewById(R.id.txtDontHaveAccount)
        btnGoToScan = findViewById(R.id.btnLogin)

        txtSignUp.setOnClickListener {
            val intent = Intent(this@LoginActivity, RegisterYourselfActivity::class.java)
            startActivity(intent)
        }
        btnGoToScan.setOnClickListener {
            Toast.makeText(
                this@LoginActivity,
                " You have successfully logged in",
                Toast.LENGTH_SHORT
            ).show()
            val intent = Intent(this@LoginActivity, DashBoardActivity::class.java)
            startActivity(intent)
        }
    }
}