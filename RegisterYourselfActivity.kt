package com.internshala.smartappformeterreading

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

lateinit var btnRegister: Button

class RegisterYourselfActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register_yourself)

        btnRegister = findViewById(R.id.btnSignUp)
        btnRegister.setOnClickListener {
            val intent = Intent(this@RegisterYourselfActivity, LoginActivity::class.java)
            startActivity(intent)
        }
    }
}